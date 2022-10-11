import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    cv2.imshow("capture", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
