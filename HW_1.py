import cv2
import numpy as np

logo_urban = np.zeros((500, 500, 3), dtype='uint8')

logo_urban[10:490, 10:490] = 255,31,133
kernel = np.ones((3,99), np.uint8)
gradient = cv2.morphologyEx(logo_urban, cv2.HOUGH_GRADIENT_ALT, kernel=kernel)


# cv2.line(photo, (0, photo.shape[0]//2), (photo.shape[1], photo.shape[0]//2), (0,0,255), thickness=3 )

cv2.circle(logo_urban, (logo_urban.shape[1] // 2, logo_urban.shape[0] // 2), 200, (255, 255, 255), thickness=3)

cv2.putText(logo_urban, 'Urban', (150,100), cv2.FONT_HERSHEY_DUPLEX, 1, (255,0,0), thickness=1)
cv2.ellipse(logo_urban, center=(logo_urban.shape[1]//2,250), axes=(100,100), angle=0, startAngle=0, endAngle=180, color=(0,255,0), thickness=5)
cv2.ellipse(logo_urban, center=(logo_urban.shape[1]//2,250), axes=(50,50), angle=0, startAngle=0, endAngle=180, color=(0,255,0), thickness=5)

cv2.line(logo_urban, (300, logo_urban.shape[0] // 4),(350, logo_urban.shape[0]//4) , color=(0,0,255), thickness=5)
cv2.line(logo_urban, (150, logo_urban.shape[0] // 4),(200, logo_urban.shape[0]//4) , color=(0,0,255), thickness=5)

cv2.line(logo_urban, (150, logo_urban.shape[0] // 4),(150, logo_urban.shape[0]//2) , color=(255,0,0), thickness=5)
cv2.line(logo_urban, (200, logo_urban.shape[0] // 4),(200, logo_urban.shape[0]//2) , color=(255,0,0), thickness=5)


cv2.line(logo_urban, (300, logo_urban.shape[0] // 4),(300, logo_urban.shape[0]//2) , color=(255,0,0), thickness=5)
cv2.line(logo_urban, (350, logo_urban.shape[0] // 4),(350, logo_urban.shape[0]//2) , color=(255,0,0), thickness=5)


cv2.imshow('photo', logo_urban) # показать картинку
cv2.waitKey(0)


