import cv2
import face_recognition
from simple_facerec import SimpleFacerec


sfr = SimpleFacerec()
sfr.load_encoding_images("image/")

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
