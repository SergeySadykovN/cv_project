import cv2
import numpy as np



capture = cv2.VideoCapture('videos/to_river.mp4')


while True:
    success, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)

    eyes = cv2.CascadeClassifier('eyes.xml')
    result = eyes.detectMultiScale(gray, scaleFactor=6, minNeighbors=4)

    for (x, y, w, h) in result:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)


    # cv2.imshow('Result', img)
    cv2.imshow('Result', img)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
