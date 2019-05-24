#filename = destruktor1.py

from __future__ import print_function

class myfile(object):
    def __init__(self, filename):
        self.file= open(filename)

    #create destructor function
    def __del__(self):
        self.file.close()
        print("Destruktor diaktifkan")

    def BacaData(self):
        for baris in self.file:
            print(baris, end='')


def main():
    #open destinated file
    f = myfile("sample.txt")
    #read file function activated
    f.BacaData()

    #Destruct f
    del f

if __name__ == "__main__":
    main()