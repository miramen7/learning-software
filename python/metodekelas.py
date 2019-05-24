#filename = metodekelas.py

from __future__ import print_function

class tanggal(object):
    def __init__(self, dd = 0, mm = 0, yyyy = 0):
        #input object with data from __init__
        self.hari = tanggal.hari = dd
        self.bulan = tanggal.bulan = mm
        self.tahun = tanggal.tahun = yyyy

    @classmethod
    def dariString(cls,strTanggal):
        hari, bulan, tahun = map(int, strTanggal.split('-'))
        objekTanggal = cls(hari, bulan,  tahun)
        return objekTanggal

    def cetakTanggal(self):
        BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
        print("%d %s % d" %(self.hari, BULAN[self.bulan-1], self.tahun))

def main():
    #create object from tanggal class
    #with regular way
    obj1 = tanggal(19, 5, 1983)

    #create object from tanggal class
    #with class method
    obj2 = tanggal.dariString("10-5-2010")

    #print tanggal
    print("Data pada obj1: ", end="")
    tanggal.cetakTanggal(obj1)
    print("Data pada obj2: ", end="")
    tanggal.cetakTanggal(obj2)

if __name__ == "__main__":
    main()