#filename = multiple-inheritance.py

from __future__ import print_function

#define first parent class
class Induk1 (object):
    def __init__(self, a):
        self.a = a

    def cetakA(self):
        print("Nilai a: ", self.a)

#define second parent class
class Induk2 (object):
    def __init__(self, b):
        self.b = b

    def cetakB(self):
        print("Nilai B: ", self.b)

#define derived class
class Anak(Induk1, Induk2):
    def __init__(self, a, b, c):
        #calling Induk1.__init__()
        Induk1.__init__(self, a)
        #calling Induk2.__init__()
        Induk2.__init__(self, b)
        self.c = c

    def cetakC(self):
        print("Nilai C: ", self.c)

def main():
    #creating object from Anak class
    obj = Anak(123, 456, 789)

    #calling Induk1 class method from obj
    obj.cetakA()

    #calling Induk2 class method from obj
    obj.cetakB()

    #calling Anak class method
    obj.cetakC()

if __name__ == "__main__":
    main() 
