from PIL import Image
from bittools import *

def hamming(cont):

    H = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    buff=[]
    i=0
    while True: # по 4 бита из сообщения
        c_part = cont[i*15:(i+1)*15]
        Hc = [
            sum([H[0][e] * (c_part[e] % 2) for e in range(15)]) % 2,
            sum([H[1][e] * (c_part[e] % 2) for e in range(15)]) % 2,
            sum([H[2][e] * (c_part[e] % 2) for e in range(15)]) % 2,
            sum([H[3][e] * (c_part[e] % 2) for e in range(15)]) % 2
              ]
        buff.extend(Hc)
        if len(buff) % 8 == 0:
            if len(buff) >= len(met):
                if buff[-len(met):] == met:
                    result = to_bytes(buff[:-len(met)])
                    break
        i+=1

    return result.decode('cp1251')

met = []
for i in "u98^%r*#8".encode('cp1251'):
    met.extend(to_bits(i))

print("HAMMING\n")
im = Image.open('HAMMING_15_11_TEST.bmp') # mushu.bmp
pix = im.load()
pixels = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y])
result = hamming(pixels)

print(result)


im.close()