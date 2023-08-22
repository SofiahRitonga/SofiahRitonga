import cv2
from cv2 import waitKey

# imread adalah fungsi untuk membaca citra digital dari komputer
citra = cv2.imread('D:\BELAJAR NGODING\PENGOLAHAN CITRA\Picture\Portal.jpeg')

# Menampilkan citra digital yang sudah dibaca
# winname adalah nama gambar dan matriks adalah citra
cv2.imshow('Sofiah Ritonga', citra)
cv2.imshow('BLUE', citra[:, :, 0])
cv2.imshow('GREEN', citra[:, :, 1])
cv2.imshow('RED', citra[:, :, 2])

# Menampilkan matriks dari citra
# Python membaca BGR yg awalnya RGB
# Channel warna : 0 = BLUE , 1 = GREEN, 2 = RED
print(citra[:, :, 0])
print(citra[:, :, 1])
print(citra[:, :, 2])

# Menunggu user menekan sembarang tombol
cv2.waitKey()
