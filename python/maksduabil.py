from __future__ import print_function

def main():
    bil1 = int(raw_input("Masukan sebuah bilangan: "))
    bil2 = int(raw_input("Kemudian masukan bilangan lainnya: "))

    if (bil1 > bil2):
        print("Nilai maksimum adalah %s" % bil1)
    else:
        print("Nilai maksimum adalah %s" % bil2)
if __name__ == "__main__":
    main()

