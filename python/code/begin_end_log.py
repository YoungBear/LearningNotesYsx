#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def log(func):
    def wrapper(*args, **kw):
        print('begin call %s(): ' % func.__name__)
        func(*args, **kw)
        print('end call %s(): ' %func.__name__)
    return wrapper

@log
def now():
    print('2015-3-25')

now()
