# !/Python27/python

from __future__ import print_function

def main():
    bilriil = float(raw_input("Masukan sebuah bilangan riil: "))
    hasil = bilriil*2
    print("Bilangan riil yang dimasukkan: %.2f" %bilriil)
    print("%.2f x 2 = %.2f" %(bilriil,hasil))

if __name__ == "__main__":
    main()
