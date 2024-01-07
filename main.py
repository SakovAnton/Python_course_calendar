from datetime import datetime as dt
from Event import Event
from Calendar import Calendar

if __name__ == "__main__":

    event1 = Event(title='Event_1', participants={'Vasya', 'Petr', 'Nik'})
    event2 = Event(title='Event_2', participants={'Vasya', 'Petr', 'Nik'})
    event3 = Event(title='Event_3', participants={'Vasya', 'Petr', 'Nik'})

#    print(event1)

    cal1 = Calendar('Anton')
    cal1.add_event(event1, event2, event3)

    print(type(dt.now().strftime('%d_%m_%Y')))

    cal1.save_to_json()

    # for event in cal1.get_events():
    #     print(event.get_title())
    #     print(event.get_id())
    #     print(event.get_time_start().strftime('%d_%m_%Y'))
    #     print(event.get_time_end().strftime('%d_%m_%Y'))
    #     print(event.get_organizer())
    #     print(event.get_participants())
    #     print(event.get_description())
    #     print("_________________________________________________")







