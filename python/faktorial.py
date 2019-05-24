from __future__ import print_function

def main():
    #Memasukan sebuah nilai faktorial
    a = int(raw_input("Masukan nilai faktorial yang diinginkan: "))
    
    faktorial = 1
    i = a
    while (i >=1):
        if i != 1: 
            print("%d x " % i, end=" ")
            faktorial *= i
        else:
            print("%d " % i, end=" ")
        i -= 1

    #Menampilkan hasil faktorial bilangan yang dimasukan
    print ("= %s" % faktorial)

if __name__ == "__main__":
    main()

