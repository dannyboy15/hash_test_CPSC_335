'''
   A program to test hash function variations
'''
# import Hash.py
from Hash import *


def testHash(radix, modulus, fName):
    print()
    print("Using radix " + str(radix) + " and modulus " + str(modulus) + ".")
    print()
    print("  Input  |  hash value")
    print("----------------------")
    file = open(fName)
    for line in file:
        for word in line.strip().split(' '):
            if (word != ''):
                print('{0:10s} {1:8d}'.format(word, hash(word, radix, modulus)))
    print()


def run_test():
    while True:
        inp = input("Enter the radix, modulus, and file: ")
        r, m, f = inp.split(',')
        testHash(int(r), int(m), f.lstrip())


if __name__ == "__main__":
    run_test()
