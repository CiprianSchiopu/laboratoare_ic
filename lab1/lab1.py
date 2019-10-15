import binascii
alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_dec(letter, k = 3):
  if letter < 'A' or letter > 'Z':
    print 'Invalid letter'
    return
  else:
    return alphabet[(ord(letter) - ord('A') - k) % len(alphabet)]


def caesar_enc(letter, k=3):
    if letter < 'A' or letter > 'Z':
        print 'Invalid letter'
        return None
    else:
        return alphabet[(ord(letter) - ord('A') + k) % len(alphabet)]


def caesar_enc_string(plaintext, k=3):
    ciphertext = ''
    for letter in plaintext:
        ciphertext = ciphertext + caesar_enc(letter, k)
    return ciphertext


def caesar_dec_string(ciphertext, k=3):
    plaintext = ''
    for letter in ciphertext:
        plaintext = plaintext + caesar_dec(letter, k)
    return plaintext


def strxor(a, b):  # xor two strings (trims the longer input)
  return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])


def hexxor(a, b):  # xor two hex strings (trims the longer input)
  ha = a.decode('hex')
  hb = b.decode('hex')
  return "".join([chr(ord(x) ^ ord(y)).encode('hex') for (x, y) in zip(ha, hb)])


def bitxor(a, b):  # xor two bit strings (trims the longer input)
  return "".join([str(int(x) ^ int(y)) for (x, y) in zip(a, b)])


def str2bin(ss):
  """
    Transform a string (e.g. 'Hello') into a string of bits
  """
  bs = ''
  for c in ss:
    bs = bs + bin(ord(c))[2:].zfill(8)
  return bs


def hex2bin(hs):
  """
    Transform a hex string (e.g. 'a2') into a string of bits (e.g.10100010)
  """
  bs = ''
  for c in hs:
    bs = bs + bin(int(c, 16))[2:].zfill(4)
  return bs


def bin2hex(bs):
  """
    Transform a bit string into a hex string
  """
  return hex(int(bs, 2))[2:-1]


def byte2bin(bval):
  """
    Transform a byte (8-bit) value into a bitstring
  """
  return bin(bval)[2:].zfill(8)


def str2int(ss):
  """
    Transform a string (e.g. 'Hello') into a (long) integer by converting
    first to a bistream
  """
  bs = str2bin(ss)
  li = int(bs, 2)
  return li


def int2hexstring(bval):
  """
    Transform an int value into a hexstring (even number of characters)
  """
  hs = hex(bval)[2:]
  lh = len(hs)
  return hs.zfill(lh + lh % 2)


def bin2str(bs):
  """
    Transform a binary srting into an ASCII string
  """
  n = int(bs, 2)
  return binascii.unhexlify('%x' % n)


def main():
    m = 'BINEATIVENIT'
    c = caesar_enc_string(m)
    print c
  
    m2 = caesar_dec_string(c)
    print m2

    C1 = "000100010001000000001100000000110001011100000111000010100000100100011101000001010001100100000101"
    C2 = "02030F07100A061C060B1909"
  
    key = "abcdefghijkl"

    binkey = str2bin(key)
    m1bit = bitxor(C1, binkey)
    m1text = bin2str(m1bit)
    print m1text

    binc2 = hex2bin(C2)
    m2bit = bitxor(binc2, binkey)
    m2text = bin2str(m2bit)
    print m2text

if __name__ == "__main__":
    main()
