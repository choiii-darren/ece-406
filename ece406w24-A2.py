#!/usr/bin/env python3
"""
Assignment 2 Python file
Copy-and-paste your extended_euclid and modexp functions
from assignment 1
"""
import random
import math


# TODO: Add implementations of modexp and extended_euclid (you can resuse your code from A1).
def modexp(x, y, N):
    """
    Input: Three positive integers x and y, and N.
    Output: The number x^y mod N
    """

    if y == 0:
        return 1
    z = modexp(x, math.floor(y/2), N)
    if f"{y:b}"[-1] == '0':
        return (z*z) % N
    else:
        return (x * z * z) % N


# part (ii) for extended Euclid  -- fill in the code below
def extended_euclid(a, b):
    """
    Input: Two positive integers a >= b >= 0
    Output: Three integers x, y, and d returned as a tuple (x, y, d)
            such that d = gcd(a, b) and ax + by = d
    """
    if b == 0:
        return (1,0,a)
    (x,y,d) = extended_euclid(b, a % b)
    return y, x-(a//b)*y, d


def primality(N):
    """
    Test if a number N is prime using Fermat's little Theorem with
    ten random values of a.  If a^(N-1) mod N = 1 for all values,
    then return true.  Otherwise return false.
    Hint:  you can generate a random integer between a and b using
    random.randint(a,b).
    """
    # TODO: Implement a True/False test for primality of an input number N.
    testing = []
    while len(testing) != 10:
        num = random.randint(2, N)
        if num % N == 0:
            continue
        else:
            testing.append(num)
    for num in testing:
        if num**(N-1)%N == 1:
            continue
        else:
            return False
    return True


def prime_generator(N):
    """
    This function generates a prime number <= N
    """
    # TODO: Implement a prime number generator.
    while True:
        number = random.randint(2,N)
        # print('trying ', number)
        if primality(number):
            return number
    # return 0


def main():
    """
    Generate RSA private/public key, then encode and decode a message.
    """
    random.seed()
    ## A2Q1:  generating primes and RSA
    ##################
    # for i in range(5):
    #     print(prime_generator(3000))
    # print(primality(59))
    e = 5 #multiplicatve exponent
    while True:
        p = prime_generator(10000000)
        q = prime_generator(10000000)
        (x,y,d) = extended_euclid(e, ((q-1)*(p-1)))
        if d == 1:
            break
    # print(p,q)
    N = p * q
    e = 5
    message = 2148321
    # message = 30
    print("p:", p, ' q: ', 'q')
    (x,y,d) = extended_euclid(((q-1)*(p-1)),e)
    # print(x,y,d)
    mult_inverse = y % ((p-1)*(q-1)) # multiplicative inverse
    print(mult_inverse)
    # print((e*mult_inverse)-1, ((q-1)*(p-1)))
    if (e * mult_inverse - 1 ) % (p-1)*(q-1) == 0:
        print('divisible')
    # print(message,e,N)
    encoded = modexp(message,e,N)
    print('encoded: ',encoded)
    decoded_message = modexp(encoded, mult_inverse , N)
    print('decoded: ', decoded_message)
    # TODO: Complete this main() function.
    #       You should use print statements to show that your code completes the 
    #       instructions from parts iii--vi.

if __name__ == '__main__':
    main()