# VideoFaceBlur

VideoFaceBlur - это приложение для захвата видео с веб-камеры или видеофайла и применения размытия к области вокруг глаз в обнаруженных лицах. Оно использует библиотеку OpenCV для обработки видео и обнаружения лиц и глаз.

## Описание функций

### Импорты
Импорт необходимых библиотек для работы с изображениями и видео.

```python
import cv2
import numpy as np
```

### Настройка захвата видео
Создает объект для захвата видео с веб-камеры или видеофайла. По умолчанию используется веб-камера.

```python
# capture = cv2.VideoCapture('videos/to_river.mp4')
capture = cv2.VideoCapture(0)
```

### Загрузка Haar Cascade для обнаружения лиц и глаз
Загружает предварительно обученные модели для обнаружения лиц и глаз.

```python
find_face = cv2.CascadeClassifier('model_face.xml')
find_eyes = cv2.CascadeClassifier('eyes.xml')
```

### Основной цикл обработки видео
Основной цикл, который захватывает кадры с видео потока, обрабатывает их и отображает результат.

```python
while True:
    success, img = capture.read()
    eye_frame = np.zeros(img.shape, np.uint8)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = find_face.detectMultiScale(gray, 1.3, 5)
```

### Обнаружение лиц
Проходит по всем обнаруженным лицам и ищет глаза в каждом лице.

```python
    for (x, y, w, h) in faces:
        eyes = find_eyes.detectMultiScale(gray, scaleFactor=5, minNeighbors=3)
        if len(eyes) >= 2:
            ex1, ey1, ew1, eh1 = eyes[0]
            ex2, ey2, ew2, eh2 = eyes[1]
```

### Обработка глаз и применение размытия
Если обнаружены два или более глаза, определяет их позиции, рисует прямоугольник вокруг глаз и применяет размытие к этой области.

```python
            if eyes[0][0] < eyes[1][0]:
                eyes = cv2.rectangle(img, (x, ey1), (x + w, ey1 + eh2), (0, 255, 0), thickness=2)
                cut_eye = eyes[ey1:ey1 + eh2, x:x + w]
                cut_eye = cv2.GaussianBlur(cut_eye, (49, 39), 0)
                img[ey1:ey1 + eh2, x:x + w] = cut_eye
```

### Отображение результата
Отображает обработанное изображение в окне.

```python
    cv2.imshow('Result', img)
```

### Условие выхода из цикла
Цикл продолжается до тех пор, пока не будет нажата клавиша 'q'.

```python
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

### Освобождение ресурсов и закрытие окон
Освобождает объект захвата видео и закрывает все окна OpenCV.

```python
capture.release()
cv2.destroyWindow()
```

