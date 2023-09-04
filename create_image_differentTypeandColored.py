import cv2 as cv
import numpy as np

path = "OpenCV_Projects_Images/"
img = cv.imread(path + "view.jpg")

#Creates a black image of size [400,400]
n1= np.zeros([400,400], np.uint8)
cv.namedWindow("n1", cv.WINDOW_AUTOSIZE)
cv.imshow("n1", n1)
cv.waitKey(1)

#Creates a black image of size [600,600].
n2= np.zeros([600,600], np.uint8)
cv.namedWindow("n2", cv.WINDOW_AUTOSIZE)
cv.imshow("n2", n2)
cv.waitKey(1)

#Creates a [400,400] size black image, which is a grayscale image.
n3= np.zeros([400,400], np.uint8)
n3[:,:]=100
cv.namedWindow("n3", cv.WINDOW_AUTOSIZE)
cv.imshow("n3", n3)
cv.waitKey(0)

cv.destroyAllWindows()