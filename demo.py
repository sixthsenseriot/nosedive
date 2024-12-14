import cv2 as cv
img = cv.imread("/home/khanh/Pictures/four-byte-burger.png")

cv.imshow("Display window", img)
k = cv.waitKey(0)
