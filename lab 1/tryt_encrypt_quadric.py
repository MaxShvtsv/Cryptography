import string

A = 1
B = 2
C = 3

def key(pos):
    return A * pos * pos + B * pos + C

alphabet = string.ascii_uppercase
count = len(alphabet)

# Encrypt

plaintext = 'HELLO'
cryptotext = []

for i in range(len(plaintext)):
    if plaintext[i] == ' ':
        cryptotext.append(' ')
        continue

    sym = alphabet[(alphabet.index(plaintext[i]) + key(i)) % count]
    cryptotext.append(sym)

cryptotext = ''.join(cryptotext)
print(cryptotext)