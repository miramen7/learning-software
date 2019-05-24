from __future__ import print_function
import os

# mendefinisikan fungsi tanpa nilai balik
def printNoLine(p):
    "Mencetak teks dan bilangan tanpa baris baru"
    print(p, end='')
    return

# mendefinisikan fungsi dengan nilai balik
def addByOne(p):
    "Menambah bilangan p dengan nilai 1"
    value = p + 1
    return value

# mendefinisikan fungi tanpa nilai balik
# dan tanpa parameter
def clearscreen():
    "Membersihkan layar"
    os.system("cls")

# mendefinisikan fungsi main() (fungsi utama)
def main():
    # memanggil fungsi printNoLine()
    printNoLine("Umur = ")
    printNoLine(35)

    print() # membuat baris baru

    # memanggil fungsi addByOne()
    x = addByOne(10)
    print("10 + 1 = %d" % x)

if __name__ == "__main__":
    main()
