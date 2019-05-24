from __future__ import print_function

def printlist(li):
    for i in li:
        print(i, end='')
    print() 

def main():
    bilangan = xrange(20)
    genap = []
    ganjil = []

    for x in bilangan:
        if x % 2 == 0:
            genap.append(x)
        else:
            ganjil.append(x)

    print("Bilangan ganjil\t: ", end='')
    print(ganjil)
    print("Bilangan genap\t: ", end='')
    print(genap)

if __name__ == "__main__":
    main()
    
