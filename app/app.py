import cv2
import faceblur as fblur

img = cv2.imread('pic.jpg')

img = fblur.enc_faceblur(img)

cv2.imwrite('processed_pic.jpg', img)
