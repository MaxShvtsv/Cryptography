import string

# A = {1, 2, 3, 4, 5}
# B = {1, 2, 3, 4, 5}
# C = {1, 2, 3, 4, 5}

def key(A, B, C, pos):
    return A * pos * pos + B * pos + C

alphabet = string.ascii_uppercase
count = len(alphabet)

# Decrypt

cryptotext = 'NLW IBU XPTU'
num = 1

for A in range(1, 6):
    for B in range(1, 6):
        for C in range(1, 6):
            plaintext = []

            for i in range(len(cryptotext)):
                if cryptotext[i] == ' ':
                    plaintext.append(' ')
                    continue

                sym = alphabet[(alphabet.index(cryptotext[i]) - key(A, B, C, i)) % count]
                plaintext.append(sym)

            plaintext = ''.join(plaintext)
            print(f'{num}. A = {A}, B = {B}, C = {C} : {plaintext}')
            num += 1