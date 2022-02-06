import string

alphabet =  string.ascii_lowercase
count = len(alphabet)

# Decrypt

cryptotext = 'xn anx ufhjr ufwf gjqqzr'

for i in range(count):
    plaintext = []

    for j in range(len(cryptotext)):
        if cryptotext[j] == ' ':
            plaintext.append(' ')
            continue

        sym = alphabet[(alphabet.index(cryptotext[j]) - i) % count]
        plaintext.append(sym)

    plaintext = ''.join(plaintext)
    print(f'{i} {plaintext}')