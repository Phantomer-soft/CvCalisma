import cv2 #                   **********KAMERA KULLANARAK FRAME YAKALAMA*************
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
while(True):
    ret, frame=cap.read() #cap.read 2 tane değer döndrürür biri true false diğeri frame
    frame=cv2.flip(frame,1) #Görüntünün yönünü düzeltir ilk değer değişken, 2.değer yön 0,1,-1 alabilir
    cv2.imshow('video',frame) #video isimli pencerede frameleri gösterir
    if cv2.waitKey(1) & 0xFF == ord('q'): #q tuşuna basılınca kapanmasını sağlar
        break


    cv2.waitKey(1) #Buradaki değeri ne kadar yüksek tutarsan fps o kadar düşük oluyor gecikme ve takılma oluyor
    # Açıklama : 1 milisaniyede 1 görüntü al

cap.release()
cv2.destroyAllWindows()