"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""

from Event import Event
import datetime as dt
import json
import os


class Calendar:
    _instance = None
    _events = []
    _owner = ''

    # def __new__(cls, *args, **kwargs):
    #     if cls._instance is None:
    #         cls._instance = super().__new__(cls)
    #     return cls._instance

    def __init__(self, owner):
        self._owner = owner

    def get_events(self):
        return self._events

    def get_owner(self):
        return self._owner

    def add_events(self, *events):
        for event in events:
            if isinstance(event, Event) or issubclass(type(event), Event):
                self._events.append(event)

    def del_events(self, *events):
        for event in events:
            if isinstance(event, Event) or issubclass(type(event), Event):
                self._events.remove(event)

    def find_all_events_at_time(self, time_start, time_end):

        found_events = []
        t_start = dt.datetime.strptime(time_start, '%Y-%m-%d %H:%M:%S')
        t_end = dt.datetime.strptime(time_end, '%Y-%m-%d %H:%M:%S')

        i = 0
        delta_time = dt.timedelta(microseconds=1)

        for event in self.get_events():
            if event.get_repeat() == 'day':
                delta_time = dt.timedelta(days=1)
            if event.get_repeat() == 'week':
                delta_time = dt.timedelta(weeks=1)
            if event.get_repeat() == 'single':
                delta_time = dt.timedelta(microseconds=1)
            print(f'Заходы в цикл self.get_events() {event}')
            # time = t_start - dt.timedelta(days=1)
            # t_start = t_start - dt.timedelta(days=1)
            while (t_start - dt.timedelta(days=1) + i * delta_time) < t_end:
                # time = t_start - dt.timedelta(days=1) + i*delta_time
                i = i + 1
                print(i)

                time_2 = dt.datetime.strptime(event.get_time_start(), '%Y-%m-%d %H:%M:%S')
                print(f"time_2: {time_2}\n")

                if t_start <= time_2 <= t_end:
                    # event = event.copy_event_dif_time(time=event.get_time_start())

                    print(f'Заходим в if по времени: {t_start - dt.timedelta(days=1) + i * delta_time}\n')
                    print(f't_start: {t_start}\n')
                    print(f't_end: {t_end}\n')
                    time_2 = dt.datetime.strptime(event.get_time_start(), '%Y-%m-%d %H:%M:%S')

                    print(f"dt.datetime.strptime(event.get_time_start(): {time_2}\n")
                    found_events.append(event.copy_event_dif_time(time=event.get_time_start()))

                    # for time in range(int(t_start-dt.timedelta(days=1)), int(t_end+dt.timedelta(days=1)), int(delta_time)):
                    #     if t_start <= time <= t_end:
                    #        found_events.append(event)

        return found_events

    def save_to_json(self):

        to_json = {
            'DATE': dt.datetime.now().strftime('%d_%m_%Y'),
            'OWNER': self.get_owner(),
            'EVENT': [
                {
                    'Title': event.get_title(),
                    'id': event.get_id(),
                    'Repeat': event.get_repeat(),
                    'Time_start': event.get_time_start(),
                    'Time_end': event.get_time_end(),
                    'Organizer': event.get_organizer(),
                    'Participants': [participant for participant in event.get_participants()],
                    'Description': event.get_description()

                } for event in self.get_events()
            ]
        }

        print(to_json)
        with open(f"{self._owner}'s events at {dt.datetime.now().date()}.json", 'w') as f:
            f.write(json.dumps(to_json))

    @staticmethod
    def read_from_json(file):

        with open(file, 'r') as f:
            json_string = json.loads(f.read())
        cal = Calendar(json_string['DATE'])
        for event in json_string['EVENT']:
            cal.add_events(Event(title=event['Title'],
                                 time_start=event['Time_start'],
                                 time_end=event['Time_end'],
                                 description=event['Description'],
                                 organizer=event['Organizer'],
                                 repeat=event['Repeat'],
                                 # participants=event[part for part in json_string['Participants']]
                                 ))
