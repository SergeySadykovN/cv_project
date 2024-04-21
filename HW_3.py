import cv2
import numpy as np



capture = cv2.VideoCapture('videos/to_river.mp4')
find_face = cv2.CascadeClassifier('model_face.xml')
find_eyes = cv2.CascadeClassifier('eyes.xml')

while True:
    success, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = find_face.detectMultiScale(gray, 1.3, 5)

    # result = eyes.detectMultiScale(gray, scaleFactor=6, minNeighbors=4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
        r_gray = gray[y:y + h, x:x + w]
        r_color = img[y:y + h, x:x + w]
        eyes = find_eyes.detectMultiScale(r_gray,scaleFactor= 2 , minNeighbors=3)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(r_color, (x,y), (ex + ew, ey + eh), (0,255,0), 2)

    # cv2.imshow('Result', img)
    cv2.imshow('Result', img)



    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

capture.release()
cv2.destroyWindow()
