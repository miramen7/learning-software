from __future__ import print_function

def main():
    x = int(raw_input("Masukan nilai x: "))
    y = int(raw_input("Masukan nilai y: "))

    if x > 0 and  y > 0:
        print("Titik koordinat terdapat dalam kuadran 1")
    elif x < 0 and y > 0:
        print("Titik koordinat terdapat dalam kuadran 2")
    elif x < 0 and y > 0:
        print("Titik koordinat terdapat dalam kuadran 3")
    elif x > 0 and y < 0:
        print("Titik koordinat terdapat dalam kuadran 4")
    else:
        print("Titik koordinat tidak terdapat pada kuadran manapun")

if __name__ == "__main__":
    main()
