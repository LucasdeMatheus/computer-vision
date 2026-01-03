import cv2

# capture video param(webcam index)
cam = cv2.VideoCapture(0)

# function set is defined for param(config, value)
cam.set(3, 640) # 3 is length
cam.set(4, 420) # 4 is width
cam.set(10, 200) # 10 is lighting

while True:
    check, img = cam.read()

    ##  function(name of windows, param(file))
    cv2.imshow('web cam', img)
    
    # if i press button "q" the loop break
    if cv2.waitkey(1) & 0xFF == ord('q'):
        break