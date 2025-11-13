#                             *********TRACKBAR + MASKELEME *********
import cv2
import numpy as np

cap=cv2.VideoCapture(0)
def fonk(x):
    pass
cv2.namedWindow("bar")
cv2.resizeWindow("bar",(500,400))
# TRACKBARLARIN OLUŞTURULMASI
cv2.createTrackbar("alt-h","bar",0,100,fonk)
cv2.createTrackbar("alt-s","bar",0,255,fonk)
cv2.createTrackbar("alt-v","bar",0,255,fonk)

cv2.createTrackbar("ust-h","bar",0,180,fonk)
cv2.createTrackbar("ust-s","bar",0,255,fonk)
cv2.createTrackbar("ust-v","bar",0,255,fonk)

# TARACKBARLARIN YERLERİNİN AYARLANMASI
cv2.setTrackbarPos("ust-h","bar",150)
cv2.setTrackbarPos("ust-s","bar",200)
cv2.setTrackbarPos("ust-v","bar",200)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#        KULLANICI PENCERENİN YERİNİ DEĞİŞTİRSE BİLE BU DEĞERLERİ ALABİLMESİNİ SAĞLADIK
    alt_h = cv2.getTrackbarPos("alt-h","bar")
    alt_s = cv2.getTrackbarPos("alt-s", "bar")
    alt_v = cv2.getTrackbarPos("alt-v", "bar")
    ust_h = cv2.getTrackbarPos("ust-h","bar")
    ust_s = cv2.getTrackbarPos("ust-s", "bar")
    ust_v = cv2.getTrackbarPos("ust-v", "bar")

    altrenk=np.array([alt_h,alt_s,alt_v]) #TUPPLE OLUŞTURMA
    ustrenk=np.array([ust_h,ust_s,ust_v])

    maske=cv2.inRange(frame_hsv,altrenk,ustrenk)
    cv2.imshow("maske",maske)
    cv2.imshow("frame",frame)

    if cv2.waitKey(1)&0xFF == ord('q'):
     break
cap.release()
cv2.destroyAllWindows()