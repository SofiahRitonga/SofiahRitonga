import cv2
import numpy as np

# imread adalah fungsi untuk membaca citra digital dari komputer
citra = cv2.imread('D:\BELAJAR NGODING\PENGOLAHAN CITRA\Picture\Portal.jpeg')

# Membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b = citra[:, :, 0]
g = citra[:, :, 1]
r = citra[:, :, 2]

# len adalah panjang
# Menyimpan jumlah baris dan kolom dari citra
jum_baris = len(citra)
jum_kolom = len(citra[0])

# Menyiapkan citra baru dengan 0
citra_gray = np.zeros((jum_baris, jum_kolom))

# Menghitung nilai pixel gray
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_gray[i, j] = round(
            0.299 * r[i, j] + 0.587 * g[i, j] + 0.114 * b[i, j])

citra_gray = citra_gray.astype(np.uint8)
cv2.imshow('Sofiah gray', citra_gray)
print(citra_gray)
cv2.waitKey()

# Cara cepatnya
#citra_gray = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Sofiah rgb', citra)
#cv2.imshow('Sofiah gray', citra_gray)
# b,g,r =cv2.split(citra) ==> Untuk mensplit channel warna dengan 1 baris
