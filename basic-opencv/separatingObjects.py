import cv2

img = cv2.imread('basic-opencv/media/gatos.jpg')
img = cv2.resize(img, (500, 500))
greyImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cannyImg = cv2.Canny(greyImg, 30, 200)

closeImg = cv2.morphologyEx(cannyImg, cv2.MORPH_CLOSE, (7,7))

# get a contours
contours, hierarchy = cv2.findContours(closeImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# contours
print(contours)

# index
objectNumber = 1
for cnt in contours:
    # cv2.drawContours(img, cnt, -1, (255, 0, 0), 2) -- this code is to contour objects
    
    # this code is for framing an object
    x, y, w, h = cv2.boundingRect(cnt) 
    
    # this a cut objects and save in folder objects
    object = img[y:y+h, x:x+w]
    cv2.imwrite(f'basic-opencv/media/objects/gato{objectNumber}.jpg', object)
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    objectNumber += 1

cv2.imshow('Image', img)
cv2.imshow('Grey Image', greyImg)
cv2.imshow('Canny Image', cannyImg)

cv2.waitKey(0)