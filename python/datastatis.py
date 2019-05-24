#filename = datastatis.py

from __future__ import print_function

class Kotak(object):
    ObjectCounter = 0 #class variable

    def __init__(self, p, l, t):
        self.p = p #instance variable
        self.l = l #instance variable
        self.t = t #instance variable
        #everytime object found the objectcounter will be raised by 1
        Kotak.ObjectCounter += 1

    #create function to find volume
    def HitungVolume(self):
        return self.p * self.l* self.t

    #create function to print Data
    def CetakData(self):
        print("Hitung volume kotak")
        print("Panjang\t\t: ", self.p)
        print("Lebar\t\t: ", self.l)
        print("Tinggi\t\t: ", self.t)

    def CetakVolume(self):
        print("Volume\t\t: ", self.HitungVolume())

def main_method():
    Kotak1 = Kotak(6, 4, 3)
    print("Objek 1")
    Kotak1.CetakData()
    Kotak1.CetakVolume()
    print("Object Counter\t: ", Kotak1.ObjectCounter)

    Kotak2 = Kotak(5, 4, 5)
    print("\nObjek 2")
    Kotak2.CetakData()
    Kotak2.CetakVolume()
    print("Object Counter\t: ", Kotak2.ObjectCounter)

    Kotak3 = Kotak(3, 5, 1)
    print("Objek 3")
    Kotak3.CetakData()
    Kotak3.CetakVolume()
    print("Object Counter\t: ", Kotak3.ObjectCounter)

if __name__ == "__main__":
    main_method()
