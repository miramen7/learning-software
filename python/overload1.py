from __future__ import print_function

# mendefinisikan fungsi jumlah()
def jumlah(bil1, bil2, bil3=None):
    if bil3 == None:
        return bil1 + bil2
    else:
        return bil1 + bil2 + bil3

def main():
    # memanggil fungsi jumlah()
    print("jumlah(2, 3) \t\t= ", jumlah(2, 3))
    print("jumlah(2, 3, 4) \t= ", jumlah(2, 3, 4))

if __name__ == "__main__":
    main()
