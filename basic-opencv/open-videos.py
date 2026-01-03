import cv2

# capture video param(file)
video = cv2.VideoCapture("basic-opencv/media/BAH.mp4")


# loop with while
while True:
    # two var, check and the img for reproduction
    check, img = video.read()

    print(img.shape) # (640, 360, 3)

    # resize resolution param(file, (width, heigth))
    ImgRedim = cv2.resize(img, (240, 260))

    cv2.imshow('video', img)
    cv2.imshow('video', ImgRedim)
    
    # wait X ms for reproduction
    cv2.waitKey(0)