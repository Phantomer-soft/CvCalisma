#                *********TUVAL OLUŞTURMA********
import cv2
import numpy as np

canvas=np.zeros((512,512,3),np.uint8)+250#sıfırlardan oluşan bir kanvas oluştur,boyutları 480-640 olsun 3 kanallı olsun(renkli),sona + değer yazınca o değerlerden oluşturuyor
print(canvas)

cv2.imshow("tuval",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()