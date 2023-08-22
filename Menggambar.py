from tkinter import CENTER, Canvas
from turtle import color
import cv2
import numpy as np

Canvas = np.zeros((300, 300, 3), dtype='uint8')

hijau = (0, 255, 0)
cv2.line(Canvas, (0, 0), (300, 300), hijau)
cv2.imshow("Canvas", Canvas)
cv2.waitKey(0)

merah = (0, 0, 255)
cv2.line(Canvas, (300, 0), (0, 300), merah, 3)
cv2.imshow("canvas", Canvas)
cv2.waitKey(0)

biru = (225, 0, 0)
cv2.rectangle(Canvas, (10, 10), (60, 60), biru, 1)
cv2.imshow("Canvas", Canvas)
cv2.waitKey(0)

cv2.rectangle(Canvas, (50, 200), (200, 225), merah, 5)
cv2.imshow("Canvas", Canvas)
cv2.waitKey(0)

cv2.rectangle(Canvas, (200, 50), (225, 155), biru, -1)
cv2.imshow("Canvas", Canvas)
cv2.waitKey(0)


Canvas = np.zeros((300, 300, 3), dtype='uint8')
centerX, centerY = Canvas.shape[1] // 2, Canvas.shape[0] // 2
putih = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(Canvas, (centerX, centerY), r, putih)
cv2.imshow("Canvas", Canvas)
cv2.waitKey(0)

Canvas = np.zeros((300, 300, 3), dtype='uint8')
for i in range(0, 25):
    r = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    pt = np.random.randint(0, high=300, size=(2,)).tolist()

    cv2.circle(Canvas, tuple(pt), r, color, -1)
cv2.imshow("Canvas", Canvas)
cv2.waitKey(0)
