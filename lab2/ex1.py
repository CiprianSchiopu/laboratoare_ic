from caesar import *

ciphertexts = [
	"LDPWKHORUGBRXUJRG",
	"XNTRGZKKGZUDMNNSGDQFNCRADENQDLD",
	"DTZXMFQQSTYRFPJDTZWXJQKFSDLWFAJSNRFLJ",
	"SIOMBUFFHINNUEYNBYHUGYIZNBYFILXSIOLAIXCHPUCH",
	"ERZRZOREGURFNOONGUQNLGBXRRCVGUBYL",
	"CJIJPMTJPMAVOCZMVIYTJPMHJOCZM",
	"DTZXMFQQSTYRZWIJW",
	"ZPVTIBMMOPUDPNNJUBEVMUFSZ",
	"FVBZOHSSUVAZALHS",
	"KAGETMXXZAFSUHQRMXEQFQEFUYAZKMSMUZEFKAGDZQUSTNAGD",
	"MCIGVOZZBCHRSGWFSOBMHVWBUHVOHPSZCBUGHCMCIFBSWUVPCIF" 
]

def decrypt(ciphertext):
    found = False
    plaintext = ''
    for i in range(1,26):
		plausiblePlaintext = caesar_dec_string(ciphertext, i)
		if (plausiblePlaintext.upper().find('YOU') > -1
		or plausiblePlaintext.upper().find('SABBATH') > -1):
			plaintext = plausiblePlaintext
			found = True
			break

    return plaintext

def main():
    for c in ciphertexts:
        print decrypt(c)

if __name__ == "__main__":
  main()

