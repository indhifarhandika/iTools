#!/usr/bin/python
#Code by Indhifarhandika
#Apikasi iTools File Sharing
#Version 1.0 Alpha

import SimpleHTTPServer
import SocketServer
import os
from colored import fg,bg,attr

ip = lambda: os.system('ifconfig | grep broadcast') #Cek IP Address
cekfolder = lambda: os.system("pwd")
clear = lambda: os.system('clear') #"clear" untuk OS Linux | "cls" untuk OS Windows

def iTools():
	port = 99
	print "%s" % fg('white')
	clear()
	ip() #Cek IP Address
	host = raw_input('\n%sYour IP Address(inet) : ' % fg('white'))#Input Ip Address, jika tidak diisi maka akan menjalankan Ip secara Otomatis
	tampilan()
	hnd = SimpleHTTPServer.SimpleHTTPRequestHandler
	http1 = SocketServer.TCPServer((host,port),hnd)

	if host == '': #Untuk Ip Otomatis
		print '%s[+]Server Ip Default, Port :%s' % (fg('white'),port)
		print '[+]Direktory Sharing....'
		cekfolder()
		print '[+]Starting.....'
	else:
		print '%s[+]Server : %s:%s' % (fg('white'),host,str(port)) #Ip Setting Manual
		print '[+]Direktory Sharing....'
		cekfolder()
		print '[+]Starting.....'
	http1.serve_forever()#Start Server
def tampilan():
    clear() #Clear Console
    print """
    %s%s\t\t++++++++++++++++++++++++++++++++++++++++++++++++++
    \t\t+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-+
    \t\t+-------------=[%siTFileSharing Linux%s]_-_-_-_-_-_-_+
    \t\t+--=[%sVersi 1.6%s]-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+
    \t\t%s+----------------=[%sAuthor : indhifarhandika%s]-_-_-+
    \t\t+----=[%sEmail : indhi.farhandika@programmer.net%s]-_+
    \t\t+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-+
    \t\t++++++++++++++++++++++++++++++++++++++++++++++++++
    \t\t+------=[%s%shttps://indhifarhandika.github.io%s]%s\n\n""" % (attr('bold'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),attr('bold'),fg('red'),fg('white'),attr('reset'))
if __name__ == "__main__":
	iTools() #Main()
