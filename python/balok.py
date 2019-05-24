from __future__ import print_function

def main():
    p = float(raw_input("Masukan panjang balok: "))
    l = float(raw_input("Masukan lebar balok: "))
    t = float(raw_input("Masukan tinggi balok: "))

    V = p * l * t
    L = 2 * ( (p * l) + (l * t)+ (p * t) )

    print("\nVolume balok adalah %f" % V)
    print("Luas balok adalah %f" % L)

if __name__ == "__main__":
    main()

