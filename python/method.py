#Filename: method.py

from __future__ import print_function

#create class to define square length, width, and height
class Kotak(object):
    def __init__(self, p,l,t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    #create function to find volume
    def HitungVolume(self):
        return self.panjang * self.lebar* self.tinggi

    #create function to print Data
    def CetakData(self):
        print("Hitung volume kotak")
        print("Panjang: ", self.panjang)
        print("Lebar: ", self.lebar)
        print("Tinggi: ", self.tinggi)
        print("Volume: ", self.HitungVolume())

def main_method():
    Kotak1 = Kotak(6, 4, 3)
    Kotak1.CetakData()

if __name__ == "__main__":
    main_method()