import cv2
import numpy as np

# capture = cv2.VideoCapture('videos/to_river.mp4')
capture = cv2.VideoCapture(0)
find_face = cv2.CascadeClassifier('model_face.xml')
find_eyes = cv2.CascadeClassifier('eyes.xml')

while True:
    success, img = capture.read()
    eye_frame = np.zeros(img.shape, np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = find_face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        eyes = find_eyes.detectMultiScale(gray, scaleFactor=5, minNeighbors=3)
        if len(eyes) >= 2:
            ex1, ey1, ew1, eh1 = eyes[0]
            ex2, ey2, ew2, eh2 = eyes[1]

            if eyes[0][0] < eyes[1][0]:
                # определяем рамку для обоих глаз
                eyes = cv2.rectangle(img, (x, ey1), (x + w, ey1 + eh2), (0, 255, 0), thickness=2)
                cut_eye = eyes[ey1:ey1 + eh2, x:x + w]
                # размываем область с глазами
                cut_eye = cv2.GaussianBlur(cut_eye, (49,39), 0)
                # заменяем оригинал на размытую рамку
                img[ey1:ey1 + eh2, x:x + w] = cut_eye

    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

capture.release()
cv2.destroyWindow()
