from __future__ import print_function

def main():
    #Memasukan sebuah nilai bilangan bulat
    x = int(raw_input("Masukan sebuah bilangan bulat: "))
    
    #Mengelompokan bilangan ganjil dan bilangan genap
    if x % 2 == 0:
        print("%s adalah bilangan genap" % x)
    else:
        print("%s adalah bilangan ganjil" % x)

if __name__ == "__main__":
    main()
