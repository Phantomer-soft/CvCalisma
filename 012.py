 #                                   ********RENK UZAYLARI - RENK DÖNÜŞÜMLERİ***********
import cv2
import numpy as np
araba=cv2.imread("car.jpg")
cv2.imshow("araba",araba)
araba2=cv2.cvtColor(araba,cv2.COLOR_BGR2GRAY) #araba nesnesinin renklerini rgbye çevirip araba 2 nesnesi ürettik
araba3=cv2.cvtColor(araba,cv2.COLOR_BGR2HSV)
cv2.imshow("araba2",araba2)


cv2.waitKey(0)
cv2.destroyAllWindows()
