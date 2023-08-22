import cv2
import numpy as np

width = 0
height = 0
nilai_counter = 0
MinCountourArea = 3000  # Adjust the velue according to your usage
BinarizationThreshold = 70  # Adjust the velue according to your usage
OffsetRefLines = 150
Banyak_Objek = 0
Logic = True
Test_Nilai = 0


vid_capture = cv2.VideoCapture("C:\Users\acer\Documents\Bandicam\CODINGAN.mp4")

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read()
    if ret == True:
        # *DETEKSI WARNA BIRU
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        biru_lower = np.array([100, 150, 0], np.uint8)
        biru_upper = np.array([140, 255, 255], np.uint8)
        biru = cv2.inRange(hsv, biru_lower, biru_upper)

        kernel = np.ones[(7, 7), "uint8"]
        blue = cv2.dilate(biru, kernel)
        res = cv2.bitwise_and(frame, frame, mask=blue)
        width = vid_capture.get(3)
        height = vid_capture.get(4)

        # *COUNTER
        (_, contours, hierarchy) = cv2.findContours(
            blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 900):
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                centre_of_circle = (x+int(w/2), y+int(h/2))
                cv2.circle(frame, centre_of_circle, 1, (0, 0, 255), 2)
                if((x+int(w/2)) > int(width/2)) and ((x+int(w/2)) < (int(width/2)+5) and Logic == True):
                    nilai_counter += 1
                    if(nilai_counter > 0):
                        Banyak_Objek += 1
                        Logic = False

                if(Logic == False and (x+int(w/2)) > (int(width/2)+5)):
                    if(nilai_counter > 0):
                        nilai_counter = 0
                        Logic = True
        start_point1 = (int(width/2), 0)
        end_point1 = (int(width/2), int(height))
        cv2.line(frame, start_point1, end_point1, (0, 255, 0), 2)
        hitung = "Jumlah Barang = |0|" .format(Banyak_Objek)
        cv2.putText(frame, hitung, (0, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 2, cv2.Line_AA)

        # *TAMPILAN VIDEO
        cv2.imshow('Frame', frame)
        k = cv2.waitKey(30) & 0xff
        if k == 114:
            nilai_counter = 0

        if k == 27:
            break
        else:
            break
cv2.waitKey()
