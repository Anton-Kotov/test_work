from delete_me import delete_me
from login_user import login
from logout_user import logout
from nums_key import send_message
from register_user import register_user

def commands():

    while True:
        request = input('request: ')
        # request_dict = {
        #     'register': register_user(),
        #     'login': login(),
        #     'logout': logout(),
        #     'delete_me': delete_me(),
        #     'send_message': send_message()
        # }

        # request_dict[request]
        if request == 'register':       #  получилось криво
            register_user()
        elif request == 'login':
            login()
        elif request == 'logout':
            logout()
        elif request == 'delete_me':
            delete_me()
        elif request == 'send_message':
            print(send_message())
        else:
            print('Нет такой команды')

commands()