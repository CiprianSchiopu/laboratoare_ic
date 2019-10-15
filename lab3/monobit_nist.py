import math

import random


def get_random_string(n):  # generate random bit string
  bstr = bin(random.getrandbits(n)).lstrip('0b').zfill(n)
  return bstr

def monobit(bin_data):
    count = 0
    for char in bin_data:
        if char == '0':
            count -= 1
        else:
            count += 1
    sobs = count / math.sqrt(len(bin_data))
    p_val = math.erfc(math.fabs(sobs) / math.sqrt(2))
    return p_val


def bin2hex(bs):
  """
    Transform a bit string into a hex string
  """
  return hex(int(bs, 2))[2:-1]


def hex2bin(hs):
  """
    Transform a hex string (e.g. 'a2') into a string of bits (e.g.10100010)
  """
  bs = ''
  for c in hs:
    bs = bs + bin(int(c, 16))[2:].zfill(4)
  return bs


def main():
    ex1ciphertext = hex2bin(
        "a432109f58ff6a0f2e6cb280526708baece6680acc1f5fcdb9523129434ae9f6ae9edc2f224b73a8")
    print monobit(ex1ciphertext)

    randombinstr = get_random_string(1000)
    print(monobit(randombinstr))    

if __name__ == "__main__":
  main()
