"""
Описывает некоторе "событие" - промежуток времени с присвоенными характеристиками
У события должно быть описание, название и список участников
Событие может быть единожды созданым
Или периодическим (каждый день/месяц/год/неделю)

# Каждый пользователь ивента имеет свою "роль"
# организатор умеет изменять названия, список участников, описание, а так же может удалить событие
# участник может покинуть событие

запрос на хранение в json
Уметь создавать из json и записывать в него

Иметь покрытие тестами
Комментарии на нетривиальных методах и в целом документация
"""

# Push TEST

import datetime as dt
import json
import uuid


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

    def __init__(self, iid=None, title='', time_start=None, time_end=None,
                 description=None, participants=set(), organizer='', repeat='single'):

        self._id = iid

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
        return f'Название события: {self._title}\n' \
               f'Время начала: {self._time_start}\n' \
               f'Время окончания: {self._time_end}\n' \
               f'Повторяемость: {self._repeat}\n' \
               f'Организатор: {self._organizer}\n' \
               f'Участники: {self._participants}\n' \
               f'ID: {self.get_id()}\n'

    def __repr__(self):
        return f'ID: {self.get_id()}||Организатор: {self._organizer}||Название: {self._title}||время начала: {self.get_time_start()}\n'

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_id(self):
        return self._id

    def get_time_start(self):
        return self._time_start

    def set_time_start(self, time_start):
        self._time_start = time_start

    def get_time_end(self):
        return self._time_end

    def set_time_end(self, time_end):
        self._time_start = time_end

    def get_organizer(self):
        return self._organizer

    def get_participants(self):
        return self._participants

    def set_participants(self, participants):
        self._participants = participants

    def get_description(self):
        return self._description

    def get_repeat(self):
        return self._repeat

    def set_repeat(self, repeat):
        self._repeat = repeat

    def copy_event_dif_time(self, time):

        time_end = dt.datetime.strptime(time, '%Y-%m-%d %H:%M:%S') + (
                dt.datetime.strptime(self.get_time_end(), '%Y-%m-%d %H:%M:%S') - dt.datetime.strptime(
            self.get_time_start(), '%Y-%m-%d %H:%M:%S'))

        return Event(iid=self.get_id(), title=self.get_title(), time_start=time,
                     time_end=time_end.strftime('%Y-%m-%d %H:%M:%S'),
                     description=self.get_description(), participants=self.get_participants(),
                     organizer=self.get_organizer(), repeat=self.get_repeat())
