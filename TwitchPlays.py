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
    global bot
    #logging.basicConfig(level=logging.DEBUG)
    bot = bot.Bot(config).run()

if __name__ == '__main__':
    main()