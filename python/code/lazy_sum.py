#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def lazy_sum(*args):
   def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
   return sum

f = lazy_sum(1,3,5,7,9)

f

print(f())
