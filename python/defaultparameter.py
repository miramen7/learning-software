from __future__ import print_function

# mendefinisikan fungsi dengan parameter default
def infoKaryawan(nama, usia = 35):
    print("Nama: %s" % nama)
    print("Usia: %d" % usia, end="\n\n")
    return

def main():
    # memanggil fungsi infokaryawan
    infoKaryawan("Bimo")
    infoKaryawan("Rizki", usia = 40)
    infoKaryawan("Hanggoro", usia = 49)

if __name__ == "__main__":
    main()


