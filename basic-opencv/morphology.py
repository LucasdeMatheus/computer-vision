import cv2

img = cv2.imread('basic-opencv/media/torre-eiffel.jpg')
img = cv2.resize(img, (500, 400))
greyImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#  -------------------- MORPHOLOGY --------------------

## GaussianBlur is a cv2 function for blur the image
###  param(file, ksize, sigmaX)
blurImg = cv2.GaussianBlur(greyImg, (7, 7), 0)

## Canny is a cv2 function for binarization of the image outline 
### param(file, min, max)
cannyImg = cv2.Canny(img, 50, 100)

## dilate is a cv2 function to expand white strokes
### param(file, ksize, dsize)
dilatImg = cv2.dilate(cannyImg, (5, 5), iterations= 5)

## erode is a function cv2 equal to dilate, but in reverse
### param(file, ksize, esize)
erodeImg = cv2.erode(cannyImg, (5, 5), iterations= 2)

## Open process is erode followed by dilate - clear image
### param(file, morph_type, ksize)
openingImg = cv2.morphologyEx(cannyImg, cv2.MORPH_OPEN, (5,5))

## Close process is dilate followed by erode - clear the object
### param(file, morph_type, ksize)
closingImg = cv2.morphologyEx(cannyImg, cv2.MORPH_CLOSE, (5,5))

cv2.imshow('Original Image', img)
cv2.imshow('Gray Image', greyImg)
cv2.imshow('Blur Image', blurImg)
cv2.imshow('Canni Image', cannyImg)
cv2.imshow('Dilat Image', dilatImg)
cv2.imshow('Erode Image', erodeImg)
cv2.imshow('open Image', openingImg)
cv2.imshow('closing Image', closingImg)

cv2.waitKey(0)