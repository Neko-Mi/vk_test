import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
# import pymysql.cursors
import requests,time
import httplib2
from bs4 import BeautifulSoup
import json
import random



neko = ['неко', 'енко', 'neko', 'enko', 'ekon', 'nkeo']
search = ['search', 'поиск', 'гугл']

vk_session = vk_api.VkApi(token="4c6103998d2af42e1a04672def9ffe6dc5bbae6f79ac2e2e5cd73973ade0ccccbff108b3c896e212246ef")
#пример  vk_session = vk_api.VkApi(token = "a6f87v8c9a9sa87a7af9a0f9f9v8a6s6c5b5m6n8bds09asc8d7b87d87bd87n"


def send_photo(msg):
    ck = vk_api.VkApi(token="db5dc6b0db5dc6b0db5dc6b00cdb307695ddb5ddb5dc6b086e58049a30ffd7b2aae27e4")
    for s in search:
        msg = msg.replace(s, '')

    q = '#' + msg.replace(' ', '')
    print(q)
    post = ck.method('newsfeed.search', values={'q': q})
    with open("data.json", "w") as write_file:
        json.dump(post, write_file)
    # print(len(post))

    photo_id = []
    rand = random.randint(0, 50)
    # rand = 100
    i = 0
    print('rand:', rand)

    # ind = 0
    for p in post['items']:
        print(p['id'])
        try:
            attachment = p['attachments']



            for a in attachment:
                print(a['type'])
                print(i)
                
                if a['type'] == 'photo':
                    # print(a['photo'])
                    i += 1
                    photo_owner_id = a['photo']['owner_id']
                    photo_id = a['photo']['id']
                    # break

                if photo_id != [] and i >= rand:
                    break
        except:
            print(p['id'], 'don`t have "attachments"')
                

        if photo_id != [] and i >= rand:
            break
    try:
        photo_att = 'photo{}_{}'.format(
            # f['items'][0]['attachments'][0]['photo']['owner_id'], f['items'][0]['attachments'][0]['photo']['id']
            photo_owner_id, photo_id
        )
        print(photo_att)
        return photo_att
    except:
        print('ничего не нашел')
    



# def upload():
#     url="https://vk.com/search?c%5Bper_page%5D=40&c%5Bq%5D=%23neko&c%5Bsection%5D=statuses"
#     html = requests.post(url)
#     # soup = BeautifulSoup(html, 'lxml')
#     print(html)

#     img_url = soup.find('a', 'showPhoto').get('src')
#     print(img_url)

#     vk_photo = VkUpload(vk_session)

#     h = httplib2.Http('.cache')
#     response, content = h.request(img_url)
#     out = open('img.png', 'wb')
#     out.write(content)
#     out.close()

#     photo = vk_photo.photo_messages('img.png')

#     photo_att = 'photo{}_{}'.format(
#         photo[0]['owner_id'], photo[0]['id']
#     )

#     return photo_att



vk = vk_session.get_api()
vk.messages.send(
    peer_id=2000000002,
    random_id=get_random_id(),
    message="Kon'nichiwa nyaaa!"
)

longpoll = VkBotLongPoll(vk_session, "188055889")


for event in longpoll.listen(): #Проверка действий
    # print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        #проверяем не пустое ли сообщение нам пришло
        if event.obj.text != '' and event.from_chat: 
            msg = event.obj.text.lower()

            print(event.obj.text)
            print(event.obj.peer_id)
            # print(event.obj)

            # vk.messages.send(
            #     peer_id=event.obj.peer_id,
            #     random_id=get_random_id(),
            #     message="*id" + str(event.obj.from_id) + " " + event.obj.text.lower() + " nya!"
            # )


            if msg in neko: 
                # send_photo('neko')
                vk.messages.send(
                    peer_id=event.obj.peer_id,
                    random_id=get_random_id(),
                    message='Nekochan nyaaa!',
                    attachment=send_photo('neko')
                )

            if msg.split(' ')[0] in search:
                vk.messages.send(
                    peer_id=event.obj.peer_id,
                    random_id=get_random_id(),
                    message='Nekochan nyaaa!',
                    attachment=send_photo(msg)
                )




            if msg == 'exit':
                vk.messages.send(
                    peer_id=2000000002,
                    random_id=get_random_id(),
                    message="Sayonara nyaaa!"
                )
                break