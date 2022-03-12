import vk_api
from datetime import datetime


LOGIN = input("логин: ")  # adislan2017@gmail.com
PASSWORD = input("пароль: ")  # 270607adislan

filename = input()  # img.jpg
album_id = input()  # album-211434200_282939525
group_id = input()  # club211434200

data = []


def upload(filename, album_id, group_id, vk):
    upload = vk_api.VkUpload(vk)
    photo = upload.photo(group_id=group_id, album_id=album_id, photos=[fr"static\img\{filename}"])

    vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"

    print(photo, vk_photo_id, sep="\n")
    vk.wall.post(message="Test", attachments=[vk_photo_id])


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    upload(filename=filename, album_id=album_id, group_id=group_id, vk=vk)


if __name__ == '__main__':
    main()