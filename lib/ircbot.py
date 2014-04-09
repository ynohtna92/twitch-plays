import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
from misc import pp
import Queue

class Irc(irc.bot.SingleServerIRCBot):
    def __init__(self, config, queue, channel, nickname, server, port=6667, password=None):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, password)], nickname, nickname)
        self.channel = channel
        self.queue = queue
        self.config = config

    @classmethod
    def from_config(cls, config, queue):

        server = config['irc']['server']
        port = config['irc']['port']
        channel = config['irc']['channel']

        nickname = config['account']['username']
        password = config['account']['password']

        return cls(config, queue, channel, nickname, server, port, password)
        
    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        pp("Joining channel " + self.channel)
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        self.do_command(e, e.arguments[0])
        #a = e.arguments[0].split(":", 1)
        #if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
        #    self.do_command(e, a[1].strip())
        #return

    def on_dccmsg(self, c, e):
        c.privmsg("You said: " + e.arguments[0])

    def on_dccchat(self, c, e):
        if len(e.arguments) != 2:
            return
        args = e.arguments[1].split()
        if len(args) == 4:
            try:
                address = ip_numstr_to_quad(args[2])
                port = int(args[3])
            except ValueError:
                return
            self.dcc_connect(address, port)

    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection
        cm = cmd.lower()
        if cm in self.config["commands"]:
            self.queue.put({"user":nick, "msg":cm})
