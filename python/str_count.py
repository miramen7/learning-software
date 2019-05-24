from __future__ import print_function

def main():
    k = "Hello World!"
    
    a = k.count("l")
    b = k.count("o")
    c = k.count("l",1, 6)

    
    print("Huruf 'l' dalam str: ", a)
    print("Huruf 'o' dalam str: ", b)
    print("Huruf 'l' dalam index 1-6: ",c)

if __name__ == "__main__":
    main()
