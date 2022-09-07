from unittest import result
import cv2
import face_recognition

image_robera = cv2.imread("image/robera.jpg")
gray_robera = cv2.cvtColor(image_robera, cv2.COLOR_BGR2RGB)
image_encoding_robera = face_recognition.face_encodings(gray_robera)[0]

image_mati = cv2.imread("image/mati.jpg")
gray_mati = cv2.cvtColor(image_mati, cv2.COLOR_BGR2RGB)
image_encoding_mati = face_recognition.face_encodings(gray_mati)[0]

image_yadinet = cv2.imread("image/yadinet.jpg")
gray_yadinet = cv2.cvtColor(image_yadinet, cv2.COLOR_BGR2RGB)
image_encoding_yadinet = face_recognition.face_encodings(gray_yadinet)[0]

result=face_recognition.compare_faces([image_encoding_yadinet], image_encoding_mati)
print(result)


cv2.imshow("Robera", image_robera)
cv2.imshow("Mati", image_mati)
cv2.imshow("Yadinet", image_yadinet)
cv2.waitKey()
