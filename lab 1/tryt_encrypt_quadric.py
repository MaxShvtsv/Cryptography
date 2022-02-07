import string

A = 5
B = 1
C = 2

def key(pos):
    return A * pos * pos + B * pos + C

alphabet = string.ascii_lowercase
count = len(alphabet)

# Encrypt

plaintext = 'king of slaves'
cryptotext = []

for i in range(len(plaintext)):
    if plaintext[i] == ' ':
        cryptotext.append(' ')
        continue

    sym = alphabet[(alphabet.index(plaintext[i]) + key(i)) % count]
    cryptotext.append(sym)

cryptotext = ''.join(cryptotext)
print(cryptotext)