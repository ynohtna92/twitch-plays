from ircbot import Irc
import time 
import threading
import Queue

exitFlag = 0

class Control(threading.Thread):

	def __init__(self, threadID, name, config, queue, func):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.config = config
		self.queue = queue
		self.func = func
	
	def run(self):
		self.func()
