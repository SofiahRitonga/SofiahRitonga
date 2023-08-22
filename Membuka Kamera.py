# Import Library OpenCV
import cv2
# Variabel Video Capture
cap = cv2.VideoCapture(0)

# Fungsi membuat Frame
while (True):
    # Membaca Video
    ret, frame = cap.read()
    # Pengaturan Frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('S'):
        break

cap.release()
cv2.destroyAllWindows()
