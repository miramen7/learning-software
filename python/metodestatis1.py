#filename = metodestatis1.py

from __future__ import print_function
import math

class hitung(object):
    def __init__(self, p, l, t):
        pass

    @staticmethod
    def log10(x):
        return math.log10(x)

    @staticmethod
    def log(x):
        return math.log(x)

    @staticmethod
    def kali(x, y):
        return x * y

    @staticmethod
    def pangkat(x, y):
        return x ** y

    @staticmethod
    def akar(x):
        return math.sqrt(x)

    @staticmethod
    def absolute(x):
        return abs(x)

def main():
    print("hitung.log10(1000)\t\t= ", hitung.log10(1000))
    print("hitung.log(1000)\t\t= ", hitung.log(1000))
    print("hitung.kali(6, 9)\t\t= ", hitung.kali(6, 9))
    print("hitung.pangkat(9, 2)\t\t= ", hitung.pangkat(9, 2))
    print("hitung.akar(25)\t\t\t= ", hitung.akar(25))
    print("hitung.absolute(-2)\t\t= ", hitung.absolute(-2))

if __name__ == "__main__":
    main()