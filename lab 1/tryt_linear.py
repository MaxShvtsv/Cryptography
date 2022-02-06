import string

A = 1
B = 5

def key(pos):
    return A * pos + B 

alphabet = string.ascii_uppercase
count = len(alphabet)

# Encrypt

plaintext = 'PATRIARCH OF DIESEL BAND'
cryptotext = []

for i in range(len(plaintext)):
    if plaintext[i] == ' ':
        cryptotext.append(' ')
        continue

    sym = alphabet[(alphabet.index(plaintext[i]) + key(i)) % count]
    cryptotext.append(sym)

cryptotext = ''.join(cryptotext)
print(cryptotext)
