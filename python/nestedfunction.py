from __future__ import print_function
import time

def hitungMundur(n):
    li = [n]
    def next():
        r = li[0]
        li[0] -= 1
        return r
    return next

def main():
    # memanggil fungsi hitungMundur()
    next = hitungMundur(3)
    while True:
        val = next()
        if val == 0:
            print("Go!!!")
            break
        print(val, end=' ')
        time.sleep(1) # jeda 1 detik

if __name__ == "__main__":
    main()
