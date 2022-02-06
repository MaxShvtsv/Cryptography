import string

alphabet =  string.ascii_lowercase
count = len(alphabet)
key = 4

# Encrypt

plaintext = 'you my heart you my soul'

cryptotext = []

for i in range(len(plaintext)):
    if plaintext[i] == ' ':
        cryptotext.append(' ')
        continue

    sym = alphabet[(alphabet.index(plaintext[i]) + key) % count]
    cryptotext.append(sym)

cryptotext = ''.join(cryptotext)
print(cryptotext)