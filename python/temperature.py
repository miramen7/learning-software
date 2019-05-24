from __future__ import print_function

def main():
    c = float(raw_input("Masukan suhu derajat Celsius:"))
    fah = 9 * (c+32) / 5
    
    print("Nilai suhu derajat Celsius: %f" % c)
    print("Nilai suhu derajat Fahrenheit: %f" % fah)

if __name__ == "__main__":
    main()

