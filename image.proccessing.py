import cv2

img = cv2.imread("poster.jpg")
cv2.imshow("output", img)
print(img)
cv2.waitKey(0)