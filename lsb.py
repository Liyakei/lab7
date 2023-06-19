from PIL import Image
from bittools import *
from random import choice
# замена наименее значащих битов в пикселях изображения на биты скрываемой информации
def lsbr(cont,mesbit,start=0,step=1):
    e = start
    for i in mesbit:
        cont[e] ^= cont[e] % 2 #Обнуляем последний бит
        cont[e] ^= i           #Заменяем бит на бит из сообщения
        e+=step
    return cont

def lsbm(cont,mesbit,start=0,step=1):
    e = start
    for i in mesbit:
        if cont[e] % 2 != i:
            cont[e] += choice([-1,1])
        e+=step
    return cont

def lsbr3(cont,mesbit,start=0,step=1):
    e = start
    for i in mesbit:
        if e % 3 == 0:
            cont[e//3] -= cont[e//3] % 8  #Обнуляем три последних бита
        cont[e//3] ^= i * 2**(e % 3)           #Заменяем бит на бит из сообщения
        e+=step
    return cont

def lsbm3(cont,mesbit,start=0,step=1):
    e = start
    for i in mesbit:
        if cont[e//3] // 2**(e % 3) % 2 != i:
            cont[e//3] += choice([-1,1]) * 2**(e % 3) # добавляем или вычитаем случайное значение -1 или 1,
        e+=step
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

pix = im.load()
pixels=[]


for x in range(im.size[0]):
    for y in range(im.size[1]):
        pixels.extend(pix[x,y]) #Значения RGB текущего пикселя считываются с помощью функции

newpixels = lsbr(pixels,bits) #скрытие битов сообщения в каждом пикселе изобр

newpix = [(newpixels[i],newpixels[i+1],newpixels[i+2]) for i in range(0,len(newpixels),3)]

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i] #присваивание соответ цвета из newpix пикселю в новом изображении
#img.show()
img.save("LSBR_TEST_R1.bmp")

newpixels = lsbm(pixels,bits)

#кортеж из трех элементов
newpix = [(newpixels[i],newpixels[i+1],newpixels[i+2]) for i in range(0,len(newpixels),3)]

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBM_TEST_R1.bmp")

newpixels = lsbr(pixels,bits,0,4)

newpix = [(newpixels[i],newpixels[i+1],newpixels[i+2]) for i in range(0,len(newpixels),3)]

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBR_TEST_R0.25.bmp")

newpixels = lsbm(pixels,bits,0,4)

newpix = [(newpixels[i],newpixels[i+1],newpixels[i+2]) for i in range(0,len(newpixels),3)]

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBM_TEST_R0.25.bmp")

newpixels = lsbr3(pixels,bits)

newpix = [(newpixels[i],newpixels[i+1],newpixels[i+2]) for i in range(0,len(newpixels),3)]

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBR_TEST_R3.bmp")

newpixels = lsbm3(pixels,bits)

newpix = [(newpixels[i],newpixels[i+1],newpixels[i+2]) for i in range(0,len(newpixels),3)]

img = Image.new(im.mode, im.size)
pixelsNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixelsNew[i,j] = newpix[j + img.size[1] * i]
#img.show()
img.save("LSBM_TEST_R3.bmp")


im.close()
img.close()