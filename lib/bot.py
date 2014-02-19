from ircd import Irc
from game import Game
from misc import pp, pbot, pbutton
from control import Control

import time
import threading
import Queue

import operator

exitFlag = 0

class Bot:

    def __init__(self, config):
        self.config = config
        self.game = Game()
        self.queue = Queue.Queue(0)
        pp("Initiating Irc Thread")
        self.control = Control(1, "Controller-1", config, self.queue)
        self.control.start()

    def run(self):
        pp("Starting Monitoring Loop")
        last_start = time.time()
        if self.config["polling"]["enabled"]:
            polling = time.time()
            tick = self.config["polling"]["time"]
            poll = {"a":0, "b":0, "up":0, "down":0, "left":0, "right":0, "start":0, "select":0}
        while not exitFlag:
            if self.config["polling"]["enabled"] and time.time() > (polling + tick):
                polling = time.time()
                turn = max(poll.iteritems(), key=operator.itemgetter(1))[0]
                if poll[turn] != 0:
                    self.game.push_button(turn)
                    print turn
                poll = dict.fromkeys(poll, 0)

            if not self.queue.empty():
                job = self.queue.get()
                button = job["msg"]
                user = job["user"].capitalize()
                pbutton(user, button)
                if self.config['start_throttle']['enabled'] and button == 'start':   
                    if time.time() - last_start < self.config['start_throttle']['time']:
                        continue
                    last_start = time.time()
                if self.config["polling"]["enabled"]:
                    poll[button] += 1
                else:
                    self.game.push_button(button)