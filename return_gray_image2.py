#Return Gray Image
#This code reads the color image directly as gray
import cv2 as cv

path= "OpenCV_Projects_Images/"

img=cv.imread(path+"view.jpg", cv.IMREAD_GRAYSCALE)

print(type(img))

cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)

cv.imshow("gray", img)
cv.waitKey(0)

#imwrite : saves an image to a file
cv.imwrite(path + "new_gray_opencv2.png", img)
cv.destroyAllWindows()