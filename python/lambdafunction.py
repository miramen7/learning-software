from __future__ import print_function

# mendefinisikan fungsi pemanggil dengan
# parameter dan nilai kembalian berupa fungsi
def panggil(func):
    return func

# mendefinisikan fungsi lain
def HelloWorld():
    return "Hello World!"

def main():
    # mendefinisikan list
    daftarnama = ["Dewi", "bimo", "AJI", "BAYU", "Cahya"]
    print("Keadaan awal")
    print(daftarnama)

    # mengurutkan element list dengan fungsi sorted()
    print("\nMenggunakan sorted():")
    print(sorted(daftarnama))

    # melewatkan lambda function untuk mengurutkan
    # elemen tanpa mempedulikan huruf kecil/besar
    daftarnama.sort(key=lambda n: n.lower())

    # menampilkan nilai list
    print("\n Keadaan akhir:")
    print(daftarnama)

if __name__ == "__main__":
    main()
