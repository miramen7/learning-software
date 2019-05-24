from __future__ import print_function

def main():
    #Memasukan nilai variabel yang akan dikalikan
    a = int(raw_input("Masukan nilai pertama yang akan dikalikan: "))
    b = int(raw_input("Masukan nilai kedua yang akan dikalikan: "))

    sum = 0
    for i in range (0,a):
        if (i <a-1):
            print("%s + " % a, end=" ")
            sum += b
        else:
            print("%s\n" % a)
            sum += b

    print("atau\n")
    for j in range (0,b):
        if (j < b-1):
            print("%s + " % b, end=" ")
        else:
            print("%s\n" % b)

    print("%s x %s = %s" %(a,b,sum))

if __name__ == "__main__":
    main()
