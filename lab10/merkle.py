    
    

import random
import string
from Crypto.Cipher import AES
import os
  
def aes_enc(k, m):
  """
  Encrypt a message m with a key k in ECB mode using AES as follows:
  c = AES(k, m)

  Args:
    m should be a bytestring multiple of 16 bytes (i.e. a sequence of characters such as 'Hello...' or '\x02\x04...')
    k should be a bytestring of length exactly 16 bytes.

  Return:
    The bytestring ciphertext c
  """
  aes = AES.new(k)
  c = aes.encrypt(m)

  return c

def aes_dec(k, c):
  """
  Decrypt a ciphertext c with a key k in ECB mode using AES as follows:
  m = AES(k, c)

  Args:
    c should be a bytestring multiple of 16 bytes (i.e. a sequence of characters such as 'Hello...' or '\x02\x04...')
    k should be a bytestring of length exactly 16 bytes.

  Return:
    The bytestring message m
  """
  aes = AES.new(k)
  m = aes.decrypt(c)

  return m

alice_keys = []
bob_key = []

# TODO This is Alice. She generates 2^16 random keys and 2^16 puzzles.
# A puzzle has the following formula:
# puzzle[i] = aes_enc(key = 0..0 + i, plaintext ="Puzzle" + chr(i) + chr(j) + alice_keys[i])
# This function shall fill in the alice_keys list and shall return a list of 2^16 puzzles.
def gen_puzzles():
  # TODO
  keys = []
  puzzles = []
  for i in range(256):
    for j in range(256):
      alice_key = os.urandom(8)
      enc = aes_enc("\xAA" * 14 + chr(i) + chr(j),
                    "Puzzle" + chr(i) + chr(j) + alice_key)
      puzzles.append(enc)
      alice_keys.append(alice_key)
  return puzzles

# TODO This is Bob. He tries to solve one random puzzle. His purpose is to solve one random puzzle
# offered by Alice.
# This function shall fill in the bob_key list with the secret discovered by Bob.
# The function shall return the index of the chosen puzzle.
def solve_puzzle(puzzles):
  # TODO
  k = random.randint(0, 255)  # doamne ajuta
  l = random.randint(0, 255)  # doamne ajuta++
  for i in range(256):
    for j in range(256):
      s = aes_dec("\xAA" * 14 + chr(k) + chr(l), puzzles[i * 256 + j])
      if s[0:6] == "Puzzle":
        bob_key.append(s[8:])
        return i * 256 + j


def main():
  # Alice generates some puzzles
  puzzles = gen_puzzles()
  # Bob solves one random puzzle and discovers the secret
  x = solve_puzzle(puzzles)
  print "Bob's secret key: " + bob_key[0]
  # Alice receives the puzzle index from Bob and now knows the secret
  print "Alice's secret key: " + alice_keys[x]
  # The secret should be the same, even if it was not explicitly shared
  if bob_key[0] == alice_keys[x]:
    print ":)"
  else:
    print ":("

if __name__ == "__main__":
  main()
