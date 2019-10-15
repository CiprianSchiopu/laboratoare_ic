import sys
import random
import string
import operator

#Parameters for weak LC RNG
class WeakRNG:
    "Simple class for weak RNG"
    def __init__(self):
        self.rstate = 0
        self.maxn = 255
        self.a = 0 #Set this to correct value
        self.b = 0 #Set this to correct value
        self.p = 257

    def init_state(self):
        "Initialise rstate"
        self.rstate = 0 #Set this to some value
        self.update_state()

    def update_state(self):
        "Update state"
        self.rstate = (self.a * self.rstate + self.b) % self.p

    def get_prg_byte(self):
        "Return a new PRG byte and update PRG state"
        b = self.rstate & 0xFF
        self.update_state()
        return b

def strxor(a, b): # xor two strings (trims the longer input)
  return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])

def hexxor(a, b): # xor two hex strings (trims the longer input)
  ha = a.decode('hex')
  hb = b.decode('hex')
  return "".join([chr(ord(x) ^ ord(y)).encode('hex') for (x, y) in zip(ha, hb)])
  
def main():

  #Initialise weak rng
  wr = WeakRNG()
  wr.init_state()

  #Print ciphertext
  CH = 'a432109f58ff6a0f2e6cb280526708baece6680acc1f5fcdb9523129434ae9f6ae9edc2f224b73a8'
  print "Full ciphertext in hexa: " + CH

  #Print known plaintext
  pknown = 'Let all creation'
  nb = len(pknown)
  print "Known plaintext: " + pknown
  pkh = pknown.encode('hex')
  print "Plaintext in hexa: " + pkh

  #Obtain first nb bytes of RNG
  gh = hexxor(pkh, CH[0:nb*2])
  print gh
  gbytes = []
  for i in range(nb):
    gbytes.append(ord(gh[2*i:2*i+2].decode('hex')))
  print "Bytes of RNG: "
  print gbytes

  #Break the LCG here:
  #1. find a and b
  #2. predict/generate rest of RNG bytes
  #3. decrypt plaintext

  for a in range(257):
    for b in range(257):
      isTrue = True
      for k in range(1,16):
        if gbytes[k] != (a * gbytes[k - 1] + b) % wr.p:
          isTrue = False
          break
      if isTrue:
        wr.a = a
        wr.b = b
        break
  print wr.a
  print wr.b


  print gbytes
  for i in range(16, len(CH) - 1):
    gbytes.append((wr.a * gbytes[i - 1] + wr.b) % wr.p)

  # Print full plaintext
  print gbytes
  p = ''

  for i in range(len(gbytes)):
    p += chr(gbytes[i])
  
  p = p.encode('hex')

  p = hexxor(CH, p)

  p = p.decode('hex')

  print "Full plaintext is: " + p



if __name__ == "__main__":
  main()  