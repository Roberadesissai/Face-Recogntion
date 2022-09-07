from email.mime import image
import cv2

image = cv2.imread("image/robera.jpg")
gray=cv2.cvtColor

cv2.imshow("image", image)

cv2.waitKey()
