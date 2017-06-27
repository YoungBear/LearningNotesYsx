#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def by_grade(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)] 

L2 = sorted(L, key = by_grade, reverse = True)
print(L2)
