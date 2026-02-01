import cv2
import mediapipe as mp
import math

video = cv2.VideoCapture('mediapipe/ANEXO+polichinelos.mp4')

pose = mp.solutions.pose
Pose = pose.Pose(min_tracking_confidence = 0.5, min_detection_confidence=0.5)

draw = mp.solutions.drawing_utils

count = 0

ret = True

while True:
    check, img = video.read()

    RGBvideo = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    results = Pose.process(RGBvideo)
    
    points = results.pose_landmarks

    draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)

    h, w, _ = img.shape
    if results.pose_landmarks:
        points = results.pose_landmarks
        draw.draw_landmarks(img, points, pose.POSE_CONNECTIONS)

        h, w, _ = img.shape

        rf = points.landmark[pose.PoseLandmark.RIGHT_FOOT_INDEX]
        lf = points.landmark[pose.PoseLandmark.LEFT_FOOT_INDEX]
        rh = points.landmark[pose.PoseLandmark.RIGHT_INDEX]
        lh = points.landmark[pose.PoseLandmark.LEFT_INDEX]

        footRX, footRY = int(rf.x * w), int(rf.y * h)
        footLX, footLY = int(lf.x * w), int(lf.y * h)
        handRX, handRY = int(rh.x * w), int(rh.y * h)
        handLX, handLY = int(lh.x * w), int(lh.y * h)

        distHands = math.hypot(handRX - handLX, handRY - handLY)
        distFeet  = math.hypot(footRX - footLX, footRY - footLY)


        if ret == True and distHands <= 150 and distFeet >= 150:
            count += 1
            ret = False
        
        if distHands > 150 and distFeet < 150:
            ret = True

        text = f'{count} polichinelos'
        cv2.putText(img, text, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 5)

    cv2.imshow("video", img)

    cv2.waitKey(40)