import cv2
import numpy as np

cap=cv2.VideoCapture("ornekvid.mp4")     #videoyu al

while True:
    ret, frame = cap.read()

    if ret != False:   #video devam ettiği sürece
        frame2=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    # yakalanan frame i bgr den griye çevir

        cv2.imshow("frame",frame)  #renkli video
        cv2.imshow("frame2",frame2) # gri video
        cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'): # çıkış işlemi
            break
        continue
    break

cap.release()
cv2.destroyAllWindows()

