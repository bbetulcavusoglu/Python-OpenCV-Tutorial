#This code assigns the image named view.jpg to the variable named img.
# Then it assigns a copy of the image to the variable m1 to operate on this image.
# It assigns 0 to the dimensions specified on this picture and these parts become black.
#NOTE: We can give values between 0 and 255. As it gets closer to 0, it becomes black, and as it gets farther from 0, it becomes white.
import cv2 as cv
import numpy as np

path = "OpenCV_Projects_Images/"
img = cv.imread(path + "view.jpg")

print(type(img))
cv.namedWindow("image_test", cv.WINDOW_AUTOSIZE)
cv.imshow("image_test", img)
cv.waitKey(1)

m1= np.copy(img)

m1[110:120, 210:310, : ]=0
cv.namedWindow("m1", cv.WINDOW_AUTOSIZE)

cv.imshow("m1", m1)
cv.waitKey(0)

cv.destroyAllWindows()