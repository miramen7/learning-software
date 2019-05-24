from __future__ import print_function

def main():
    a = raw_input("Masukan sebuah variabel: ")
    b = raw_input("Masukan variabel lain: ")

    c = a
    a = b
    b = c

    print("Nilai kedua variabel ditukar")
    print("Nilai variabel pertama menjadi:\t ", a)
    print("Nilai variabel kedua menjadi:\t ", b)

if __name__ == "__main__":
    main()
