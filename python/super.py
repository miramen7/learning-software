#filename = super.py

from __future__ import print_function

#define main class (superclass)
class Kotak(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    def hitungVolume(self):
        return self.panjang * self.lebar * self.tinggi

    def cetakData(self):
        print("Panjang\t\t:", self.panjang)
        print("Lebar\t\t:", self.lebar)
        print("Tinggi\t\t:", self.tinggi)

    def cetakVolume(self):
        print("Jumlah Volume\t:", self.hitungVolume())

#define derived class (subclass)
class KotakWarna(Kotak):
    def __init__(self, p, l, t, w):
        #calling Kotak.__init__()
        super(KotakWarna, self).__init__(p, l, t)
        #add new attributes
        self.warna = w

    def cetakData(self):
        #calling Kotak.cetakData()
        super(KotakWarna, self).cetakData()

def main():
    #create KotakWarna object
    kotakwarna1 = KotakWarna(10, 3, 4, "biru")
    
    #using object 
    kotakwarna1.cetakData()
    kotakwarna1.cetakVolume()

if __name__ == "__main__":
    main() 
