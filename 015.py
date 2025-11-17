#                                         *********BITWISE(MANTIK)ISLEMLERI**********
import cv2
import numpy as np

img = cv2.imread("daire.png")
img2 = cv2.imread("dikdortgen.png")
bit_and=cv2.bitwise_and(img,img2)# 1-1 = 1, 1-0 = 0
bit_or=cv2.bitwise_or(img,img2)# 1-0 = 1 , 0 -0 = 0
bit_xor=cv2.bitwise_xor(img,img2)
bit_not=cv2.bitwise_not(img,img2)
nand=cv2.bitwise_not(bit_and,bit_and)
nor=cv2.bitwise_not(bit_or,bit_or)
#KLASİK MANTIK KAPILARI KULLANILIYOR GİBİ DÜŞÜNÜLEBİLİR

#cv2.imshow("img1",img)
#cv2.imshow("img2",img2)
#cv2.imshow("and",bit_and)
#cv2.imshow("or",bit_or)
#cv2.imshow("xor",bit_xor)
#cv2.imshow("not",bit_not)
cv2.imshow("nand",nand)
cv2.imshow("nor",nor)

cv2.waitKey(0)
cv2.destroyAllWindows()