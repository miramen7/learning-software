#filename = kelasabstrak1.py

from __future__ import print_function
import math

#define abstract class
class Bangun3D(object):
    #define abstract method
    def cetakData(self):
        raise NotImplementedError
    def hitungVolume(self):
        raise NotImplementedError
    def cetakVolume(self):
        raise NotImplementedError

#define concrete abstract class which is
#derivative from abstract class
class Kotak(Bangun3D):
    def __init__(self, p, l=None, t=None):
        if l == None and t == None:
            #if it is a cube
            self.panjang = self.lebar = self.tinggi = p
        else:
            #if it is a beam
            self.panjang = p
            self.lebar = l
            self.tinggi = t
    #implement cetakData() method
    def cetakData(self):
        print("Panjang\t\t: ", self.panjang) 
        print("Lebar\t\t: ", self.lebar) 
        print("Tinggi\t\t: ", self.tinggi)

    #implement hitungVolume() method
    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi

    #implement cetakVolume() method
    def cetakVolume(self):
        print ("Volume Kotak\t: ", self.hitungVolume())

class Tabung(Bangun3D):
    def __init__(self, r, t):
        self.jarijari = r
        self.tinggi = t

    #implement cetakData() method
    def cetakData(self):
        print("Jari-jari\t: ", self.jarijari)
        print("Tinggi\t\t: ", self.tinggi)

    #implement hitungVolume() method
    def hitungVolume(self):
        return math.pi * pow(self.jarijari,2) * self.tinggi

    #implement cetakVolume() method
    def cetakVolume(self):
        print("Volume Tabung\t: ", self.hitungVolume())

def main():
    obj1 = Kotak(6, 5, 4) # balok
    print("\nBALOK")
    obj1.cetakData()
    obj1.cetakVolume()

    obj2 = Kotak(4,4,4) # kubus 
    print("\nKUBUS")
    obj2.cetakData()
    obj2.cetakVolume()
    
    obj3 = Tabung(6,5) # tabung
    print("\nTABUNG")
    obj3.cetakData()
    obj3.cetakVolume()

if __name__ == "__main__":
    main()
    
