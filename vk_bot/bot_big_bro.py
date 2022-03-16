import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random


TOKEN = "e6e57b9973f18bb99accb41b9d55da24749a6c708b12421cd5be87acc5a10b8f9337728c15e8228c77a54"

vk = vk_api.VkApi(token=TOKEN)
longpoll = VkLongPoll(vk)


def send_msg(chat_id, text):
    random_id = random.randint(0, 999999999999)
    vk.method("messages.send", {"chat_id": chat_id, "message": text, "random_id": random_id})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            chat_id = event.chat_id
            msg = vars(event)
            if event.from_chat:
                bad_words = ["привет", "пока"]
                if msg in bad_words:
                    send_msg(chat_id=chat_id, text="вы использовали запретное слово")
                else:
                    print(msg)
                    send_msg(chat_id=chat_id, text=msg)
