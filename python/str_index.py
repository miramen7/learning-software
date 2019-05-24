from __future__ import print_function

def main():
    str = "hello world!"
    
    print("str: " + str)
    print("str.index('o'): ", str.index('o'))
    print("str.index('o',5): ", str.index('o', 5))
    print("str.index('world'): ", str.index('world'))
    print("str.index('Python'): ", str.index('Python'))

if __name__ == "__main__":
    main()
