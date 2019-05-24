from __future__ import print_function
import sys

def main():
    try:
        filename = "contoh.txt"
        #membuka file
        f = open(filename)
        
        #membaca contoh.txt
        for line in f:
            print(line, end='')

        #menutup file
        f.close()
    except IOError as e:
        print("File '%s' tidak ditemukan" % filename)
        sys.exit()

if __name__ == "__main__":
    main()
