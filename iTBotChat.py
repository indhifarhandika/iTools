import sys
import time
import socket

server = "irc.freenode.net"
bnick = "iToolsBot"
channel = "#iTools"

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server,6667))
irc.setblocking(False)
time.sleep(1)
irc.send("USER "+bnick+" "+bnick+" "+bnick+" "+"\r\n")
time.sleep(1)
irc.send("NICK "+bnick+"\n")
time.sleep(1)
irc.send("JOIN "+channel+"\n")

while 1:
	try:
		text = irc.recv(2040)
		print(text)
	except Exception:
		pass
	if text.find("PING") != -1:
		irc.send("PONG"+ text.split()[1]+"\r\n")
	if text.lower().find(":@hi") != -1:
		irc.send("PRIVMSG "+channel+" :Hello!\r\n")
input()
