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
# #        port = "/dev/tty.HC-05-SPPDev"
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


class WSHandler(tornado.websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        self.callback = self.send_temp()
        self.callback.start()

    def send_hello(self):
        self.write_message('hello')

    def on_message(self, message):
        pass

    def send_temp(self):
        self.port = 1
        self.bd_addr = '00:19:08:35:F1:7F'
        self.sock = BluetoothSocket(RFCOMM)
        self.sock.connect((bd_addr, port))

    	# print('waiting')

        while True:
			self.data = self.sock.recv(10)
			print(self.data.decode())
            self.write_message(self.data.decode())
			
        sock.close()

    def on_close(self):
        self.callback.stop()
        print("Closed Connection")


application = tornado.web.Application([(r'/', WSHandler), ])

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
