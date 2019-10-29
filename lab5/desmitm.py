import sys
import random
import string
from operator import itemgetter
import time
import bisect
from Crypto.Cipher import DES

def strxor(a, b): # xor two strings (trims the longer input)
  return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

def hexxor(a, b): # xor two hex strings (trims the longer input)
  ha = a.decode('hex')
  hb = b.decode('hex')
  return "".join([chr(ord(x) ^ ord(y)).encode('hex') for (x, y) in zip(ha, hb)])

def bitxor(a, b): # xor two bit strings (trims the longer input)
  return "".join([str(int(x)^int(y)) for (x, y) in zip(a, b)])

def str2bin(ss):
  """
    Transform a string (e.g. 'Hello') into a string of bits
  """
  bs = ''
  for c in ss:
    bs = bs + bin(ord(c))[2:].zfill(8)
  return bs

def str2int(ss):
  """
    Transform a string (e.g. 'Hello') into a (long) integer by converting
    first to a bistream
  """
  bs = str2bin(ss)
  li = int(bs, 2)
  return li

def hex2bin(hs):
  """
    Transform a hex string (e.g. 'a2') into a string of bits (e.g.10100010)
  """
  bs = ''
  for c in hs:
    bs = bs + bin(int(c,16))[2:].zfill(4)
  return bs

def bin2hex(bs):
  """
    Transform a bit string into a hex string
  """
  bv = int(bs,2)
  return int2hexstring(bv)

def byte2bin(bval):
  """
    Transform a byte (8-bit) value into a bitstring
  """
  return bin(bval)[2:].zfill(8)

def int2hexstring(bval):
  """
    Transform an int value into a hexstring (even number of characters)
  """
  hs = hex(bval)[2:]
  lh = len(hs)
  return hs.zfill(lh + lh%2)

def get_index(a, x):
  'Locate the leftmost value exactly equal to x in list a'
  i = bisect.bisect_left(a, x)
  if i != len(a) and a[i] == x:
    return i
  else:
    return -1

def des_enc(k, m):
  """
  Encrypt a message m with a key k using DES as follows:
  c = DES(k, m)

  Args:
    m should be a bytestring (i.e. a sequence of characters such as 'Hello' or '\x02\x04')
    k should be a bytestring of length exactly 8 bytes.

  Note that for DES the key is given as 8 bytes, where the last bit of
  each byte is just a parity bit, giving the actual key of 56 bits, as expected for DES.
  The parity bits are ignored.

  Return:
    The bytestring ciphertext c
  """
  d = DES.new(k)
  c = d.encrypt(m)

  return c

def des_dec(k, c):
  """
  Decrypt a message c with a key k using DES as follows:
  m = DES(k, c)

  Args:
    c should be a bytestring (i.e. a sequence of characters such as 'Hello' or '\x02\x04')
    k should be a bytestring of length exactly 8 bytes.

  Note that for DES the key is given as 8 bytes, where the last bit of
  each byte is just a parity bit, giving the actual key of 56 bits, as expected for DES.
  The parity bits are ignored.

  Return:
    The bytestring plaintext m
  """
  d = DES.new(k)
  m = d.decrypt(c)

  return m

def maninthemiddle(k1rest, k2rest, m, c):

  k1 = None
  k2 = None

  tb1 = []
  tb2 = []

  for i in range(0, 0xff):
    for j in range(0, 0xff):
      key = chr(i) + chr(j) + k2rest[2:]
      cipher = des_enc(key, m)
      tb1.append((key, cipher))

  for i in range(0, 0xff):
    for j in range(0, 0xff):
      key = chr(i) + chr(j) + k1rest[2:]
      plain = des_dec(key, c.decode('hex'))
      tb2.append((key, plain))

  tb2s = sorted(tb2, key = itemgetter(1))
  tenc2 = [value for _,value in tb2s]

  idx = -1
  keys = []
  print "key:"
  for (key, value) in tb1:
    idx = get_index(tenc2, value)

    if idx != -1:
      print(key, tb2[idx][0])

def des2_dec(key1, key2, ciphertext):
  k1_dec = des_dec(key1, ciphertext)
  plaintext = des_dec(key2, k1_dec)
  return plaintext

def des2_enc(key1, key2, m):
  k2_enc = des_enc(key2, m)
  return des_enc(key1, k2_enc)

def main():

  # Exercitiu pentru test des2_enc
  key1 = 'Smerenie'
  key2 = 'Dragoste'
  m1_given = 'Fericiti cei saraci cu duhul, ca'
  c1 = 'cda98e4b247612e5b088a803b4277710f106beccf3d020ffcc577ddd889e2f32'
  # TODO: implement des2_enc and des2_dec
  m1 = des2_dec(key1, key2, c1.decode('hex'))

  print 'ciphertext: ' + c1
  print 'plaintext: ' + m1
  print 'plaintext in hexa: ' + m1.encode('hex')

  # TODO: run meet-in-the-middle attack for the following plaintext/ciphertext
  m1 = 'Pocainta'
  c1 = '9f98dbd6fe5f785d' # in hex string
  m2 = 'Iertarea'
  c2 = '6e266642ef3069c2'
  
  # Note: you only need to search for the first 2 bytes of the each key:
  k1 = '??oIkvH5'
  k2 = '??GK4EoU'


  maninthemiddle(k1, k2, m1, c1)
  maninthemiddle(k1, k2, m2, c2)

if __name__ == "__main__":
  main()
