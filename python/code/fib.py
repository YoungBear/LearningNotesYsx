#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while(n < max):
        yield (b)
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(10):
    print(n)
#print(fib(6))


