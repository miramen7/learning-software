
from __future__ import print_function

def main():
    
    #mendefinisikan variabel serta nilainya
    str1 = "	PYTHON"
    str2 = 'python99'
    str3 = "--PYTHON--"

    #menampilkan nilai dari variabel yang telah didefinisikan
    print("str 1 = " +str1)
    print("str 2 = " +str2)
    print("str 3 = " +str3)

    #menghapus karakter tertentu dalam variabel sesuai dengan metode yang diinginkan
    print("\nstr 1 = ", str1.lstrip())
    print("str 2 = ", str2.rstrip('9'))
    print("str 3 = ", str3.strip('-'))

if __name__ == "__main__":
    main()
