'''
    An implementation of a hash function
'''


def hash(inStr, radix, modulus):
    '''
        Complete the implementation of the method hash(); be sure to
        uncomment the value returned!

        Use (ord)inStr[i] to convert the character at position i
        to the integer value of its ASCII code.

        NOTE that the indexing of the characters in a Python string is reversed
        from what we used in lecture.
    '''
    hashValue = 0
    for i in range(len(inStr)):
        hashValue = (hashValue * radix + ord(inStr[i])) % modulus

    return hashValue
