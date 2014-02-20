from ircbot import Irc
from game import Game
from misc import pp, pbot, pbutton
from control import Control

import time
import threading
import Queue

import operator

import web as web

exitFlag = 0

class Bot:

    def __init__(self, config):
        self.config = config
        self.game = Game()
        self.queue = Queue.Queue(0)
        pp("Initiating Irc Thread")
        self.c1 = Control(1, "Controller-1", self.config, self.queue, Irc.from_config(self.config, self.queue).start)
        self.c1.daemon = True
        self.c1.start()
        pp("Initiating Tornado Thread")
        self.c2 = Control(2, "Controller-2", self.config, self.queue, web.run)
        self.c2.daemon = True
        self.c2.start()

    def to_web(self, msg):
        web.send(msg)

    def run(self):
        try:
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
                    print(pbutton(user, button))
                    self.to_web({"button": {"user":user, "button":button, "formated": pbutton(user, button)}})
                    if self.config['start_throttle']['enabled'] and button == 'start':   
                        if time.time() - last_start < self.config['start_throttle']['time']:
                            continue
                        last_start = time.time()
                    if self.config["polling"]["enabled"]:
                        poll[button] += 1
                    else:
                        self.game.push_button(button)
        except KeyboardInterrupt:
            print ""
            print "Shutting Down...."
            print "Thank you for using twitch-plays."
            print "Support this project at https://github.com/ynohtna92/twitch-plays"
            exit()
