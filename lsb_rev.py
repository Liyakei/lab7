from PIL import Image
from bittools import *

def hamming_invert_bits_index(cont):
    buff = []

    H = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    for i in range(0,256): # по 4 бита из сообщения
        c_part = cont[i*15:(i+1)*15]
        Hc = [
            sum([H[0][e] * (c_part[e] % 2) for e in range(15)]) % 2,
            sum([H[1][e] * (c_part[e] % 2) for e in range(15)]) % 2,
            sum([H[2][e] * (c_part[e] % 2) for e in range(15)]) % 2,
            sum([H[3][e] * (c_part[e] % 2) for e in range(15)]) % 2
        ]

        ind = Hc[3]*8 + Hc[2]*4 + Hc[1]*2 + Hc[0]
        buff.append(ind + i*15)

    return buff

def lsb(cont,start=0,step=1):
    e=start
    result = []
    while True:
        result.append(cont[e] % 2)
        e+=1
        if len(result)>=len(met):
            tmp = result[-len(met):]
            if tmp == met:
                break
    return to_bytes(result[:-len(met)]).decode('cp1251')

def lsb3(cont,start=0,step=1):
    e=start
    result = []
    while True:
        result.append((cont[e//3] // 2**(e % 3)) % 2)
        e+=1
        if len(result)==200:
            print(result)
        if len(result)>=len(met):
            tmp = result[-len(met):]
            if tmp == met:
                break
    return to_bytes(result[:-len(met)]).decode('cp1251')

met = []
for i in "u98^%r*#8".encode('cp1251'):
    met.extend(to_bits(i))

print("\n\nLSBR_R1\n")
im = Image.open('LSBR_TEST_R1.bmp')
pix = im.load()
pixels = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y])
result = lsb(pixels)

print(result)


im.close()

print("\n\nLSBM_R1\n")
im = Image.open('LSBM_TEST_R1.bmp') # mushu.bmp
pix = im.load()
pixels = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y])
result = lsb(pixels)

print(result)


im.close()

print("\n\nLSBR_R0.25\n")
im = Image.open('LSBR_TEST_R1.bmp') # mushu.bmp
pix = im.load()
pixels = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y])
result = lsb(pixels,0,4)

print(result)


im.close()

print("\n\nLSBM_R0.25\n")
im = Image.open('LSBM_TEST_R1.bmp') # mushu.bmp
pix = im.load()
pixels = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y])
result = lsb(pixels,0,4)

print(result)


im.close()

print("\n\nLSBR_R3\n")
im = Image.open('LSBR_TEST_R3.bmp') # mushu.bmp
pix = im.load()
pixels = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y])
result = lsb3(pixels)

print(result)


im.close()

print("\n\nLSBM_R3\n")
im = Image.open('LSBM_TEST_R3.bmp') # mushu.bmp
pix = im.load()
pixels = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y])
result = lsb3(pixels)

print(result)


im.close()
