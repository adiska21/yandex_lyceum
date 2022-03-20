import vk_api

TOKEN = "e6e57b9973f18bb99accb41b9d55da24749a6c708b12421cd5be87acc5a10b8f9337728c15e8228c77a54"


def main():
    vk_session = vk_api.VkApi("adislan2017@gmail.com" "270607adislan")
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    # Используем метод wall.get
    response = vk.users.get(user_id=617475448)
    print(response)


if __name__ == '__main__':
    main()