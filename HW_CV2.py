import cv2
import numpy as np

img = cv2.imread('pics/color_text.jpg')

new_image = np.zeros(img.shape, dtype='uint8')

# формат изображения
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# маска
mask = cv2.inRange(hsv, (0, 0, 0), (255, 255, 255))
img = cv2.bitwise_and(img, img, mask)
# print(mask)
img = cv2.GaussianBlur(img, (5, 5), 0)

# задаем точность обводки
img = cv2.Canny(img, 55, 55)

# определяем контуры
con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# рисуем контуры
cv2.drawContours(new_image, con, -1, (255, 100, 20), 1)
print(new_image.shape)

# определяем высоту, длину и каналы
ht, wt, chanel = new_image.shape

color_1 = [255, 100, 20]
color_2 = [20, 100, 255]
color_3 = [100, 20, 255]

for x in range(0, wt):
    for y in range(0, 165):
        yx = new_image[y, x]
        if not all(color_1 == yx):
            continue
        new_image[y, x] = color_2

    for y in range(303, ht):
        yx = new_image[y, x]
        if all(color_1 == yx):
            new_image[y, x] = color_3

cv2.imwrite('pics/result.jpg', new_image)
cv2.imshow('result', new_image)
cv2.waitKey(0)
