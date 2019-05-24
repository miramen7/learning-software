from __future__ import print_function

def main():
   
    # mendefinisikan variabel serta nilai dari variable itu sendiri
    str1 = "hurufbesar"
    str2 = "HURUFKECIL"

    # menampilkan hasil input di layar
    print("str1 = " + str1)
    print("str2 = " + str2)

    # menguji apakah variabel diatas memiliki huruf besar semua atau huruf kecil semua
    print("\nstr1.islower() = ",  str.islower(str1))
    print("str2.islower() = ",  str.islower(str2))

    print("\nstr1.isupper() = ",  str.isupper(str1))
    print("str2.isupper() = ",  str.isupper(str2))

if __name__ == "__main__":
    main()
