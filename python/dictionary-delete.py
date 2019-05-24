#!C:\Python27\python

from __future__ import print_function

def main():
    d = {'satu':20,'dua':40,'tiga':60}
    print("Elemen sebelum dihapus %s" % d)   
 
    #menghapus elemen kedua
    del d['dua']
    print("Setelah elemen kedua dihapus, maka d menjadi %s" % d)
    
    #menghapus elemen ketiga
    del d['tiga']
    print("Setelah elemen kedua dan ketiga dihapus, maka d menjadi %s" % d)

if __name__ == "__main__":
    main()
