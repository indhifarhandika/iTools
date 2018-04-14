#!/usr/bin/python
#Code by Indhifarhandika
#Apikasi iTools File Sharing
#Version 1.0 Alpha

import http.server
import socketserver
import os

ip = lambda: os.system('ifconfig | grep broadcast') #Cek IP Address
cekfolder = lambda: os.system("pwd")
clear = lambda: os.system('clear') #"clear" untuk OS Linux | "cls" untuk OS Windows

def iTools():
	port = 99
	clear()
	print "\t\t\tiTools File Sharing"
	print "\t\t\t Versi : 1.0 Alpha"
	print "\t\t     Code by Indhi Farhandika"
	ip() #Cek IP Address
	host = raw_input('\nYour IP Address(inet) : ')#Input Ip Address, jika tidak diisi maka akan menjalankan Ip secara Otomatis
	hnd = http.server.SimpleHTTPRequestHandler
	http1 = socketserver.TCPServer((host,port),hnd)

	if host == '': #Untuk Ip Otomatis
		print '[+]Server Ip Default, Port :%s' % port
		print '[+]Direktory Sharing....'
		cekfolder()
		print '[+]Starting.....'
	else:
		print '[+]Server : %s:%s' % (host,str(port)) #Ip Setting Manual
		print '[+]Direktory Sharing....'
		cekfolder()
		print '[+]Starting.....'
	http1.serve_forever()#Start
if __name__ == "__main__":
	iTools() #Main()
