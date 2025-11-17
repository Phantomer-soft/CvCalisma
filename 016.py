#                                       ********RESİM DÖNDÜRME İŞLEMLERİ*********
import cv2
import numpy as np

img=cv2.imread("car.jpg")

rows=img.shape[0]#SATIR SAYISI
cols=img.shape[1]#SÜTUN SAYISI
#print(rows) 561
#print(cols) 900
rot=cv2.getRotationMatrix2D((cols/2,rows/2),180,1)# SATIR SAYISININ YARISI,SÜTUN SAYISININ YARISI 180 DERECE 1 ÖLÇEKLE DÖNDÜR
# İKİYE BÖLMEMİZİN SEBEBİ RESMİ TUVALE SIĞDIRM İÇİN
new_pic=cv2.warpAffine(img,rot,(cols,rows))


cv2.imshow("araba",new_pic)

cv2.waitKey(0)
cv2.destroyAllWindows()