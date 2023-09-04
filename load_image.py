import cv2 as cv

path= "OpenCV_Projects_Images/"

img=cv.imread(path+"view.jpg")

print(type(img)) #So a data structure on which I can perform mathematical operations

# namedWindow : Creates a window to hold images
# WINDOW_AUTOSIZE : Allows the image to be sent in its own size
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)

# imshow : show pictures
cv.imshow("opencv_test", img)
cv.waitKey(0)

# destroyAllWindows : If there are any open windows, close them all
cv.destroyAllWindows()