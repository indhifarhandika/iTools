#!/usr/bin/python
"""
    https://indhifarhandika.github.io
    Author : INDHI Farhandika
    Aplikasi iTools Mail
    Version 1.6
    Windows
"""

import smtplib,base64,os,getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkFileDialog import askopenfilename

clear = lambda: os.system('cls')
warna = lambda: os.system("color 7")

mymail=''
pas = ''
server = ''
mailReal = ''

def login():
    #------- Memanggil fungsi tampilan() ------#
    tampilan()
    #------- Variabel Global ------#
    global server
    global mymail
    global pas
    global mailReal
    #-----------------------------#
    print '\t\t+---=[Login Menggunakan Akun Gmail atau Yahoo]\n'
    mymail = raw_input('[+]Email : ')
    pas = getpass.getpass('[+]Password : ')
    #------[ iTools Teknik While ]---------
    mail1 = [mymail]
    mail2 = []
    mail_total = len(mymail)
    co = 0
    while(mail_total >= co):
        if mail1[0][mail_total-1] == '@':
            break
        mail2.append(mail1[0][mail_total-1])
        mail_total = mail_total - 1
    mail_total1 = len(mail2)
    mail3 = []
    while(mail_total1>co):
        mail3.append(mail2[mail_total1-1])
        mail_total1 = mail_total1 - 1
    mailReal = ''.join(mail3)
    #---------- Cek Email -------------#
    if mailReal.lower() == 'gmail.com':
        print '[+]Loading.....'
        server = smtplib.SMTP('smtp.gmail.com',587)
        print '[+]Menyambungkan ke Gmail.....'
        server.starttls()#Menyambungkan ke Gmail
        print '[+]Login.....'
        server.login(mymail,pas) #Login ke Gmail
        iTMail()
    elif mailReal.lower() == 'yahoo.com':
        print '[+]Loading.....'
        server = smtplib.SMTP('smtp.mail.yahoo.com',587)
        print '[+]Menyambungkan ke Yahoo.....'
        server.starttls()#Menyambungkan ke Yahoo
        print '[+]Login.....'
        server.login(mymail,pas) #Login ke Yahoo
        iTMail()
    elif mailReal.lower() == 'programmer.net':
        print '[+]Loading.....'
        server = smtplib.SMTP('smtp.mail.com', 587)
        print '[+]Menyambungkan ke Mail.....'
        server.starttls()
        print '[+]Login.....'
        server.login(mymail,pas)
        iTMail()
    else:
        print '[+]-----------Hanya bisa Login dengan akun Gmail atau Yahoo'
        raw_input('')
        login()
    #-----------------

def iTMail():
    global mymail
    global pas
    global server
    global mailReal
    tampilan()
    #------------------------
    if mailReal.lower() == 'gmail.com':
        print '\t\t+-----------------=[Gmail]'
        print '\t\t+----=[Your Mail : %s]\n' % mymail
    elif mailReal.lower() == 'yahoo.com':
        print '\t\t+-----------------=[Yahoo]'
        print '\t\t+----=[Your Mail : %s]\n' % mymail
    elif mailReal.lower() == 'programmer.net':
        print '\t\t+-----------------=[Mail]'
        print '\t\t+----=[Your Mail : %s]\n' % mymail
    #-------------------------
    yumail = raw_input('To : ')
    subject = raw_input('Subject : ')
    msg = MIMEMultipart()
    msg['From'] = mymail
    msg['To'] = yumail
    msg['Subject'] = subject
    pesan = raw_input('Pesan : ')
    msg.attach(MIMEText(pesan,'plain'))
    count = raw_input("Jumlah File : ")
    fileArray=[] #Array
    # Perulangan mengirim File
    while True: #Perulangan while 1
        if count == "":
            print '[+]Anda mengirim Pesan tanpa File'
            break
        else:
            for i in range(int(count)):
                while True: #Perulangan while 2
                    filename = askopenfilename(title = 'iTMail')
                    if filename == None:
                        continue
                    elif os.path.isfile(filename): #Cek File
                        #---Menentukan Nama File
                        #------[ iTools Teknik While ]---------
                        file1 = [filename]
                        file2 = []
                        file_total = len(filename)
                        co = 0
                        while(file_total >= co):
                            if file1[0][file_total-1] == '/':
                                break
                            file2.append(file1[0][file_total-1])
                            file_total = file_total - 1
                        file_total1 = len(file2)
                        file3 = []
                        while(file_total1 > co):
                            file3.append(file2[file_total1-1])
                            file_total1 = file_total1 - 1
                        fileReal = ''.join(file3)
                        print '[+]Nama File %i : %s' % ((i+1),fileReal)
                        #-----------------
                        attachment = open(filename,'rb') #Membuka File
                        fileArray=[i] #memasukan nama file ke dalam array
                        part = MIMEBase('application','octet-stream')
                        part.set_payload((attachment).read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition',"attachment; filename= "+ fileReal)
                        msg.attach(part)
                        break #Berhenti perulangan while 2
                    else:
                        filename = None
                        break
        break #Berhenti perulangan while 1
    #Exit Perulangan
    print '[+]Loading.....'
    text = msg.as_string()
    print '[+]Mengirim Pesan......'
    server.sendmail(mymail,yumail,text) #Mengirim Email
    print '[+]Pesan Terkirim'
    server.quit() #Exit

def tampilan():
    clear() #Clear Console
    print """
    \t\t++++++++++++++++++++++++++++++++++++++++++++++++++
    \t\t+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-+
    \t\t+-----------------=[iTMail Windows]-_-_-_-_-_-_-_+
    \t\t+--=[Versi 1.6]-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+
    \t\t+----------------=[Author : indhifarhandika]-_-_-+
    \t\t+----=[Email : indhi.farhandika@programmer.net]-_+
    \t\t+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-+
    \t\t++++++++++++++++++++++++++++++++++++++++++++++++++
    \t\t+------=[https://indhifarhandika.github.io]"""
if __name__ == '__main__':
    login()
