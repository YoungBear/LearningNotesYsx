#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def move(n, a, b,c):
    if n > 1:
        move(n-1, a, c, b)
        print("# " + a + " --> " + c)
        move(n-1, b, a, c)
    else:
        print("# " + a + " --> " + c)
    #print("move...")
    pass

move(3, 'A', 'B', 'C')
