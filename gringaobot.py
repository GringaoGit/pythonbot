#!/usr/bin/env python2
# -*- coding: utf8 -*-

import irclib
import ircbot
import time

ircsrv = "irc.domain.fr"
port = 6667
nick = "nickname"
chan = "#Channel"
botpasswd = "password"

class Bot(ircbot.SingleServerIRCBot):
	def __init__(self):
		ircbot.SingleServerIRCBot.__init__(self, [(ircsrv, 6667)], nick, "Je suis un bot.")
	def on_welcome(self, serv, ev):
		serv.oper(nick, botpasswd)
		serv.join(chan)
		serv.privmsg(chan, "C'est moi que voilà !!!")
	def on_kick(self, serv, ev):
		serv.join(chan)
		serv.privmsg(chan, "He ! Tu te prends pour qui toi ?!")
	def on_pubmsg(self, serv, ev):
		message = ev.arguments()[0]
		if message.startswith("!help"):
			serv.privmsg(chan, "Commandes disponibles : biere, repeat, spam")
			return
		elif message.startswith("!biere"):
			serv.privmsg(chan, "et une biere pour "+nick +" !")
			return
		elif message.startswith("!repeat"):
			serv.privmsg(chan, message[8:100])
			return
		elif message.startswith("!spam"):
			num_str = message[6:8]
			try:
				num_int = int(num_str)
			except Exception, e:
				serv.privmsg(chan, "Mets un numéro !")
				print "not integer"
				return
			print type(num_int)
			for i in range(0, num_int):
				serv.privmsg(chan, "Voilà t'as du spam !")
				time.sleep(1)
			return
		elif message.startswith("!bye"):
			serv.privmsg(chan, "Ouai ouai, on me jette comme ça...")
			serv.quit(chan)
			return
if __name__ == "__main__":
    Bot().start()
