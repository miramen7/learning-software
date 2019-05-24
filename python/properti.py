#filename = properti.py

from __future__ import print_function

class Titik(object):
    def __init__(self, x = None, y = None):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, nilai):
        if (not isinstance(nilai, int) and not isinstance(nilai, float)):
            raise TypeError("x must be numeric")
        self.__x = nilai

    @x.deleter
    def x(self):
        del self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, nilai):
        if (not isinstance(nilai, int) and not isinstance(nilai, float)):
            raise TypeError("y must be numeric")
        self.__y = nilai

    @y.deleter
    def y(self):
        del self.__y

def main():
    #create object from Titik class
    A = Titik()
    B = Titik(15, 30)

    #determine value of __x and __y inside A
    #through property x and y
    A.x = 25
    A.y = 50

    #take __x and __y value inside A
    #through property x and y
    print("A(%d. %d)" %(A.x, A.y))

    #take __x and __y value inside B
    #through property x and y
    print("B(%d. %d)" %(B.x, B.y))

if __name__ == "__main__":
    main()
