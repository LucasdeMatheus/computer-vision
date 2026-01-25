import cv2

video = cv2.VideoCapture(2)

# index
index = 1
while True:
    check, img = video.read()
    greyImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    
    # comand to capture images positives
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        print("press tecla Q")
        imgR = cv2.resize(greyImg, (220, 220))
        cv2.imwrite(f'haarCascade/project/photos/p/img{index}.jpg', imgR)
        index += 1

    cv2.imshow('Captura', img)
    cv2.waitKey(1)