"""
Сущность, отвечающая за хранение и предоставление данных
Оно хранит пользователей, календари и события.
Хранение, в том числе означает сохранение между сессиями в csv файлах
(пароли пользователей хранятся как hash)

Должен быть статическим или Синглтоном

*) Нужно хранить для каждого пользователя все события которые с нима произошли но ещё не были обработаны.
"""
from User import User
from Calendar import Calendar
import hashlib


class Backend:
    _instance = None
    _users = dict()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance

    def create_user(self, user=None, login='', password='', password_hash=''):
        if user not in self.get_all_name_users():
            _login = '@' + user
            if password:
                # _password = hash(password)
                _password = hashlib.sha256(password.encode()).hexdigest()
            if password == '' and password_hash:
                _password = password_hash

            self._users[user] = [_login, _password]
            User(name_user=user, login_user=login, password_user=password)
        else:
            print(f'Пользователь с таким "{user}" именем ужже существует')

    def create_calendar(self, user):
        if user in self._users:
            Calendar(user)
        else:
            print(f'Календарь не возможно создать: {user} не существует.')

    def login_user(self, user, password):
        if self.get_password_user(user) == hashlib.sha256(password.encode()).hexdigest():
            return True
        else:
            return False

    def get_all_name_users(self):
        return self._users.keys()

    def get_all_users(self):
        return self._users

    def print_all_users(self):
        for key, val in self._users.items():
            print(f'Name: {key}')
            print(f'Login: {val[0]}')
            print(f'Password(hash): {val[1]}')
            print('________________\n')

    def get_password_user(self, user):
        return self._users[user][1]
