import datetime
import json

import validators as validators


def password_test(password):
    check_lst = [False, False, False, False]  # 4 критерия правильности пароля

    if len(password) >= 12:
        check_lst[0] = True

    for el in password:

        if el.isupper():
            check_lst[1] = True
        elif el.islower():
            check_lst[2] = True
        if el.isdigit():
            check_lst[3] = True

    for i in check_lst:
        if not i:
            return False
    return True


def register_user():
    username = input('username: ')
    email = input('email: ')

    while validators.email(email) != True:
        email = input('email: ')

    password = input('password: ')
    while not password_test(password):
        print('- Длинна пароля не меньше 12 символов\n'
              '- Содержит хотя бы 1 букву в ВЕРХНЕМ регистре\n'
              '- Содержит хотя бы 1 букву в нижнем регистре\n'
              '- Содержит хотя бы 1 цифру')
        password = input('password: ')

    return [username, email, password]


user_date = register_user()

with open(f'{user_date[0]}_{datetime.datetime.today().date()}.json', 'w') as f:
    json.dump(user_date, f)
