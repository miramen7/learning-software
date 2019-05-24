from __future__ import print_function
import math

def main():
    a = int(raw_input("Masukan nilai koefisien persamaan ke-1: "))
    b = int(raw_input("Masukan nilai koefisien persamaan ke-2: "))
    c = int(raw_input("Masukan nilai koefisien persamaan ke-3: "))

    D = ((b**2) - (4*a*c))
    x1 = (-b + math.sqrt(D)) // (2 * a)
    x2 = (-b - math.sqrt(D)) // (2 * a)
    
    if D < 0:
        print("Akar-akar yang dihasilkan akar imajiner")
    elif D == 0:
        print("Akar- akar yang dihasilkan adalah akar real dan kembar") 
    	print("x1: %d" % x1)
    	print("x2: %d" % x2)
    else:
        print("Akar-akar yang dihasilkan adalah akar real dan berbeda")
     	print("x1: %d" % x1)
    	print("x2: %d" % x2)       

if __name__ == "__main__":
    main()
