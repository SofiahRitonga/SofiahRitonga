import cv2

filepath = 'D:\BELAJAR NGODING\PENGOLAHAN CITRA\Picture\Portal.jpeg'
image = cv2.imread(filepath)
# .display.gambar
cv2.imshow('Sofiah', image)
cv2.waitKey(0)
output = 'D:\BELAJAR NGODING\PENGOLAHAN CITRA\Tutor Youtube\ Save Picture.jpg'
cv2.imwrite(output, image)
print("[INFO] Gambar telah tersimpan di {}".format(output))
