from __future__ import print_function

def main():
    
    # mendefinisikan variabel beserta nilainya
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # menampilkan nilai variabel
    print("str1 = " +str1)

    # mengolah nilai max dan min dari nilai variabel dan menampilkannya
    print(" max(str1) = ", max(str1), \
        " ( ", ord(max(str1)), " ) " )

    print(" min(str1) = ", min(str1), \
        " ( ", ord(min(str1)), " ) " )

if __name__ == "__main__":
    main()
