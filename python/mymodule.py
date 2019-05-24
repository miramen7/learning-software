from __future__ import print_function

def tambah(a,b):
    return a + b 
def kurang(a,b):
    print("%d" % tambah(8,7))
    return a - b
    
def kali(a,b):
    return a*b
def bagi(a,b):
    if isinstance(a,int) and isinstance(b,int):
        return a // b
    else:
        return a / b

def main():
    c = kurang(8,7)
    print("%s" % c)
#print ("%d" % c)
if __name__ == "__main__":
    main()
