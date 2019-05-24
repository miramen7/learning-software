from __future__ import print_function

def main():
    x = int(raw_input("Masukan nilai yang anda inginkan: "))

    if x > 0:
        print("%d adalah bilangan positif" % x)
    elif x == 0:
        print("%d sama dengan nol" % x)
    else:
        print("%d adalah bilangan negatif" % x)

if __name__ == "__main__":
    main()
