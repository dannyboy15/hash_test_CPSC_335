'''
   A program to test hash function variations
'''
from collections import Counter
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


def count_hash(radix, modulus, fName):
    print()
    print("Using radix " + str(radix) + " and modulus " + str(modulus) + ".")
    print()
    print("Hash value | Occurences")
    print("-----------------------")

    hashes = []

    with open(fName) as file:
        for line in file:
            for word in line.strip().split(' '):
                if (word != ''):
                    hashes.append(hash(word, radix, modulus))
                    # print('{0:10s} {1:8d}'.format(word, hash(word, radix, modulus)))
    print()
    count = Counter(hashes)
    for val, cnt in count.items():
        print('{0:8d} {1:8d}'.format(val, cnt))


def run_man_test():
    while True:
        inp = input("Enter the radix, modulus, and file: ")
        r, m, f = inp.split(',')
        testHash(int(r), int(m), f.lstrip())


def run_auto_test(how):
    files = ["5lw-s.dat", "5lw-m.dat", "5lw.dat", "wordList"]
    radices = [128]
    moduli = [32, 127, 97]

    print("Starting auto test with the following values:\n")
    print("Files: " + str(files))
    print("Radices: " + str(radices))
    print("Moduli: " + str(moduli))

    for radix in radices:
        for mod in moduli:
            for file in files:
                file = "../Data files/" + file
                if(how == "test"):
                    testHash(radix, mod, file)
                elif(how == "count"):
                    count_hash(radix, mod, file)
                input()


if __name__ == "__main__":
    while True:
        print("Enter one of the following options to begin:")
        print("1. Run the auto test for hash")
        print("2. Run the auto count for hash")
        print("3. Run the manual test for hash")

        inp = int(input())

        if inp == 1:
            run_auto_test("test")
        elif inp == 2:
            run_auto_test("count")
        elif inp == 3:
            run_man_test()
        else:
            print("Please enter a valid option!")
