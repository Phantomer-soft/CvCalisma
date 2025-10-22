import cv2 #                   **********VİDEODAN FRAME YAKALAMA*************
cap=cv2.VideoCapture("307864_small.mp4")

while(True):
    ret, frame=cap.read()
    if ret==False:
        break
    frame=cv2.flip(frame,1)
    cv2.imshow('video',frame) #video isimli pencerede frameleri gösterir
    if cv2.waitKey(1) & 0xFF == ord('q'): #q tuşuna basılınca kapanmasını sağlar
        break

cap.release()
cv2.destroyAllWindows()