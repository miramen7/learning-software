from __future__ import print_function

def main():
    #Membuat list nama-nama hari
    hari = ("senin","selasa","rabu","kamis","jumat","sabtu","minggu")
    
    #Memasukan sebuah hari
    namahari = raw_input("Masukan sebuah nama hari: ")
    
    if namahari.lower() == hari[5] or \
       namahari.lower() == hari[6]:
       print("%s adalah hari libur" % namahari)
    else:
       print("%s adalah hari kerja(terutama untuk karyawan)" % namahari)

if __name__ == "__main__":
    main() 
