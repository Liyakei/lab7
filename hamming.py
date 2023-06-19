from PIL import Image
from bittools import *

# cont взятие изображения в виде списка пикселей
# mesbit сообщение которое необходимо скрыть в изображении
def hamming(cont,mesbit):

    H = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    for i in range(0,len(mesbit)//4): # функция разбивает сообщ по 4 бита и
        c_part = cont[i*15:(i+1)*15] # Для каждого фрагмента извлекается соответствующий контейнер,следующие 15 пикселей после предыдущего контейнера, и сохраняется в переменной `c_part`.
        Hc = [
            #  вычисление проверочной битовой последовательности
            sum([(H[0][e] * c_part[e]) % 2 for e in range(15)]) % 2,
            sum([(H[1][e] * c_part[e]) % 2 for e in range(15)]) % 2,
            sum([(H[2][e] * c_part[e]) % 2 for e in range(15)]) % 2,
            sum([(H[3][e] * c_part[e]) % 2 for e in range(15)]) % 2
              ]
#  в переменной `Hc` сохраняется проверочная битовая последовательность для текущего фрагмента.
 # s подследоват. содержит биты сообщения и проверочной последовательности.
        s = [
            (Hc[0] + mesbit[i * 4]) % 2,
            (Hc[1] + mesbit[i * 4 + 1]) % 2,
            (Hc[2] + mesbit[i * 4 + 2]) % 2,
            (Hc[3] + mesbit[i * 4 + 3]) % 2
        ]
        ind = s[3]*8 + s[2]*4 + s[1]*2 + s[0] - 1
        if ind!=-1:
            cont[i*15+ind] ^= 1

    return cont

im = Image.open('part.bmp')
mes = "".join(open("input.txt").readlines())
print(mes)
met = "u98^%r*#8"
mes = mes + met #метка окончания
q=mes.encode('cp1251')
bits = []
for i in q:
    bits.extend(to_bits(i))

print(bits)
# перебор всех пикселей изображения,
pix = im.load()
pixels=[]


for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y])
print(pixels[:150])
newpixels = hamming(pixels,bits)
print(newpixels[:150])
# newpix который содержит новое изображение, в котором каждый пиксель представляется кортежем из трех значений
newpix = [(newpixels[i],newpixels[i+1],newpixels[i+2]) for i in range(0,len(newpixels),3)]

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i]
#img.show()
img.save("HAMMING_15_11_TEST.bmp")
img.close()