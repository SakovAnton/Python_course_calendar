"""
Класс календаря - хранит события.
он умеет искать все события из промежутка (в том числе повторяющиеся)
он умеет добавлять/удалять события.
У каждого календаря ровно один пользователь.
"""

from Event import Event
import datetime as dt
import json
import uuid


class Calendar:
    _events_user = dict()

    def __init__(self, owner):
        self._owner = owner
        self._events = []

    def create_event(self, title='', time_start=None, time_end=None, description=None,
                     participants=None, organizer=None, repeat='single'):

        organizer = self.get_owner()

        _id = str(uuid.uuid4())

        if time_start:

            event = Event(iid=_id, title=title, time_start=time_start, time_end=time_end, description=description,
                          participants=participants, organizer=organizer, repeat=repeat)

            self._events_user[_id] = [event]

            self.add_events(event)
        else:
            print('Не хватает данных для создания события!')

    def get_event_id(self, iid):
        event = self._events_user[iid]
        return event

    def change_event(self, iid, new_title=None, new_time_start=None, new_time_end=None, new_description=None,
                     new_participants=None, new_repeat=None):

        event = self._events_user[iid][0]

        if new_title:
            event.set_title(new_title)
        if new_time_start:
            event.set_time_start(new_time_start)
        if new_time_end:
            event.set_time_end(new_time_end)
        if new_description:
            event.set_description(new_description)
        if new_participants:
            event.set_participants(new_participants)
        if new_repeat:
            event.set_repeat(new_repeat)

    def delete_event_id(self, iid):
        del (self._events_user[iid][0])

    def get_events(self):
        return self._events

    def get_events_user(self, owner):
        found_events = []
        for event in self.get_events():
            if event.get_organizer() == owner:
                found_events.append(event)

        return found_events

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

    def find_all_events_at_time(self, owner, time_start, time_end):

        found_events = []
        t_start = dt.datetime.strptime(time_start, '%Y-%m-%d %H:%M:%S')
        t_end = dt.datetime.strptime(time_end, '%Y-%m-%d %H:%M:%S')

        delta_time = dt.timedelta(microseconds=0)

        for event in self.get_events_user(owner):

            if event.get_repeat() == 'day':
                delta_time = dt.timedelta(days=1)
            if event.get_repeat() == 'week':
                delta_time = dt.timedelta(weeks=1)
            if event.get_repeat() == 'month':
                delta_time = dt.timedelta(weeks=1)
            if event.get_repeat() == 'year':
                delta_time = dt.timedelta(weeks=1) * 52
            if event.get_repeat() == 'single':
                delta_time = dt.timedelta(days=36500)
            i = 0
            while (t_start + i * delta_time) <= t_end:
                time_2 = dt.datetime.strptime(event.get_time_start(), '%Y-%m-%d %H:%M:%S') + i * delta_time
                if t_start <= time_2 <= t_end:
                    found_events.append(event.copy_event_dif_time(time=time_2.strftime('%Y-%m-%d %H:%M:%S')))
                i = i + 1
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

                } for event in self.get_events_user(self.get_owner())
            ]
        }

        print(to_json)
        with open(f"Calendars\\{self._owner}_calendar.json", 'w') as f:
            f.write(json.dumps(to_json))
        # with open(f"Calendars\\{self._owner}_{dt.datetime.now().date()}.json", 'w') as f:
        #     f.write(json.dumps(to_json))

    # @staticmethod
    def read_from_json(self, file):

        try:
            with open(file, 'r') as f:
                json_string = json.loads(f.read())

            for event in json_string['EVENT']:
                # self.change_event(iid,
                #                   new_title=event['Title'],
                #                   new_time_start=event['Time_start'],
                #                   new_time_end=event['Time_end'],
                #                   new_description=event['Description'],
                #                   new_participants=event['Participants'],
                #                   new_repeat=event['Repeat']
                #                   )

                self._id = event['id']
                self.create_event(title=event['Title'],
                                  time_start=event['Time_start'],
                                  time_end=event['Time_end'],
                                  description=event['Description'],
                                  organizer=event['Organizer'],
                                  repeat=event['Repeat'],
                                  participants=event['Participants']
                                  )
        except:
            print('Пока мероприятий нет у вас, создайте первое мероприятие.')
