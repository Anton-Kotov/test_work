import glob
import json

login_user = input('login: ')

def login(login_user):

    all_users = glob.glob("*.json")

    for user in all_users:                          # Здесь и далее исходим из того, что логин уникальный

        if user.split('_')[0] == login_user:
            with open(f'{user}', 'r') as f:
                user_info = json.load(f)
                if user_info[0] == login_user:

                    while user_info[2] != input('password: '):
                        pass
                    return True
    print('Такого пользователя нет')
    return False

