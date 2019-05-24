#!\Python27\python

from __future__ import print_function
import os, compileall

def main():
    dir = "/Users/muhammadibadurrahman/kodepython"
    compileall.compile_dir(dir)
    print("Semua file dalam %s telah dikompilasi" % dir)

if __name__ == "__main__":
    main()
