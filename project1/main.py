import cv2
import pickle
import numpy as np

spaces = []

with open('project1/spaces.pkl', 'rb') as file:
    spaces = pickle.load(file)

video = cv2.VideoCapture('project1/video.mp4')

while True:
    check, img = video.read()
    greyImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
   
    thImg = cv2.adaptiveThreshold(greyImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    
    imgMedian = cv2.medianBlur(thImg, 5)

    kernel = np.ones((3, 3), np.int8)

    dilImg = cv2.dilate(imgMedian, kernel)

    spaceFree = 0

    for x, y, w, h in spaces:
       space = dilImg[y : y + h, x : x + w]
       count = cv2.countNonZero(space)
       cv2.putText(img, str(count), (x, y + h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

       if count > 1100:   
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
       else:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        spaceFree +=1

    cv2.putText(img, f'{spaceFree}/69',(20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    cv2.imshow('video', img)  
    cv2.waitKey(10)
