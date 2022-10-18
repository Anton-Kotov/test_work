import os

from login_user import login


def delete_me():

    user = login()
    if user[0] == True:
        os.remove(f"{user[1]}")
