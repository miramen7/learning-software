from __future__ import print_function

def main():
    a = int(raw_input("Masukan nilai jam yang anda inginkan:\t "))
    b = int(raw_input("Masukan nilai menit yang anda inginkan:\t "))
    c = int(raw_input("Masukan nilai detik yang anda inginkan:\t "))
 
    if (a > 24):
        print("Nilai yang anda masukan salah")
    elif (b > 60):
        print("Nilai yang anda masukan salah")
    elif (c > 60):
        print("Nilai yang anda masukan salah")
    else:
        detik = (3600 * a) + (60 * b) + c
        #print(str(a) + ":" + str(b) + ":" + str(c) + " setara dengan: ")
        print("%s : %s : %s setara dengan: " % (a,b,c))
        print("%d detik" % detik)

if __name__ == "__main__":
    main()
