#!c:\Python37\python

###########################################
# Nama file: array2.py
###########################################

import sys

# Mendefinisikan array konstan
HARI = ('Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu')

def main():
    # Meminta user memasukkan nomor hari
    nohari = int(input("Masukkan nomor dari [1..7]: "))

    if (nohari < 1) or (nohari > 7):
        print("TIdak ada hari ke-%s" % nohari)
        sys.exit(1)

    print("Hari ke-%d adalah %s" % (nohari, HARI[nohari-1]))

if __name__ == '__main__':
    main()
