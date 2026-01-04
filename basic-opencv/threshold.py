import cv2

img = cv2.imread('basic-opencv/media/livro-com-sombra.jpg')
img = cv2.resize(img, (500, 500))
greyImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

### 
## threshold is a cv2 function to binarize an image
# param(file, thresh, maxval, type)
_, th1 = cv2.threshold(greyImg, 80, 255, cv2.THRESH_BINARY)

## but the image has a shadow that hinders binarization, so use-
## adaptiveThreshold is a cv2 function adpative to binarize an image with shadows.
# param(file, maxval, adptativeMethod, type, blocksize)
th2 = cv2.adaptiveThreshold(greyImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 47, 10)

th3 = cv2.adaptiveThreshold(greyImg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 47, 10)


cv2.imshow('Original Image', img)
cv2.imshow('Grey Image', greyImg)
cv2.imshow('TH1', th1)
cv2.imshow('TH2', th2)
cv2.imshow('TH3', th3)

cv2.waitKey(0)