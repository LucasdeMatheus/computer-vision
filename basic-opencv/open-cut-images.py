import cv2

#     open image  param(file)
img = cv2.imread("basic-opencv/media/BAH.jpg")

# selectROI is a function opencv for select area in image.
## param(string, file, ...)
dim = cv2.selectROI("select cropping area", img, False)

cv2.destroyWindow('select cropping area')

x, y, w, h = dim # (position x, position y, width, height)


cut = img[y : y + h, x : x + w]

# SAVE IMAGES

# directory
directory = "basic-opencv/clippings/"

# imwrite is a function opencv for save medias. 
## param(directory+nameFile, file)
cv2.imwrite(f"{directory}cut.jpg", cut)


##  function(name of windows, param(file))
cv2.imshow('image', img) 
cv2.imshow("cut", cut)

cv2.waitKey(0)



