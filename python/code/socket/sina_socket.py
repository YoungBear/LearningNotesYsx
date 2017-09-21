#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

addr = 'www.sina.com.cn'
port = 80
s.connect((addr, port))

# 发送数据
data = b'GET / HTTP/1.1\r\vHost: www.sina.com.cn\r\nConnection: close\r\n\r\n'

s.send(data)

# 接收数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
recv_data = b''.join(buffer)

# 关闭连接
s.close()

header, html = recv_data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))

# 把接收到的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)
