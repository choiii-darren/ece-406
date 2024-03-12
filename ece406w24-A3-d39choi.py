#!/usr/bin/env python3
"""
ECE 406:  File for Exercise 1 of Assignment #3
"""
import numpy.fft as np


################################################################################
# student info
#
<<<<<<< HEAD:ece406w24-A3-d39choi.py
# WatIAM username: d39choi
=======
# WatIAM username: d39choi  
>>>>>>> 710208d11f1f71217803cad6181a8777e076ddaa:ece406w24-A3-d39choi.py
# Student number: 20876806
################################################################################


def main():
    """
    Exercise 1:  Using the FFT to multiply two binary numbers.
    You just need to fill in parts (v) and (vi)
    """
    # The binary numbers and their product
    a_bin = 0b110000001101
    b_bin = 0b100011110001
    c_bin = a_bin * b_bin
    print('The product of a and b is', c_bin)


    # (i) The coefficients of the polynomials A and B
    Acoeff = [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1]
    Bcoeff = [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1]


    # (ii) the value representations of A and B
    Aval = np.fft(Acoeff, 32)
    Bval = np.fft(Bcoeff, 32)


    # (iii) The value representation of C
    Cval = []
    for i in range(len(Aval)):
        Cval.append(Aval[i] * Bval[i])

    # (iv) The coefficients of the polynomial C
    Ccoeff = np.ifft(Cval)
    # we'll get rid of the imaginary parts, which are just numerical errors
    for i, c in enumerate(Ccoeff):
        Ccoeff[i] = int(round(c.real))
    # print(Ccoeff)
    # NOTE: Because we are taking the FFT on 12-bit numbers using the 32-th roots
    #       of unity, the polynomial coefficients (Ccoeff) can be numbers 
    #       other than 0 and 1. Don't be alarmed by this: this polynomial will
    #       sill produce the correct answer c = C(2)


    # (v) calculate the product by evaluating the polynomial at 2, i.e., C(2)
    # (You may need to take the real part at the end if there is a small imaginary component)
    prod = 0
    # TODO: write some code to produce the proper value of prod as an integer
    for i in range(len(Ccoeff)):
        prod += Ccoeff[i]*(2**i)
    print('Using the FFT the product of a and b is', int(round(prod.real)))

    
    # (vi) write code to calculate the binary digits of c directly from the coefficients of C, Ccoeff.
    # TODO: use Coeff to produce an array of {0, 1} values that represent the binary values of c
    bitArray = []
    carry = 0
    lastSigBit = 0
    for i in range(len(Ccoeff)):
        addBit = carry + int(round(Ccoeff[i].real))
        carry = addBit // 2
        addBit = addBit % 2
        bitArray.append(str(addBit))
        if addBit == 1:
            lastSigBit = i
    if carry != 0:
        bitArray.append(str(addBit))
        lastSigBit += 1
    print(''.join(bitArray[:lastSigBit+1]))





if __name__ == '__main__':
    main()
