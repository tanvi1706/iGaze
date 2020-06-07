import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("206.jpg")
img = img1.astype('uint8')
 #cv2.THRESH_BINARY |
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
(thresh, im_bw) = cv2.threshold(img, 155, 255, cv2.THRESH_OTSU)
cv2.imwrite('bw_image7.jpg',im_bw)