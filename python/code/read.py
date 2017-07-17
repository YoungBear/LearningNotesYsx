#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

try:
    f = open('C:\\Users\\ysx\\github\\LearningNotesYsx\\python\\code\\test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

try:
    f = open('C:\\Users\\ysx\\github\\LearningNotesYsx\\python\\code\\test_1.txt', 'r', encoding='gbk')
    print(f.read())
finally:
    if f:
        f.close()

try:
    f = open('C:\\Users\\ysx\\github\\LearningNotesYsx\\python\\code\\test_2.txt', 'w')
    f.write('Hello, world!')
finally:
    if f:
        f.close()
