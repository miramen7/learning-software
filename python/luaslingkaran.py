#!C:\Python27\python

from __future__ import print_function
import math

def main():
    print("Game luas lingkaran")
    r = float(raw_input("Masukan jari-jari: "))
    L = math.pi * (r ** 2)
    K = 2 * math.pi * r
    
    print("radius: ", r)
    print("Luas lingkaran adalah ", L)
    print("Keliling lingkaran adalah %f" %  K)

if __name__ == "__main__":
    main()
