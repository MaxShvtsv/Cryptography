import string

alphabet = string.ascii_uppercase
count = len(alphabet)

# Find A anb B
'''
/ y0 = x0 + A * 0 + B - first letter(p = 0)
\ y1 = x1 + A * 1 + B - second letter(p = 1)
    ||
    \/
/ y0 = x0 + B       => B = y0 - x0      !!!
\ y1 = x1 + A + B   => A = y1 - x1 - B  !!!
'''

plaintext = 'PATRIARCH OF DIESEL BAND'
cryptotext = 'UGAZRKCOU DV VBYNAI AAOF'

x0 = alphabet.index(plaintext[0])
x1 = alphabet.index(plaintext[1])
y0 = alphabet.index(cryptotext[0])
y1 = alphabet.index(cryptotext[1])

B = y0 - x0
A = y1 - x1 - B

print(f'A = {A}, B = {B}')