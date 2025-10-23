#                      *******PIKSEL BOYAMA********
import cv2
import numpy as np
img=np.zeros((20,20,3),np.uint8)+255 #3 kanal ile renklendirme yapma
img[0,0]=(10,100,250)
img[0,1]=(50,90,0)  # Renk sıralaması blue,green,red
img[0,2]=(80,80,0)
img[0,3]=(100,70,0)
img[0,4]=(140,60,0)
img[0,5]=(180,50,0)
img[0,6]=(200,40,0)
img[0,7]=(250,30,0)
img=cv2.resize(img,(640,480),interpolation=cv2.INTER_AREA)
#cv2.imshow('image',img)

img2=np.zeros((20,20),np.uint8)+255 #Tek kanal ile renklendirme yapma
img2[0,0]=250
img2[0,1]=150
img2[0,2]=50
img2=cv2.resize(img2,(640,480),interpolation=cv2.INTER_AREA)

cv2.imshow("tuval",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

