#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# server端监听端口
# server_addr = '127.0.0.1'
server_addr = '47.95.249.79'
server_port = 9999
s.connect((server_addr, server_port))
# 接收欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送消息
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
