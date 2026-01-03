import cv2

#     open image  param(file)
img = cv2.imread("basic-opencv/media/BAH.jpg")

#        convert Colors param(file, conversion)
greyImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

# dimensions function: (width, length, colors layers)
print(img.shape) # (487, 480, 3)

# show image in a window
##  function(name of windows, param(file))
cv2.imshow('image', img) 
cv2.imshow('grey image', greyImg)

cv2.waitKey(0)