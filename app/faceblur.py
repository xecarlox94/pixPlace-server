import cv2

import numpy as np



def process_img(img):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('mldata.xml')

    img = cv2.imdecode(img, flags=1)

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        # Enclose inside a blue rectangular box
#        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        # Select only detected face portion for Blur
        face_color = img[y:y + h, x:x + w]
        # Blur the Face with Gaussian Blur of Kernel Size 51*51
        blur = cv2.GaussianBlur(face_color, (51, 51), 0)
        img[y:y + h, x:x + w] = blur

    return img

