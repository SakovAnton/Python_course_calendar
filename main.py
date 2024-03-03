from datetime import datetime as dt
from Event import Event
from Calendar import Calendar
from User import User
from Backend import Backend

if __name__ == "__main__":
    # event1 = Event(title='Event_1', time_start='2023-12-22 15:15:01', time_end='2023-12-22 19:15:01',
    #                participants={'Vasya', 'Petr', 'Nik'}, repeat='day')
    # event2 = Event(title='Event_2', time_start='2023-12-23 15:16:01', time_end='2023-12-22 19:15:01',
    #                participants={'Vasya', 'Petr', 'Nik'}, repeat='week')
    # event3 = Event(title='Event_3', time_start='2023-12-24 15:17:01', time_end='2023-12-24 19:15:01',
    #                participants={'Vasya', 'Petr', 'Nik'}, repeat='single')
    #
    # event4 = event3.copy_event_dif_time(time='2023-12-25 15:18:01')
    #
    # print(type(event4.get_time_start()))
    #
    # cal_Anton = Calendar('Anton')
    # cal_Anton.add_events(event1, event2, event3, event4)
    #
    # print(f'cal_Anton: {cal_Anton.get_events()}')
    #
    # cal_test2 = Calendar('G')
    # cal_test2 = cal_Anton.find_all_events_at_time('2023-12-22 15:15:01', '2023-12-25 15:18:01')
    #
    # # print(event3)
    # print(f'EVENT 4: {event4}')
    #
    # print(f'Found events: \n {cal_test2}')
    # print(f'Calendar(Anton): {cal_Anton}')
    #
    # # cal_Anton.del_events(event1)
    #
    # # print(type(dt.now().strftime('%d_%m_%Y')))
    #
    # cal_Anton.save_to_json()
    #
    # cal_test = Calendar('Gosha')
    # cal_test.read_from_json("Anton's events at 2024-01-21.json")
    # cal_test.save_to_json()
    #
    B1 = Backend()
    #
    # Anton = User('Anton', 'remelle', 'qwerty')
    # print(Anton)
    # # print(Anton.get_password())
    #
    # # print(f'Users: {User.get_all_users()}')
    #
    # Ant2 = User('Anton', 'remelle', 'qwerty')

    # print(f'Попытка создать юзера с повторяющимся именем: {Ant2}')

    B1.create_user('Anton2', 'remelle', 'qwerty')
    B1.create_user('Anton', 'remelle', 'qwerty')
    B1.create_user('Anton', 'remelle', 'qwerty')
    B1.create_user('Anton', 'rem', 'qwerty')

    print(f'All_users: {Backend.get_all_name_users(B1)}\n')
    Backend.print_all_users(B1)

    C = Calendar('Anton3')
    C.create_event(title='Event_1_A', time_start='2023-12-22 15:15:01', time_end='2023-12-22 19:15:01',
                   participants={'Vasya', 'Petr', 'Nik'}, repeat='day')
    C.create_event(title='Event_2_A', time_start='2023-12-23 15:16:01', time_end='2023-12-22 19:15:01',
                   participants={'Vasya', 'Petr', 'Nik'}, repeat='week')
    C.create_event(title='Event_3_A', time_start='2023-12-24 15:17:01', time_end='2023-12-24 19:15:01',
                   participants={'Vasya', 'Petr', 'Nik'}, repeat='single')

    # C1 = B1.create_calendar('Anton33')
    C1 = Calendar('Anton33')
    C1.create_event(title='Event_1_A_33', time_start='2023-12-22 15:15:01', time_end='2023-12-22 19:15:01',
                    participants={'Vasya', 'Petr', 'Nik'}, repeat='day')
    C1.create_event(title='Event_2_A_33', time_start='2023-12-23 15:16:01', time_end='2023-12-22 19:15:01',
                    participants={'Vasya', 'Petr', 'Nik'}, repeat='week')
    C1.create_event(title='Event_3_A_33', time_start='2023-12-24 15:17:01', time_end='2023-12-24 19:15:01',
                    participants={'Vasya', 'Petr', 'Nik'}, repeat='single')

    # print(f'Календарь C:\n {C.get_events_v2()}')
    # print(f'Календарь C1:\n {C1.get_events_v2()}')

    print(f'Календарь C:(Anton3)\n {C.get_events()}')
    print(f'Календарь C1 (Anton33):\n {C1.get_events()}')

    print(f'длинна С: {len(C.get_events())}')
    print(f'длинна С1: {len(C1.get_events())}')

    print(C.get_owner())
    print(C.get_events_user(C.get_owner()))

    C.save_to_json()
    # cal_test.read_from_json("Anton's events at 2024-01-28.json")
    CC = C1.find_all_events_at_time('2023-12-22 15:15:01', '2023-12-25 15:18:01')

    print(f"Found Events: \n{CC}")

    for i in range(len(CC)):
        print(f'{CC[i]}\n')
        print(f'{CC[i].get_id()}\n')

    # print(f'CC: {CC[0]}')

    print(type(C._events))
    print(type(C._events_user))
    print(type(C._events[0]))

    print(B1.get_password_user('Anton2'))

    print(B1.login_user('Anton2', 'qwerty'))
    print(B1.login_user('Anton2', 'qwerty2'))

    event_id = CC[1].get_id()
    print(event_id)
    print(C.get_event_id(event_id))
    print(type(C))
    print(type(C.get_event_id(event_id)))

    print(len(C.get_event_id(event_id)))
    print(C.get_event_id(event_id)[0])

    print(type(C.get_event_id(event_id)[0]))

    C.change_event(iid=event_id, new_title='EventTTTTT_3_A_33',
                   new_time_start='2023-12-24 15:17:01', new_time_end='2029-12-24 19:15:01',
                   new_participants={'Vasya', 'Petr', 'Nik', 'Nik2', 'Nik3', 'Nik4'}, new_repeat='single')

    print(C.get_event_id(event_id))
    C.delete_event_id(event_id)
    print(C.get_event_id(event_id))

    print(f'Users(B1): {B1.get_all_users().keys()}')

    for i in B1.get_all_users().keys():
        print(f'User: {i}')
        print(f'login: {B1.get_all_users()[i][0]}')
        print(f'password: {B1.get_all_users()[i][1]}\n')

    # print(f'Календарь C:\n {C.get_events()}')

# print(type(Calendar._events_user[0]))

# print(f'Календарь cal_test2: {cal_test2.get_events()}')
# print(f'Календарь cal_Anton:\n {cal_Anton.get_events_v2()}')

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
