from __future__ import print_function

# mendefinisikan fungsi pemanggil dengan
# parameter dan nilai kembalian berupa fungsi
def panggil(func):
    return func

# mendefinisikan fungsi lain
def HelloWorld():
    return "Hello World!"

def main():
    # memanggil fungsi panggil() dengan melewatkan
    # fungsi HelloWorld() sebagai argumennya
    s = panggil(HelloWorld())
    print(s)

if __name__ == "__main__":
    main()
