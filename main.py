from PIL import Image
import random

im = Image.open('your_image.png')
pixelMap = im.load()
pixelValues_base = list(im.getdata())
pixelValues = [[] for _ in range(im.size[1])]
j = 0
for i in range(len(pixelValues_base)):
    if i % im.size[0] == 0 and i != 0:
        j += 1
    pixelValues[j].append(pixelValues_base[i])
print(pixelValues)

img = Image.new(im.mode, im.size)
pixelsNew = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1] - 1, 0, -1):
        if pixelValues[j][i] == (0, 0, 0):
            pixelsNew[i, j] = (255, 255, 255)
        else:
            pixelsNew[i, j] = (0, 0, 0)

img.show()
