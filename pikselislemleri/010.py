#                                ***********PİKSEL İŞLEMLERİ************
import cv2
import numpy as np
resim=cv2.imread("img001.png")
#cv2.imshow("gorsel",resim)
renk=resim[200,200,2] #resim isimli görselin 200,200 noktasındaki (b(0),g(1),r(2)) değerini döndür 3. değeri girmezsen hepsini verir
"""mavi=resim[100,100,0]
yesil=resim[100,100,1]
kirmizi=resim[100,100,2]
print("Mavi : ",mavi,"Yeşil : ",yesil,"Kırmızı : ",kirmizi)"""
print(resim.shape) #resim boyutu

img=cv2.imread("img001.png")
print(img[300,300],"önce")
img[300,300]=255#300,300 noktasındaki değerleri 255 yap
print(img[300,300],"sonra")

mavi=img.item(100,100,0)#mavi=resim[] ile aynı şey
print(mavi)

print(img.item(150,150,0))
cv2.imshow("gorsel",img)

cv2.waitKey(0)
cv2.destroyAllWindows()