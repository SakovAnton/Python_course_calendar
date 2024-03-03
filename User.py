"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""
import functools


##from Backend import Backend


class User:
    _users_passwords = {}
    _users_logins = {}
    _name_user = ''
    _id_user = ''
    _type_user = ''
    _login_user = ''
    _password_user = ''

    #    backend = Backend()

    # def __new__(cls, name_user=None, login_user=None, password_user=None):
    #
    #     if name_user not in Backend.get_all_users(Backend):
    #         #Backend.create_user(Backend, name_user)
    #         return super().__new__(cls)
    #     else:
    #         # raise NameError(f'Пользователь с таким "{name_user}" именем ужже существует')
    #         print(f'Пользователь с таким "{name_user}" именем ужже существует')

    def __init__(self, name_user=None, login_user=None, password_user=None):

        if name_user:
            self._name_user = '@' + name_user

        if login_user:
            self._login_user = login_user

        if password_user:
            self._users_passwords[self._name_user] = password_user

    def __str__(self):
        return f'Имя: {self._name_user}\n' \
               f'Login: {self._login_user}\n' \

    # def unic_name(self ):
    #     @functools.wraps(func)
    #     def wrapper():

    def get_password(self):
        return self._password_user

