#filename = dataprivate.py

from __future__ import print_function

class Titik(object):
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    #setter
    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    #getter
    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

def main():
    #creating object
    A = Titik()

    #define __x & __y value
    A.setx(6)
    A.sety(4)

    A.getx()
    A.gety()

    # takes values __x and __y
    print("A(%d, %d)" %(A.getx(), A.gety()))

if __name__ == "__main__":
    main()
