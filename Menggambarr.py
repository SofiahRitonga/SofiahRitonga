from tkinter import Canvas
import cv2
import numpy as np
canvas = cv2.imread('D:\BELAJAR NGODING\PENGOLAHAN CITRA\Picture\Portal.jpeg')

cv2.rectangle(canvas, (91, 25), (242, 228), (0, 255), 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
