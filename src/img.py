import cv2

img = cv2.imread("cat.jpg")
cv2.imwrite("new_img.jpg", img)