#!/usr/bin/python
#Code by INDHI FARHANDIKA R
#Aplikasi iToolsDownloads

import urllib

def iTools():
    fi1 = raw_input('Link >> ')
    fi2 = raw_input('NamaFile.format >> ')
    urllib.urlretrieve(fi1, fi2)
    print('Download Selesai :)')

if __name__ == '__main__':
    iTools()
