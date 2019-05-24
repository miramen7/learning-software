from __future__ import print_function

def main():
    #Membuat tuple
    hari = ("senin","selasa","rabu","kamis","jumat","sabtu","minggu")

    #memasukan sebuah string nama hari
    namahari = raw_input("Masukan nama hari: ")

    if namahari.lower() == hari[5] or \
       namahari.lower() == hari[6]:
       print("%s adalah hari libur" % namahari)

if __name__ == "__main__":
    main()
    
