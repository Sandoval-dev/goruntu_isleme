import cv2 as cv

resim = cv.imread("resim/fotografci.png")

yumusatilmis_resim = cv.blur(resim, (10, 10))

cv.imshow("a", yumusatilmis_resim)
cv.waitKey(0)
