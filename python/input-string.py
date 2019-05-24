# !C:\Python27\python

from __future__ import print_function

def main():
    #membuat prompt dengan tipe data string
    nama = raw_input("Masukan nama anda: ")
    
    #masukan prompt dengan tipe data karakter
    karakter = raw_input("Masukan sebuah karakter: ")

    print("Halo, %s, Apa kabar?" % nama)
    print ("%s belajar Python %d dan Python %d" %("Arman",2,3))
    print("Karakter yang dimasukan: '%s'" % karakter)

if __name__ == "__main__":
    main()
