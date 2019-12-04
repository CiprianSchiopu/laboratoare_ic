#!/usr/bin/env python 

from Crypto.PublicKey import RSA
import base64
import struct
import math
from Crypto.Cipher import PKCS1_OAEP
import binascii
from decimal import *
from math import ceil, floor, log

private = RSA.generate(1024)
public  = private.publickey()

def oracle(msg):
    # TODO - oracle
    return (private.decrypt(msg) % 2 == 0)

def attack(ciphertext, n):
    # TODO - attack
    e = private.e

    enctwo = pow(2, e, n)

    lb = Decimal(0)
    ub = Decimal(n)

    k = int(ceil(log(n, 2)))  # n. of iterations
    getcontext().prec = k

    for i in range(1, k + 1):
        ciphertext = (ciphertext * enctwo) % n
        
        nb = (lb + ub) / 2
        
        if oracle(ciphertext):
            ub = nb
        else:
            lb = nb

    return (hex(int(ub)) + hex(int(lb)))

    
def main():
    textb64 = 'VGhhdCdzIHdoeSBJIGZvdW5kIHlvdSBkb24ndCBwbGF5IGFyb3VuZCB3aXRoIHRoZSBGdW5reSBDb2xkIE1lZGluYQ=='
    plaintext = base64.b64decode(textb64)
    ciphertext = int(public.encrypt(plaintext, 32)[0].encode('hex'), 16)
    
    plaintext_obtained = attack((ciphertext * 2**public.e) % public.n, public.n)
    
    print bytearray.fromhex('{:x}'.format(plaintext_obtained))
    #print plaintext


if __name__ == "__main__": main()
