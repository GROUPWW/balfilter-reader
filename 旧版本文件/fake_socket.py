#!/usr/bin/env python
# -*- coding=utf-8 -*-
import socket
import sys
import os
import struct
import cv2
import time
import json

def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]

def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]

def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('162.105.183.67', 23456))#这里换上自己的ip和端口
        s.listen(10) # 监听，这里表示最多有10个客户端连接服务器
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print ("Waiting...")

    # 放上面不断连接就行，完美
    conn, addr = s.accept()
    while True:
        recv_filepath = conn.recv(1024) #看来recv确实是在等待！！棒
        filepath = recv_filepath.decode()
        print('服务端收到了客户端发来的请求，想获取:',filepath)

        if filepath=='get_case_pic_list':
            print('hello')
            fsize = str(len(str(['0.5-32x27','0.7-65x63','0.7-81x54']))).encode('utf-8')
            # fsize = '3'.encode('utf-8')
            conn.send(fsize)
            enc = (str(['0.5-32x27','0.7-65x63','0.7-81x54'])+'_'*1024).encode(encoding='utf-8')
            while enc:
                sd,enc = enc[:1024],enc[1024:]
                conn.send(sd)


        elif os.path.isfile(filepath):
            print('服务端在数据库找到了:', filepath)
            img = cv2.imread(filepath)
            shape_str = str(img.shape[0])+'_'+str(img.shape[1])+'_'+str(img.shape[2])


            # 预先发送下图片的大小，方便客户端接收完整图片
            fsize = shape_str.encode('utf-8')
            conn.send(fsize)
            print('服务端向客户端发送了图片的大小:',fsize)

            send_from(img, conn)



socket_service()