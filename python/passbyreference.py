from __future__ import print_function

def ubahNilai(p):
    p *= 100
    print("\nNilai di dalam fungsi")
    print("p = %d" % p)
    return

def main():
    a = 5

    print("\nSebelum pemanggilan fungsi")
    print("a = %d" % a)

    # memanggil fungsi ubahNilai()
    # dengan a sebagai parameter aktualnya
    ubahNilai(a)

    print("\nSetelah pemanggilan fungsi")
    print("a = %d" % a)

if __name__ == "__main__":
    main()
