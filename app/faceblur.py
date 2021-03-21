import cv2
import io
import numpy as np





def blur_faces(img):
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('mldata.xml')

    img = cv2.imdecode(img, flags=1)

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        # Select only detected face portion for Blur
        face_color = img[y:y + h, x:x + w]
        # Blur the Face with Gaussian Blur of Kernel Size 51*51
        blur = cv2.GaussianBlur(face_color, (51, 51), 0)
        img[y:y + h, x:x + w] = blur

    return img



def proc_req_img(request):
    image = request.files["image"]

    in_memory_file = io.BytesIO()

    image.save(in_memory_file)

    image = np.frombuffer(in_memory_file.getvalue(), dtype=np.uint8)

    return  encode_img(image)

def enc_faceblur(img):
    img = blur_faces(img)

    img = cv2.imencode('.jpg',img)[1].tobytes()

    return img
