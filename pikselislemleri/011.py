#               ********ROI IŞLEMI*********
import cv2
img=cv2.imread("araba.jpg")
roi=img[260:320,400:530] #odaklanmak istediğimiz aralığı bir değişkene atadık
cv2.imshow("roi",roi)#odaklandığımız aralığı ekranda gösterdik

cv2.waitKey(0)
cv2.destroyAllWindows()