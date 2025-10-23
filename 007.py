import cv2
import numpy as np
canvas=np.zeros((480,640,3),np.uint8)

cv2.line(canvas,(0,0),(200,200),(255,255,255),5)#Çizgi oluşturma (başlangıç,bitiş,renk,kalınlık)
cv2.rectangle(canvas,(100,100),(200,200),(255,255,255),3)#dikdörtgen oluşturma(başlangıç,bitiş,renk,çizgi kalınlığı(-1 içi dolu))
cv2.circle(canvas,(400,300),50,(255,255,255),-1)#Çember oluşturma(merkez,yarıçap,renk,çizgi kal.(-1 yapınca içi dolu)

nokta1=(300,10)  #Üçgenin köşe noktalarının belirlenmesi
nokta2=(300,100)
nokta3=(400,80)
canvas=cv2.line(canvas,nokta1,nokta2,(255,255,255),5)#Köşe noktalarını birleştirme
canvas=cv2.line(canvas,nokta2,nokta3,(255,255,255),5)
canvas=cv2.line(canvas,nokta3,nokta1,(255,255,255),5)
#Devamında beşgen altıgen de oluşturulabilir



cv2.imshow("tuval",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()