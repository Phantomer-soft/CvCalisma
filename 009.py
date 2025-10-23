#                     ********TRACKBAR OLUŞTURMA********
import cv2
import numpy as np

def x ():# Create trackbar fonksiyonunda kullanmak için bir x metodu tanımladık boş olacak
    pass
img=np.zeros((680,540,3),np.uint8)# tuval
cv2.namedWindow("image",cv2.WINDOW_NORMAL)


cv2.createTrackbar("r","image",0,255,x)#r isminde image penceresinde görünecek
# 0 ile 255 arası değer alacak bir trackbar oluştur
cv2.createTrackbar("g","image",0,255,x)
cv2.createTrackbar("b","image",0,255,x)

switch="1: ON, 0: OFF"
cv2.createTrackbar(switch,"image",0,1,x)
#aç kapa tuşu olarak kullanmak için bir trackbar

while True:
    cv2.imshow("image",img)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

    r=cv2.getTrackbarPos("r","image")#image penceresinin r trackbarındaki değeri r değişkenine ata
    g=cv2.getTrackbarPos("g","image")
    b=cv2.getTrackbarPos("b","image")
    #r,g,b trackbarlarıbdan geelen değerleri değişkenlere atadık


    s=cv2.getTrackbarPos(switch,"image")#anahtardan gelen değeri aldık
    if (s==1):
        img[:] = [b, g, r]#resmin renklerini verilen değişkenler yap
    if (s==0):
        img[:]=[0,0,0]

cv2.waitKey(0)
cv2.destroyAllWindows()

