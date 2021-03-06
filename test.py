#!/usr/bin/python
# -*- coding: utf-8 -*-
# from bluetooth import *
# import bluetooth
# import serial
# import time

# import asyncio
# import datetime
# import random
# import websockets

# async def time(websocket, path):
#     while True:
#         print("start")
##        port = "/dev/tty.HC-05-SPPDev"
#  #       bluetooth = serial.Serial(port, 9600)
#   #      print("Connected")
#    #     data = bluetooth.readline().decode()
#     #    await websocket.send(data)

# start_server = websockets.serve(time, "127.0.0.1", 5679)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()

from bluetooth import *
import time
import tornado.web
import tornado.ioloop
import tornado.websocket
import tornado.httpserver
from tornado.ioloop import PeriodicCallback
from tornado.concurrent import Future
from tornado import gen
port = 1
bd_addr = '00:19:08:35:F1:7F'
sock = BluetoothSocket(RFCOMM)
sock.connect((bd_addr, port))


class WSHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def initialize(self):
        print("connncted 1")

    def open(self):
        print("connncted 2")

    def send_hello(self):
        self.write_message('hello')

    def on_message(self, message):
        print(message)
        if message == 'start':
            self.send_temp()

        else:
            sock.close()

    def send_temp(self):

        # print('waiting')

        while True:
            data = sock.recv(10)
            print(data.decode())
            self.write_message(data.decode())

    def on_close(self):
        self.close_future.set_result(None)


application = tornado.web.Application([(r'/', WSHandler)])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
