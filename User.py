"""
Пользователь - имеет логин и пароль, а так же календарь.
у пользователя есть итендифекатор начинающийся с @
"""


class User:
    _users_passwords = {}
    _users_logins = {}
    _name_user = ''
    _id_user = ''
    _type_user = ''
    _login_user = ''
    _password_user = ''

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


