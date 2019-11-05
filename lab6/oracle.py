#!/usr/bin/env python

import random
import sys
from Crypto.Cipher import AES

BLOCK_SIZE = 16
IV = 'Happy Halloween!'


def strxor(a, b):  # xor two strings (trims the longer input)
  return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

def blockify(text, block_size=BLOCK_SIZE):
    return [text[i:i+block_size] for i in range(0, len(text), block_size)]

def validate_padding(padded_text):
    return all([n == padded_text[-1] for n in padded_text[-ord(padded_text[-1]):]])

def pkcs7_pad(text):
    length = BLOCK_SIZE - (len(text) % BLOCK_SIZE)
    text += chr(length) * length
    return text

def pkcs7_depad(text):
    if not validate_padding(text):
        return None
    return text[:-ord(text[-1])]

def aes_dec_cbc(k, c, iv):
    """
    Decrypt a ciphertext c with a key k in CBC mode using AES as follows:
    m = AES(k, c)

    Args:
      c should be a bytestring (i.e. a sequence of characters such as 'Hello...' or '\x02\x04...')
      k should be a bytestring of length exactly 16 bytes.
      iv should be a bytestring of length exactly 16 bytes.

    Return:
      The bytestring message m
    """
    aes = AES.new(k, AES.MODE_CBC, iv)
    m = aes.decrypt(c)
    depad_m = pkcs7_depad(m)

    return depad_m

def check_cbcpad(c, iv):
    """
    Oracle for checking if a given ciphertext has correct CBC-padding.
    That is, it checks that the last n bytes all have the value n.

    Args:
      c is the ciphertext to be checked.
      iv is the initialization vector for the ciphertext.
      Note: the key is supposed to be
      known just by the oracle.

    Return 1 if the pad is correct, 0 otherwise.
    """

    key = "za best key ever"

    if aes_dec_cbc(key, c, iv) != None:
        return 1

    return 0

def numberify(characters):
    """ Transforms a string into a list of integers. Note: ASCII text required. E.g. ctext.decode('hex') """
    return map(lambda x: ord(x), characters)

def stringify(numbers):
    """ Transfoms a list of integers into a string """
    return "".join(map(lambda x: chr(x), numbers))

if __name__ == "__main__":
    ctext = "f5b376080831f2b262fd204ca865b740c67b5a5456a2653dfee2bb8e7c9b81a8be5a1b57645d3b98f2e191e897e8fcf98ddd2005628243a8315be785c870eecc7c60ba1cf6bd4b7fa6a9e9dbbeabf24fc9f7140791f7d13539082bf590393aa3"
    iv = numberify(IV)
    ct = ctext.decode('hex')
    cc = [ct[0:16], ct[16:32], ct[32:48], ct[48:64]]
    ciphertext = numberify(ctext.decode('hex'))
    blocks = blockify(ciphertext)
    cleartext = []
    

    # TODO: implement the CBC-padding attack to find the message corresponding to the above ciphertext
    # Note: you cannot use the key known by the oracle
    # You can use the known IV in order to recover the full message

    for k in range(4):
        r = "radoirazvanbogd"
        buf = ''
        found = True

        for j in range(16):
            found = False

            for i in range(0, 256):
                cs = r[:(15 - j)] + chr(i) + strxor(buf, chr(j + 1) * len(buf)) + cc[k]

                if check_cbcpad(cs, IV) == 1:
                    found = True
                    buf = strxor(chr(i), chr(j + 1)) + buf
                    break

            if found:
                j += 1
            else:
                j -= 1
                buf = buf[1:]

        if k == 0:
            print strxor(IV, buf)
        else:
            print strxor(cc[k - 1], buf)
