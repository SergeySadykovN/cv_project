import cv2
import numpy as np



# capture = cv2.VideoCapture('videos/to_river.mp4')
capture = cv2.VideoCapture(0)
find_face = cv2.CascadeClassifier('model_face.xml')
find_eyes = cv2.CascadeClassifier('eyes.xml')

while True:
    success, img = capture.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = find_face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        r_gray = gray[y:y + h, x:x + w]
        r_color = img[y:y + h, x:x + w]
        eyes = find_eyes.detectMultiScale(r_gray, scaleFactor=5, minNeighbors=3)
        # if len(eyes) >= 2:
        #     ex1, ey1, ew1, eh1 = eyes[0]
        #     ex2, ey2, ew2, eh2 = eyes[1]

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)

        for (ex, ey, ew, eh) in eyes:
            eyes = cv2.rectangle(r_color, (ex, ey), (ex + ew//2, ey + eh//2), (0, 255, 0), thickness=1)
            # cut_eyes = eyes

    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

capture.release()
cv2.destroyWindow()
