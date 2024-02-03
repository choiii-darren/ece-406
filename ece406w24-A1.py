"""
ECE406, Assignment 1.
Fill in these functions and submit on LEARN.
"""
#!/usr/bin/env python3
import math

# part (i) for modular exponentiation -- fill in the code below
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
    return y, x-math.floor(a/b)*y, d


def main():
    """
    Testing the two functions on a few inputs
    """
    # testing modular exponentiation
    if modexp(10, 1200, 14) == 8:
        print("modexp passed test 1")
    else:
        print("modexp failed test 1")

    # modexp -- test 2
    if modexp(325942, 25000000, 7) == 1:
        print("modexp passed test 2")
    else:
        print("modexp failed test 2")

    if modexp(32,21,15) == 2:
        print("modexp passed test 3")
    else:
        print("modexp failed test 3")

    if modexp(447, 3537, 4313) == 2583:
        print("modexp passed test 4")
    else:
        print("modexp failed test 4")

    if modexp(563,626,812) == 289:
        print("modexp passed test 5")
    else:
        print("modexp failed test 5")
    
    if modexp(839, 366, 142) == 107:
        print("modexp passed test 6")
    else:
        print("modexp failed test 6")

    # testing extended Euclid
    (x, y, d) = extended_euclid(125, 15)
    if d == 5 and x*125 + y*15 == d:
        print("extended_euclid passed test 1")
    else:
        print("extended_euclid failed test 1")

    # extended_euclid -- test 2
    (x, y, d) = extended_euclid(10203040, 20304)
    if d == 16 and x*10203040 + y*20304 == d:
        print("extended_euclid passed test 2")
    else:
        print("extended_euclid failed test 2")

    (x,y,d) = extended_euclid(46355, 62748)
    if d == 1 and x*46355 + y*62748 == d:
        print('extended euclid passed test 3')
    else:
        print("extended euclide failed test 3")
    
    (x,y,d) = extended_euclid(45107, 88064)
    if d == 43 and x*45107 + y*88064:
        print('extended euclid passed test 4')
    else:
        print("extended euclid failed test 4")

if __name__ == '__main__':
    main()
