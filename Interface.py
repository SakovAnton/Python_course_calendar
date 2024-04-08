"""
Позволяет зайти по логину-паролю или создать нового пользователя (а так же выйти из аккаунта)
Позволяет выбрать календарь, узнать ближайшие события, события из промежутка времени а так же
Создать событие или удалить событие
После создания события можно добавить туда пользователей
Если нас добавили в событие или удалили мы получаем уведомление.

в main можно использовать ТОЛЬКО interface
"""
import csv
import re

from Backend import Backend
from Calendar import Calendar
import datetime as dt


class Interface:
    state = 'start'
    func_request = list()
    _current_user = ''
    _current_cal = ''
    _current_calendars = list()

    @staticmethod
    def work():
        Interface.func_request = [Interface.start]

        while Interface.func_request:
            Interface.func_request[0]()
            del Interface.func_request[0]

        print('Интерфейс закончил работу!')

    @staticmethod
    def start():
        global back
        back = Backend()
        Interface.state = 'start'
        print('Запуск календаря')
        Interface.func_request.append(Interface.load_users)
        Interface.func_request.append(Interface.read)

    @staticmethod
    def exit():
        print('До новых встреч!')
        exit()

    @staticmethod
    def read():
        Interface.state = 'read'
        ret = input("""Главное меню:
                    1. Login user
                    2. Выход
                    3. Посмотреть список зарегистрированных пользователей
                    4. Создать пользователя
                    """)

        if ret.isdigit():
            ret = int(ret)
            if ret == 1:
                Interface.func_request.append(Interface.login_user())
            elif ret == 2:
                Interface.func_request.append(Interface.exit_main_menu())
            elif ret == 3:
                Interface.func_request.append(Interface.all_users())
            elif ret == 4:
                Interface.func_request.append(Interface.create_user())
            else:
                print('Попробуйте ещё раз ввести правильную цифру!')
                Interface.func_request.append(Interface.read())
        else:
            print('Вероятно вы ошиблись! \n (вводить нужно только цифру пункт меню)')
            Interface.func_request.append(Interface.read())

    @staticmethod
    def exit_main_menu():
        with open('registered_users.txt', 'w+', newline='') as f:
            date = dt.datetime.now()
            w = csv.DictWriter(f, fieldnames=['user', 'login', 'password_hash', 'date'])
            w.writeheader()
            for user in Backend.get_all_users(back).keys():
                data = dict()
                data['user'] = user
                data['login'] = Backend.get_all_users(back)[user][0]
                data['password_hash'] = Backend.get_all_users(back)[user][1]
                data['date'] = date
                w.writerow(data)
        Interface.func_request.append(Interface.exit())

    @staticmethod
    def load_users():
        with open('registered_users.txt', 'r') as f:
            w = csv.DictReader(f, fieldnames=['user', 'login', 'password_hash', 'date'])
            for i in w:
                if i['user'] == 'user':
                    continue

                user = i['user']
                login = i['login']
                password_hash = i['password_hash']

                back.create_user(user=user, login=login, password_hash=password_hash)

        Interface.func_request.append(Interface.read())

    @staticmethod
    def all_users():
        for k, user in enumerate(Backend.get_all_name_users(back)):
            print(f'Пользователь_{k + 1}: {user}')
        Interface.func_request.append(Interface.read())

    @staticmethod
    def create_event():

        pattern_date = r'^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
        t_s = '  '
        t_end = '  '
        users = []
        participants = []

        event = input('Введите название события: ')
        while re.match(pattern_date, t_s) == None:
            t_s = input('Введите время начала события (YY-MM-dd h:m:s): ')

        while re.match(pattern_date, t_end) == None:
            t_end = input('Введите время окончания события (YY-MM-dd h:m:s): ')

        print('Введите имена участников: ')
        for k, user in enumerate(Backend.get_all_name_users(back)):
            print(f'Пользователь_{k + 1}: {user}')
            users.append(user)

        while True:
            k = input('Введите номер зарегистрированного юзера:\n '
                      '(для выхода введите любой символ) ')
            if k.isalnum():
                if k.isalpha() or int(k) > len(users) or int(k) <= 0:
                    print(f'Добавляем следующих пользователей:\n{participants}\n')
                    break

                participant = users[int(k) - 1]
                print(f'Добавим участника: {participant}')
                participants.append(participant)

        while True:
            rep = input('''Выберите повторяющиеся событие\n 
                            1: Единичное событие
                            2: Каждый день
                            3: Каждую неделю
                            4: Каждый месяц''')
            if rep.isdigit():
                rep = int(rep)
                if rep == 1:
                    repeat = 'single'
                    break
                elif rep == 2:
                    repeat = 'week'
                    break
                elif rep == 3:
                    repeat = 'month'
                    break
                elif rep == 4:
                    repeat = 'year'
                    break
                else:
                    print('Попробуйте ещё раз ввести правильную цифру!')

        print('Событие создано.')
        Interface._current_cal.create_event(title=event, time_start=t_s, time_end=t_end, participants=participants,
                                            repeat=repeat)

        Interface.func_request.append(Interface.user_read())

    @staticmethod
    def print_user_events():
        # print(f'Текущий календарь: {Interface._current_cal}')

        events_all = Interface._current_cal.get_events_user(Interface._current_user)
        print(f'Текущий юзер: {Interface._current_user}')

        for event in events_all:
            print(event)

        Interface.func_request.append(Interface.user_read())

    @staticmethod
    def print_user_between_date_events():
        # print(f'Текущий календарь: {Interface._current_cal}')

        pattern_date = r'^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
        time_start = '  '
        time_end = '  '

        while re.match(pattern_date, time_start) == None:
            time_start = input('Введите время начала поиска событий (YY-MM-dd h:m:s): ')

        while re.match(pattern_date, time_end) == None:
            time_end = input('Введите время окончание поиска событий (YY-MM-dd h:m:s): ')

        events_all = Interface._current_cal.find_all_events_at_time(Interface._current_user, time_start, time_end)

        print(f'События для вас: {Interface._current_user} в период с {time_start} по {time_end}:')

        for event in events_all:
            print(event)

        Interface.func_request.append(Interface.user_read())

    @staticmethod
    def create_user():
        user = input('Введите ваше имя: ')
        login = input('Введите login: ')
        password = input('Введите пароль: ')
        back.create_user(user=user, login=login, password=password)
        # b.create_calendar(user)
        Interface.func_request.append(Interface.read())

    @staticmethod
    def login_user():
        print('LOGIN:\n')
        user = input('Введите ваше имя: ')
        # login = input('Введите login: ')
        password = input('Введите пароль: ')
        if user in Backend.get_all_name_users(back):
            if back.login_user(user, password):
                print(f'Здравствуйте {user}, рады вас приветствовать!')

                Interface._current_user = user

                Interface._current_cal = Calendar(Interface._current_user)

                try:
                    Interface._current_cal.read_from_json(f"Calendars\\{user}_calendar.json")
                except:
                    print('Вы давно не заходили и календарь забыл все ваши события')
                    # решение очень плохое, но времени писать проверку версии файла

                if Interface._current_cal not in Interface._current_calendars:
                    Interface._current_calendars.append(Interface._current_cal)

                Interface.func_request.append(Interface.user_read())

            else:
                print('Пароль не правильный попробуйте ввести его ещё раз!')
                Interface.func_request.append(Interface.login_user())
        else:
            print('Такого user не найдено, попробуйте ещё раз.')
            y = input('Нажмите "Y" если хотите увидеть всех зарегистрированных пользователей:')
            if y == 'y' or y == 'Y':
                Interface.func_request.append(Interface.all_users())

                Interface.func_request.append(Interface.login_user())
                # Interface.func_request.append(Interface.read())

            Interface.func_request.append(Interface.read())

    @staticmethod
    def user_read():
        ret = input(f"""{Interface._current_user}'s меню:
                               1. Создать событие
                               2. Удалить событие
                               3. Изменить событие
                               4. Показать все мои события
                               5. Показать мои события между двумя датами
                               6. Изменить пароль
                               7. Выход
                               """)

        if ret.isdigit():
            ret = int(ret)
            if ret == 1:
                Interface.func_request.append(Interface.create_event())
            elif ret == 2:
                Interface.func_request.append(Interface.exit_login())
            elif ret == 3:
                Interface.func_request.append(Interface.all_users())
            elif ret == 4:
                Interface.func_request.append(Interface.print_user_events())
            elif ret == 5:
                Interface.func_request.append(Interface.print_user_between_date_events())
            elif ret == 6:
                Interface.func_request.append(Interface.print_user_events())
            elif ret == 7:
                Interface.func_request.append(Interface.exit_login())
            else:
                print('Попробуйте ещё раз ввести правильную цифру!')
                Interface.func_request.append(Interface.read())
        else:
            print('Вероятно вы ошиблись! \n (вводить нужно только цифру пункт меню)')
            Interface.func_request.append(Interface.user_read())

    @staticmethod
    def exit_login():
        Interface._current_cal.save_to_json()
        print(f'До свидания {Interface._current_user} !')
        Interface.func_request.append(Interface.read())

    @staticmethod
    def finish():
        pass

    # Interface.start()


Interface.work()
