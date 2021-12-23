import cv2
import numpy as np

cap = cv2.VideoCapture(0)

rojoBajo1 = np.array([0,100,20], np.uint8)
rojoAlto1 = np.array([8,255,255], np.uint8)

rojoBajo2 = np.array([175,100,20],np.uint8)
rojoAlto2 = np.array([179,255,255],np.uint8)

while True:
    ret,frame = cap.read()
    if ret == True:
        cuadroHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        maskRojo1 = cv2.inRange(cuadroHSV,rojoBajo1,rojoAlto1)
        maskRojo2 = cv2.inRange(cuadroHSV,rojoBajo2,rojoAlto2)
        maskRojo = cv2.add(maskRojo1, maskRojo2)
        maskRojoVis = cv2.bitwise_and(frame,frame, mask = maskRojo)
        cv2.imshow('frame', frame)
        cv2.imshow('maskRojo', maskRojo)
        cv2.imshow('Visualizacion de Rojo',maskRojoVis)
        cv2.imshow('Video',frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
cap.release()
cv2.destroyAllWindows()
