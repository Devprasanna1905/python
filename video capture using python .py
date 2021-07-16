import cv2
import numpy

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
while (1):
    ret,img=cap.read()
    cv2.imshow("img",img)

    k=cv2.waitKey(30)
    if k==ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
