#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for d in L1:
    if isinstance(d, str):
        L2.append(d.lower())

print(L2)
