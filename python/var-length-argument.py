from __future__ import print_function

def cetakParameter(*var):
    for i in var:
        print(i)
    return

def main():
    # memanggil fungsi
    print("Satu Parameter")
    cetakParameter(10)

    print("\nDua Parameter")
    cetakParameter(10, 20)

    print("\nTiga Parameter")
    cetakParameter(10, 20, 30)

if __name__ == "__main__":
    main()
