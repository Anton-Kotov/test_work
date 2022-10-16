import validators as validators


def password_test(password):

    par1, par2, par3, par4 = False, False, False, False

    if len(password) >= 12:
        par1 = True

    for el in password:

        if el.isupper():
            par2 = True
        elif el.islower():
            par3 = True
        if el.isdigit():
            par4 = True

    if par1 == par2 == par3 == par4 == True:
        return True
    else:
        return False



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

    print(username, email, password)

register_user()