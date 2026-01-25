import cv2

cam = cv2.VideoCapture(2)

### CascadeClassifier is a cv2 function classifier of Cascade.
## param(.xml)
classifier = cv2.CascadeClassifier("cascades/haarcascade_eye.xml")

while True:
    check, img = cam.read()

    greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ### detectMultiScale is a cv2 function to detect the objects in video.
    ## param(file, minSize, scaleFactor)
    # return positions X and Y and Length and Width
    objects = classifier.detectMultiScale(greyImg, minSize = (50, 50), scaleFactor = 1.5)

    ## draw rectangles in the videos
    for x, y, h, w in objects:
        cv2.rectangle(img, (x, y), (x + h, y + w), (255, 0, 0), 2)
    
    cv2.imshow("grey cam", greyImg)
    cv2.imshow("cam", img)
    cv2.waitKey(1)