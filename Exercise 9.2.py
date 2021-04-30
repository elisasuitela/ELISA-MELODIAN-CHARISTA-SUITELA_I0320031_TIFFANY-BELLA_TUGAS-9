#!c:\Python37\python

###########################################
# Nama file: array2.py
###########################################

import sys

# Mendefinisikan array asosiatif
KAMUS = {
    'one' : 'satu',
    'two' : 'dua',
    'three' : 'tiga',
    'four' : 'empat',
    'five' : 'lima',
    'six' : 'enam',
    'seven' : 'tujuh',
    'eight' : 'delapan',
    'nine' : 'sembilan',
    'ten' : 'sepuluh'
    # ...
        }

def main():
    # Meminta user memasukkan kata dalam bahasa inggris
    kata = input("Masukkan kata dalam bahasa inggris: ")

    if not (kata in KAMUS.keys()):
        print("'%s' tidak ditemukan di dalam kamus ini" % kata)
        sys.exit()
        
    print("Arti kata '%s' adalah '%s'" % (kata, KAMUS[kata]))
if __name__ == '__main__':
   main()
