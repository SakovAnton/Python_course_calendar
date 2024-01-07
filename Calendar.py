"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""

from Event import Event
from datetime import datetime as dt
import json


class Calendar:
    _events = []

    def get_events(self):
        return self._events

    def __init__(self, owner):
        self._owner = owner

    def add_event(self, *events):
        for event in events:
            if isinstance(event, Event) or issubclass(type(event), Event):
                self._events.append(event)

    def save_to_json(self):

        to_json = {
            'date': dt.now().strftime('%d,%m,%Y'),
            'EVENT': [
                {
                    'Title:': event.get_title(),
                    'id:': event.get_id(),
                    'Repeat:': event.get_repeat(),
                    'Time_start:': event.get_time_start().strftime('%d_%m_%Y'),
                    'Time_end:': event.get_time_end().strftime('%d_%m_%Y'),
                    'Organizer:': event.get_organizer(),
                    'Participants': [participant for participant in event.get_participants()],
                    'Description': event.get_description()

                } for event in self.get_events()
            ]
        }

        print(to_json)
        with open(f'Events {dt.now().date()}.json', 'w') as f:
            f.write(json.dumps(to_json))
