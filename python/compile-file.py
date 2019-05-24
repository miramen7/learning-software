#!\Python27\python

from __future__ import print_function
import os,py_compile

def main():
    os.chdir("/Users/muhammadibadurrahman/kodepython")
    py_compile.compile("hello.py")
    print("File hello.pyc telah terbuat...")

if __name__  == "__main__":
    main()
