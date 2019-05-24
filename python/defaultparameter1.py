from __future__ import print_function

def cetakDaftar(alist=[], urut = False):
    if urut:
        alist.sort()
    for i in alist:
        print(i, end=" ")
    print()
    return

def main():
    # membuat list
    li = [65, 34, 21, 89, 75, 24]
    print("Data tidak terurut")

    # memanggilfungsi cetakDaftar
    cetakDaftar(li)

    print("\nData terurut")
    cetakDaftar(li, True)

if __name__ == "__main__":
    main()
