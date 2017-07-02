'''
   A program to test hash function variations
'''
from collections import Counter
import statistics as stats
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

    f = open("../Data files/results.dat", 'w')

    for val, cnt in count.items():
        f.write('{0:8d} {1:8d}\n'.format(val, cnt))
        print('{0:8d} {1:8d}'.format(val, cnt))

    # print(get_avg_collision(count))
    print_stats(count.values())
    f.close()
    return count


def run_man_test(how):
    while True:
        inp = input("Enter the radix, modulus, and file: ")
        r, m, f = inp.split(',')
        if(how == "test"):
            testHash(int(r), int(m), f.lstrip())
        elif(how == "count"):
            count_hash(int(r), int(m), f.lstrip())


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


def find_best_prime():
    file = "../Data files/5lw.dat"
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
              61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]

    for rdx in primes:
        for mod in primes:
            count = count_hash(rdx, mod, file)
            avg = get_avg_collision(count)
            print('radix: {0:8d}, modulus: {1:8d} => {2: 8f}'
                  .format(rdx, mod, avg))


def print_stats(list):
    print('Mean : {0:f}'.format(stats.mean(list)))
    print('StDev: {0:f}'.format(stats.stdev(list)))
    print('Var  : {0:f}'.format(stats.variance(list)))



def get_avg_collision(count):
    sum = 0
    # print('values: {0:s}'.format(str(count.values())))
    for val, cnt in count.items():
        print(cnt)
        sum += cnt

    return sum / len(count)




if __name__ == "__main__":
    while True:
        print("Enter one of the following options to begin:")
        print("1. Run the auto test for hash")
        print("2. Run the auto count for hash")
        print("3. Run the manual test for hash")
        print("4. Run the manual count for hash")

        inp = int(input())

        if inp == 1:
            run_auto_test("test")
        elif inp == 2:
            run_auto_test("count")
        elif inp == 3:
            run_man_test("test")
        elif inp == 4:
            run_man_test("count")
        elif inp == 5:
            find_best_prime()
        else:
            print("Please enter a valid option!")
