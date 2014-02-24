import tornado.ioloop
import tornado.web
import tornado.websocket

import json

from tornado import websocket
from tornado import ioloop

cl = []

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("template/index.html")

class SocketHandler(websocket.WebSocketHandler):

	def open(self):
		if self not in cl:
			cl.append(self)

	def on_close(self):
		if self in cl:
			cl.remove(self)

application = tornado.web.Application([
		(r"/", MainHandler),
		(r"/ws", SocketHandler),
		(r"/font/(.*)", tornado.web.StaticFileHandler, {"path": "lib/font/"}),
	])

def send(msg):
	data = json.dumps(msg)
	for c in cl:
		c.write_message(data)

def run():
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()