#!/usr/bin/python
#Code by INDHI FARHANDIKA R
#Aplikasi iTBase64

import base64,os

def iTools():
    os.system("clear")
    print("\t\tiToolsBase64 by indhifarhandika\t\t")
    pilih = raw_input(">> ")
    if pilih=="E" or pilih=="e":
        os.system("clear")
        e = raw_input(">> ").encode('utf-8')
        e1 = base64.b64encode(e)
        print(e1)
    elif pilih=="D" or pilih=="d":
        os.system("clear")
        d = raw_input(">> ")
        d1 = base64.b64decode(d)
        print(d1)
    elif pilih=="help":
        print("\nE = Encrypt\nD = Decrypt\nex = Exit Aplikasi\n\nPress Enter to Continue")
        raw_input()
        iTools()
    elif pilih=="ex":
	    print('')
    else:
        print('\nPerintah yang anda masukkan Salah, Press Enter to Continue')
        raw_input()
        iTools()
if __name__ == '__main__':
	iTools()
