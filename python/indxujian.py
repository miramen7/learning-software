from __future__ import print_function

def main():
    a = int(raw_input("Masukan nilai UTS mahasiswa: "))
    b = int(raw_input("Masukan nilai UAS mahasiswa: "))

    NA = (0.65*b) + (0.35*a)

    if (NA >= 80):
        indeks = 'A'
    elif ((NA < 80) & (NA >= 70)):
        indeks = 'B'
    elif ((NA < 70) & (NA >= 55)):
        indeks = 'C'
    elif ((NA < 55) & (NA >= 40)):
        indeks = 'D'
    elif ((NA < 40) & (NA >=0)):
        indeks = 'E'
    else:
        print("Nilai yang anda masukan salah")

    print("Indeks yang didapat dari nilai akhir mahasiswa adalah: ")
    print("%s" % indeks)

if __name__ == "__main__":
    main()
