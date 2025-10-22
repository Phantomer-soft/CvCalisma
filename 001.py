import cv2#             *********BAŞLANGIÇ**********
import numpy as np
import matplotlib

img=cv2.imread('img001.png',cv2.IMREAD_GRAYSCALE) #Resim okuma //GRAYSCALE KOMUTU GRI TONLAMALI OLARAK ALIR BUNUN YERIBNE 0 YAZ DAHA KISA
img=cv2.resize(img,(400,400))#Açılan resmin boyutunu ayarlama
cv2.namedWindow("resim",cv2.WINDOW_NORMAL) #resim isimli pencerenin boyutunu el ile ayarlanabilir yapar
cv2.imshow('resim',img) # Resim gösterme// ilk girilen değer pencere ismi, 2.değer gösterilecek resim
cv2.imwrite('kopya.jpg',img) #img resmini kopya.jpg olarak kaydeder


cv2.waitKey(0) # Kapanmadan ekranda kalmasını sağlama //(0) girince tuşa basılana kadar ekranda kalır
# eğer milisaniye olarak değer girilecekse parantez içine değer girilir
cv2.destroyAllWindows()