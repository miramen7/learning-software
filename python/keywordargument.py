from __future__ import print_function

def infoKaryawan(nama, usia, gaji):
    print("Nama: %s" % nama)
    print("Usia: %d" % usia)
    print("Gaji: %d" % gaji, end="\n\n")
    return

def main():
    # memanggil fungsi
    infoKaryawan(nama = "Bimo", usia = 36, gaji = 4500000)
    infoKaryawan(usia = 40, gaji = 10000000, nama = "Valentino")
    infoKaryawan(gaji = 9500000, nama = "Suryo", usia = 50)

if __name__ == "__main__":
    main()
