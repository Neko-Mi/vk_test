import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.upload import VkUpload
# import pymysql.cursors
import requests,time


vk_session = vk_api.VkApi(token="4c6103998d2af42e1a04672def9ffe6dc5bbae6f79ac2e2e5cd73973ade0ccccbff108b3c896e212246ef")
#пример  vk_session = vk_api.VkApi(token = "a6f87v8c9a9sa87a7af9a0f9f9v8a6s6c5b5m6n8bds09asc8d7b87d87bd87n"
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, "188055889")

vk_photo = VkUpload(vk_session)
# upload_url = vk_photo.photo_messages('https://i.redd.it/tonb6ujeb7u21.jpg')

import httplib2
start = time.time()

h = httplib2.Http('.cache')
response, content = h.request('https://i.redd.it/tonb6ujeb7u21.jpg')
out = open('img.png', 'wb')
out.write(content)
out.close()
print(time.time()-start)

photo = vk_photo.photo_messages('img.png')
print(time.time()-start)

photo_att = 'photo{}_{}'.format(
        photo[0]['owner_id'], photo[0]['id']
    )


vk.messages.send(
    peer_id=2000000002,
    random_id=get_random_id(),
    message="Kon'nichiwa nyaaa!"
)

vk.messages.send(
    peer_id=2000000001,
    random_id=get_random_id(),
    message="Kon'nichiwa nyaaa!"
)

#пример longpoll = VkBotLongPoll(vk_session, "637182735")
for event in longpoll.listen(): #Проверка действий
    # print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        #проверяем не пустое ли сообщение нам пришло
        if event.obj.text != '' and event.from_chat: 
            msg = event.obj.text.lower()
            #проверяем пришло сообщение от пользователя или нет
            print(event.obj.text)
            print(event.obj.peer_id)

            if msg == 'neko': #Если написали в Беседе
                # vk_photo.photo_messages('https://i.redd.it/tonb6ujeb7u21.jpg')
                vk.messages.send(
                    peer_id=event.obj.peer_id,
                    random_id=get_random_id(),
                    message='Nekochan nyaaa!',
                    attachment=photo_att
                )
            if msg == 'exit':
                vk.messages.send(
                    peer_id=2000000002,
                    random_id=get_random_id(),
                    message="Sayonara nyaaa!"
                )
                vk.messages.send(
                    peer_id=2000000001,
                    random_id=get_random_id(),
                    message="Sayonara nyaaa!"
                )
                break