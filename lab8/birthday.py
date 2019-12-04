    
    

import sys
import string
import base64

import random
import string

from Crypto.Hash import SHA256

def raw2hex(raw):
    return raw.encode('hex')


def hex2raw(hexstring):
    return base64.b16decode(hexstring)

hexdigits = '0123456789ABCDEF'

def hash(message):
    h = SHA256.new()
    h.update(message)
    return h.digest()


def get_random_message():
    message = ''
    for _ in range(0, random.randint(4, 100)):
        if (random.choice([0, 1]) == 1):
            message += str(random.choice(string.digits))
        else:
            message += random.choice(string.letters)
    return message, message[0:4]

def main():
    # Try to find a collision on the first 4 bytes (32 bits)
    
    # Step 1. Generate 2^16 different random messages
    random_messages = []
    random_small_messages = []
    hashDict = {}
    for _ in range(pow(2,16)):
        m,smallm = get_random_message()
        random_messages.append(m)
        random_small_messages.append(smallm)
    
    # Step 2. Compute hashes
    random_hashes = []
    for _ in range(pow(2, 16)):
        m = random_small_messages[_]
        mhash = hash(m)
        random_hashes.append(mhash)

        if (mhash in hashDict and (hashDict[mhash])):
            hashDict[mhash].append(random_messages[_])
        else:
            hashDict[mhash] = [random_messages[_]]


    # Step 3. Check if there exist two hashes that match in the first
    # four bytes.
    
    # Step 3a. If a match is found, print the messages and hashes
    
    # Step 3b. If no match is found, repeat the attack with a new set
    # of random messages
    '''
    for i in range(0, pow(2, 16)):
        for j in range(0, pow(2, 16)):
            if i == j:
                continue
            if (random_messages[i] != random_messages[j]) and (random_hashes[i] == random_hashes[j]):
                print('Message #1: ' + random_messages[i])
                print('Message #2:' + random_messages[j])
    '''
    for key in hashDict:
        if len(hashDict[key]) > 1:
            print('key:' + key)
            print(hashDict[key])

if __name__ == "__main__":
    main()
