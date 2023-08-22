import cv2

image = cv2.imread('D:\BELAJAR NGODING\PENGOLAHAN CITRA\Picture\Portal.jpeg')
face = cv2.CascadeClassifier(
    'D:\BELAJAR NGODING\PENGOLAHAN CITRA\Tutor Youtube\eye-detection.xml')
eye = cv2.CascadeClassifier(
    'D:\BELAJAR NGODING\PENGOLAHAN CITRA\Tutor Youtube\eye-detection.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
wajah = face.detectMultiScale(gray, 1.3, 5)
for (v, x, y, z) in wajah:
    cv2.rectangle(image, (v, x), (v + y, x + z), (0, 255, 0), 2)
    cv_warna = image[v:v + z, v: v + y]

cv2.imshow('Sofiah', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
