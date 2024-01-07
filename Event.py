"""
Описывает некоторе "событие" - промежуток времени с присвоенными характеристиками
У события должно быть описание, название и список участников
Событие может быть единожды созданым
Или периодическим (каждый день/месяц/год/неделю)

Каждый пользователь ивента имеет свою "роль"
организатор умеет изменять названия, список участников, описание, а так же может удалить событие
участник может покинуть событие

запрос на хранение в json
Уметь создавать из json и записывать в него

Иметь покрытие тестами
Комментарии на нетривиальных методах и в целом документация
"""

# Push TEST

import datetime as dt
import json


class Event:
    _id = 0
    _title = ''
    __id_counter__ = 0
    # _time_start = dt.datetime()
    # _time_end = dt.datetime()
    _description = None
    _participants = set()
    _organizer = ''

    # _repeat = {'single': 1, 'every_day': 0, 'every_week': 0, 'every_month': 0}

    def __init__(self, title='Заглушка 1', time_start=dt.datetime(1, 1, 1), time_end=dt.datetime(1, 1, 1),
                 description='NONE', participants=set(), organizer='Nikola Tesla', repeat='single'):
        self._id = self.__class__.__id_counter__
        self.__class__.__id_counter__ += 1

        self._repeat = repeat

        if title:
            self._title = title
        if time_start:
            self._time_start = time_start
        if time_end:
            self._time_end = time_end
        if description:
            self._description = description
        if participants:
            self._participants = participants
        if organizer:
            self._organizer = organizer

    def __str__(self):
        return f'Название: {self._title}\n' \
               f'Время начала: {self._time_start}\n' \
               f'Время окончания: {self._time_end}\n' \
               f'Организатор: {self._organizer}\n' \
               f'Участники: {self._participants}'
    def __repr__(self):
        return f'Название: {self._title}\n'

    def get_title(self):
        return self._title

    def get_id(self):
        return self._id

    def get_time_start(self):
        return self._time_start

    def get_time_end(self):
        return self._time_end

    def get_organizer(self):
        return self._organizer

    def get_participants(self):
        return self._participants

    def get_description(self):
        return self._description

    def get_repeat(self):
        return self._repeat



