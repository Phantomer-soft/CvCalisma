#                         *********EKRANA YAZI YAZDIRMA*********
# TRACKBAR İLE TUVAL BOYAMA
import cv2
import numpy as np

canvas=np.zeros((480,640,3),np.uint8) # kanvas oluşturma

font1=cv2.FONT_HERSHEY_SIMPLEX #Font türleri
font2=cv2.FONT_ITALIC
font3=cv2.QT_FONT_BOLD
cv2.putText(canvas,"SELAMLAR",(30,200),font2,2,(255,255,255),cv2.LINE_4)
#Yazılacak yer,metin,konum,font türü,boyut,renk,yazı tipi(sanırım)


cv2.imshow("pencere",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()