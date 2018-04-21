#!/usr/bin/python
<<<<<<< HEAD
"""
    https://indhifarhandika.github.io
    Author : INDHI Farhandika
    Aplikasi iTools Mail
    Version 1.6
    Linux
"""
=======
#Code by INDHI Farhandika
#Aplikasi iTools Mail
#Version 1.6
>>>>>>> 6f4a2175ecd13de448ba96fb6ff88380fb42ae3a

import smtplib,base64,os,getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from colored import fg, attr, bg
from tkFileDialog import askopenfilename

clear = lambda: os.system('clear')

mymail=''
pas = ''
server = ''
mailReal = ''

def login():
<<<<<<< HEAD
    #------- Memanggil fungsi tampilan() ------#
    tampilan()
    #------- Variabel Global ------#
=======
    tampilan()
>>>>>>> 6f4a2175ecd13de448ba96fb6ff88380fb42ae3a
    global server
    global mymail
    global pas
    global mailReal
<<<<<<< HEAD
    #-----------------------------#
=======
>>>>>>> 6f4a2175ecd13de448ba96fb6ff88380fb42ae3a
    print '%s\t\t+---=[%s%sLogin Menggunakan Akun Gmail atau Yahoo%s%s]\n' % (fg('white'),bg('white'),fg('red'),attr('reset'),fg('white'))
    mymail = raw_input('%s[+]Email : '% fg('white'))
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
<<<<<<< HEAD
    #---------- Cek Email -------------#
=======
    #--------------------------------
>>>>>>> 6f4a2175ecd13de448ba96fb6ff88380fb42ae3a
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
        print '\t\t%s+-----------------=[%s%sGmail%s%s]' % (fg('white'),bg('white'),fg('red'),attr('reset'),fg('white'))
        print '\t\t+----=[%s%sYour Mail : %s%s%s]\n' % (bg('white'),fg('red'),mymail,attr('reset'),fg('white'))
    elif mailReal.lower() == 'yahoo.com':
        print '\t\t%s+-----------------=[%s%sYahoo%s%s]' % (fg('white'),bg('white'),fg('red'),attr('reset'),fg('white'))
        print '\t\t+----=[%s%sYour Mail : %s%s%s]\n' % (bg('white'),fg('red'),mymail,attr('reset'),fg('white'))
    elif mailReal.lower() == 'programmer.net':
        print '\t\t%s+-----------------=[%s%sMail%s%s]' % (fg('white'),bg('white'),fg('red'),attr('reset'),fg('white'))
        print '\t\t+----=[%s%sYour Mail : %s%s%s]\n' % (bg('white'),fg('red'),mymail,attr('reset'),fg('white'))
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
<<<<<<< HEAD
                    filename = askopenfilename(title = 'iTMail')
=======
                    filename = askopenfilename(title='iTMail')
>>>>>>> 6f4a2175ecd13de448ba96fb6ff88380fb42ae3a
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
<<<<<<< HEAD
                        while(file_total1 > co):
=======
                        while(file_total1>co):
>>>>>>> 6f4a2175ecd13de448ba96fb6ff88380fb42ae3a
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
    %s%s\t\t++++++++++++++++++++++++++++++++++++++++++++++++++
    \t\t+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-+
<<<<<<< HEAD
    \t\t+------------------=[%siTMail Linux%s]_-_-_-_-_-_-_-_+
    \t\t+--=[%sVersi 1.6%s]-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+
    \t\t%s+----------------=[%sAuthor : indhifarhandika%s]-_-_-+
    \t\t+----=[%sEmail : indhi.farhandika@programmer.net%s]-_+
    \t\t+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-+
    \t\t++++++++++++++++++++++++++++++++++++++++++++++++++
    \t\t+------=[%s%shttps://indhifarhandika.github.io%s]%s""" % (attr('bold'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),attr('bold'),fg('red'),fg('white'),attr('reset'))
=======
    \t\t+--------------------=[%siTMail%s]_-_-_-_-_-_-_-_-_-_+
    \t\t+--=[%sVersi 1.6%s]-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_+
    \t\t%s+----------------=[%sAuthor : indhifarhandika%s]-_-_-+
    \t\t+-----=[%sEmail : indhifarhandika@programmer.net%s]-_+
    \t\t+_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-+
    \t\t++++++++++++++++++++++++++++++++++++++++++++++++++
    \t\t|%s""" % (attr('bold'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),fg('red'),fg('white'),attr('reset'))
>>>>>>> 6f4a2175ecd13de448ba96fb6ff88380fb42ae3a
if __name__ == '__main__':
    login()
