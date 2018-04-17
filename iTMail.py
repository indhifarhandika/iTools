#!/usr/bin/python
#Code by INDHI Farhandika
#Aplikasi iTools Mail
#Version 1.2 Beta

import smtplib,base64,os,getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from colored import fg, attr
from tkFileDialog import askopenfile

clear = lambda: os.system('clear')

mymail = base64.b64decode('aW5kaGlmYXJoYW5kaWthQGdtYWlsLmNvbQ==') #My Email
ps = base64.b64decode('aW5maXRhMTk5OQ==') #My Password

def iTools():
    clear() #Clear Console
    print "\t\t\t    %s%siTools Mail" % (fg('red'),attr('bold'))
    print "\t\t\t %sVersi : 1.2 Beta" % (fg('white'))
    print "\t\t     %sCode by Indhi Farhandika\n\t\t%shttps://github.com/indhifarhandika/iTools%s\n" % (fg('red'), fg('white'), attr('reset'))
    print "%s1. Mengirim Pesan\n%s2. Help\n%s3. Keluar%s" % (fg('red'), fg('white'), fg('red'), attr('reset'))
    pilih = raw_input('%s[+]Pilih >> ' % (fg('white')))
    if pilih == '1':
        PesanFile() #Pesan dan File
    elif pilih == '2':
        hel()
    elif pilih == '3':
         print '[+]Thanks'#Keluar Aplikasi
    else:
        print 'Salah'
        raw_input('')
        return (iTools())
def hel():
    print '\t\t\tLogin menggunakan akun Gmail\n'
    raw_input('Tekan Enter untuk kembali ke Menu')
    iTools()
def PesanFile():
    #mymail = raw_input('Email : ')
    #pas = getpass.getpass('Password : ')
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
            ##while True: #Perulangan while 2
                #dire = raw_input('Letak File : ')
                #if dire == '':
                    #continue
                #elif os.path.isdir(dire):
            for i in range(int(count)):
                while True: #Perulangan while 3
                    filename = askopenfile()
                            #dirfil = dire + filename
                    if filename == '':
                        continue
                    else :#os.path.isfile(str(filename)): #Cek File
                        attachment = open(str(filename),'r') #Membuka File
                        fileArray=[i] #memasukan nama file ke dalam array
                        part = MIMEBase('application','octet-stream')
                        part.set_payload((attachment).read())
                        encoders.encode_base64(part)
                        part.add_header('Content-Disposition',"attachment; filename= "+ str(filename))
                        msg.attach(part)
                        break #Berhenti perulangan while 3
                    #else:
                    #    print '[+]File tidak ditemukan'
                    #    continue
                    #break #Berhenti perulangan while 2
                else:
                    print '[+]Folder tidak di temukan'
                    continue
        break #Berhenti perulangan while 1
    #Exit Perulangan
    print '[+]Loading.....'
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587) #menyambungkan ke Gmail, untuk Yahoo ('smtp.mail.yahoo.com',587)
    server.starttls()
    print '[+]Login......'
    server.login(mymail,ps) #Login ke Gmail
    print '[+]Mengirim Pesan......'
    server.sendmail(mymail,yumail,text) #Mengirim Email
    print '[+]Pesan Terkirim'
    server.quit() #Exit
if __name__ == '__main__':
    iTools()
