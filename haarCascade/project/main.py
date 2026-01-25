import cv2

cam = cv2.VideoCapture(2)
classifier = cv2.CascadeClassifier("haarCascade/project/cascade.xml")


while True:
    check, img = cam.read()

    greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ### detectMultiScale is a cv2 function to detect the objects in video.
    ## param(file, minSize, scaleFactor)
    # return positions X and Y and Length and Width
    objects = classifier.detectMultiScale(greyImg, minSize = (30, 30), minNeighbors=3, scaleFactor = 1.3)

    ## draw rectangles in the videos
    for x, y, w, h in objects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    
    cv2.imshow("cam", img)
    cv2.waitKey(1)