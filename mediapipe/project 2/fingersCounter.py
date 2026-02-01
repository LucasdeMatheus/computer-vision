import cv2
import mediapipe as mp

video = cv2.VideoCapture(1)

hand = mp.solutions.hands
Hands = hand.Hands(max_num_hands = 1)

draw = mp.solutions.drawing_utils


while True:
    check, img = video.read()
    RGBvideo = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


    results = Hands.process(RGBvideo)
    
    points = results.multi_hand_landmarks

    h, w, _ = img.shape

    pointsFinger = []
    if points:
        for point in points:
            #print(point)

            draw.draw_landmarks(img, point, hand.HAND_CONNECTIONS)

            # id e cordenadas dos pontos
            for id, cord in enumerate(point.landmark):
                cx, cy = int(cord.x * w), int(cord.y * h)
                # cv2.putText(img, str(id), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
                pointsFinger.append((cx,cy))

        # ponta dos dedos
        finger = [8, 12, 16, 20]
        count = 0

        if point:
            for x in finger:
                # se a cordenada da ponta do dedo for menor que a base, o dedos está levantado
                if pointsFinger[x][1] < pointsFinger[x-2][1]:
                    count += 1

            # logica para o dedo polegar, que se movimenta para os lados, e não para baixo.
            if results.multi_handedness[0].classification[0].label == "Left":
                # se a ponta do polegar estiver mais ao lado(left or right), o dedo esta "levantado"
                if pointsFinger[4][0] > pointsFinger[2][0]:
                    count += 1
            else:
                if pointsFinger[4][0] < pointsFinger[2][0]:
                    count += 1
        

        text = f'{count} dedos levantados'
        cv2.putText(img, text, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)

        thumb = 4
        thumb_mcp = 2


    

    cv2.imshow("video", img)

    cv2.waitKey(1)