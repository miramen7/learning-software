from __future__ import print_function

# mendefinisikan fungsi bagi()
def bagi(bil1,bil2):
    if isinstance(bil1, int) and \
       isinstance(bil2, int):
       return bil1 // bil2
    else:
        return bil1 / bil2

def main():
    # memanggil fungsi bagi() untuk bilangan bulat
    print("Pembagian bilangan bulat:")
    print("10/3 \t\t= ", bagi(10,3))

    # memanggil fungsi bagi() untuk bilangan riil
    print("\nPembagian bilangan riil:")
    print("10.0/3.0 \t = ", bagi(10.0, 3.0))
    print("10.0/3 \t\t= ", bagi(10,0.3))
    print("10/3.0 \t\t= ", bagi(10, 3.0))

if __name__ == "__main__":
    main()
