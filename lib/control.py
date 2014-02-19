from ircd import Irc
import time 
import threading
import Queue

exitFlag = 0

class Control(threading.Thread):

	def __init__(self, threadID, name, config, queue):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.config = config
		self.queue = queue
	
	def run(self):
		self.irc = Irc.from_config(self.config, self.queue).start()