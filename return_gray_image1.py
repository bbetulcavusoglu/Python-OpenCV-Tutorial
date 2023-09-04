#Return Gray Image
#This code first reads the image in color and then converts it to gray.
import cv2 as cv

path= "OpenCV_Projects_Images/"

img=cv.imread(path+"view.jpg")

print(type(img))

cv.namedWindow("colored", cv.WINDOW_AUTOSIZE)

cv.imshow("colored", img)
cv.waitKey(1)

#cvtColor: the method used to change the format of the picture
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(0)

#imwrite : saves an image to a file
cv.imwrite(path + "new_gray_opencv1.png", gray)
cv.destroyAllWindows()