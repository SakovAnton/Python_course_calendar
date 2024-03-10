import datetime as dt

#dt.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

t1 = dt.datetime.now().date()
t2 = dt.datetime.now().date()-dt.timedelta(days=1)
print(t1)
print(t2)

print(t1 > t2)