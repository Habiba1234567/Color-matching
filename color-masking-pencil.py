import cv2
import numpy as np

img = cv2.imread('./color_pencils.jpeg', cv2.IMREAD_UNCHANGED)

# converting from gbr to hsv color space
img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

HSV_mask = cv2.inRange(img_HSV, (129, 50, 70), (158, 255, 255))
HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))

HSV_result = cv2.bitwise_and(img, img, mask=HSV_mask)
cv2.imshow("Mask Pencil", HSV_mask)
cv2.imshow("Result Pencil", HSV_result)
cv2.imshow("Original Image Pencil", img)
cv2.waitKey(0)