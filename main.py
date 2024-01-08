from datetime import datetime as dt
from Event import Event
from Calendar import Calendar

if __name__ == "__main__":

    event1 = Event(title='Event_1', time_start='2023-12-22 15:15:01', time_end='2023-12-22 19:15:01',
                   participants={'Vasya', 'Petr', 'Nik'}, repeat='week')
    event2 = Event(title='Event_2', time_start='2023-12-23 15:15:01', time_end='2023-12-22 19:15:01',
                   participants={'Vasya', 'Petr', 'Nik'}, repeat='week')
    event3 = Event(title='Event_3', time_start='2023-12-24 15:15:01', time_end='2023-12-22 19:15:01',
                   participants={'Vasya', 'Petr', 'Nik'}, repeat='week')

    #    print(event1)

    cal_Anton = Calendar('Anton')
    cal_Anton.add_events(event1, event2, event3)

    #cal_test2 = Calendar('G')
    cal_test2 = cal_Anton.find_all_events_at_time('2023-12-22 15:15:01', '2023-12-24 15:15:01')

    print(f'Found events: {cal_test2}')
    print(f'Calendar(Anton): {cal_Anton}')

    #cal_Anton.del_events(event1)


    # print(type(dt.now().strftime('%d_%m_%Y')))

    cal_Anton.save_to_json()


    cal_test = Calendar('Gosha')
    #cal_test.read_from_json("Anton's events at 2024-01-08.json")
    #cal_test.save_to_json()


    # print(cal_test)

    # print(event1.get_time_start())
    # print(type(event1.get_time_start()))
    #
    # for event in cal_test2.get_events():
    #     print(event.get_title())
    #     print(event.get_id())
    #     # print(event.get_time_start().strftime('%d_%m_%Y'))
    #     # print(event.get_time_end().strftime('%d_%m_%Y'))
    #     print(event.get_time_start())
    #     print(event.get_time_end())
    #     print(event.get_organizer())
    #     print(event.get_participants())
    #     print(event.get_description())
    #     print("_________________________________________________")
