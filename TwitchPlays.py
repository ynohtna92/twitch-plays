#!/usr/bin/env python
# coding: utf8

# Twitch Plays Pokemon
# Clone of twitch.tv/twitchplayspokemon
# Initially written by Aidan Thomson <aidraj0 at gmail dot com>
# Forked by ynohtna92

import logging
import sys
from config.config import *
import lib.bot as bot

def main():
    try:
        global bot
        #logging.basicConfig(level=logging.DEBUG) #debug
        bot = bot.Bot(config).run()
    except KeyboardInterrupt:
        print ""
        print "Shutting Down...."
        print "Thank you for using twitch-plays."
        print "Support this project at https://github.com/ynohtna92/twitch-plays"
        exit()

if __name__ == '__main__':
    main()
