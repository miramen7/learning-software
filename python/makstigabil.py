from __future__ import print_function

def main():
    a = int(raw_input("Masukan bilangan pertama: "))
    b = int(raw_input("Masukan bilangan kedua: "))
    c = int(raw_input("Masukan bilangan ketiga: "))

    maks = a
    if (b > maks):
        maks = b
    else:
        (c > maks)
        maks = c
  
    print("Nilai maksimum adalah %s" % maks)

if __name__ == "__main__":
    main()

