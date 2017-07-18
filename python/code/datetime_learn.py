#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone
now = datetime.now()
print(now)

print(type(now))

dt = datetime(2015, 4, 19, 10, 20)
print(dt)


print(dt.timestamp())

t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

# str to datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime to str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))
print(now)
print(now + timedelta(hours = 10))
print(now - timedelta(days = 1))
print(now + timedelta(days = 2, hours = 12))

tz_utc_8 = timezone(timedelta(hours = 8))
dt = now.replace(tzinfo = tz_utc_8)
print(now)
print(dt)