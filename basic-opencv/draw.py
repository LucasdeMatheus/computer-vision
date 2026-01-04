import cv2

img = cv2.imread('basic-opencv/media/torre-eiffel.jpg')


# DRAW FORMS IN IMAGE


## rectangle
### param(file, initial, final, rgb, thickness)
cv2.rectangle(img, (50, 50), (200, 200), (255, 0, 0), 2)

## circle
### param(file, center, ray, color, thickness)
cv2.circle(img, (50, 50), 10, (255, 0, 0), 2)


## line
### param(file, initial, final, rgb, thickness)
cv2.line(img, (400, 400), (500, 400), (255, 0, 0), 2)


# INSERT TEXT IN IMAGE

## text
text = "torre eiffel"

## putText is a cv2 function for insert text in images
### param(file, text, initial, font, fontsize, color, thickness)
cv2.putText(img, text, (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)


cv2.imshow('Original Image', img)

cv2.waitKey(0)