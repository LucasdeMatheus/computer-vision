import cv2
import mediapipe as mp
import math

# Webcam
video = cv2.VideoCapture(1)

# Face Mesh
mpFaceMesh = mp.solutions.face_mesh
FaceMesh = mpFaceMesh.FaceMesh(max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5)

while True:
    ret, img = video.read()
    if not ret:
        break

    h, w, _ = img.shape
    RGBvideo = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = FaceMesh.process(RGBvideo)

    if results.multi_face_landmarks:
        for face in results.multi_face_landmarks:

            # --------- OLHO ESQUERDO ---------
            y159 = int(face.landmark[159].y * h)  # pálpebra superior
            y145 = int(face.landmark[145].y * h)  # pálpebra inferior
            x33  = int(face.landmark[33].x  * w)  # canto esquerdo
            x133 = int(face.landmark[133].x * w)  # canto direito

            eye_height_left = abs(y159 - y145)
            eye_width_left  = abs(x133 - x33)
            ear_left = eye_height_left / eye_width_left

            # --------- OLHO DIREITO ---------
            y386 = int(face.landmark[386].y * h)
            y374 = int(face.landmark[374].y * h)
            x362 = int(face.landmark[362].x * w)
            x263 = int(face.landmark[263].x * w)

            eye_height_right = abs(y386 - y374)
            eye_width_right  = abs(x263 - x362)
            ear_right = eye_height_right / eye_width_right

            # --------- LÓGICA FINAL ---------
            EAR_THRESHOLD = 0.18

            eyes_closed = False
            if ear_left < EAR_THRESHOLD and ear_right < EAR_THRESHOLD:
                eyes_closed = True

            # Texto e cor
            text = "olhos fechados" if eyes_closed else "olhos abertos"
            color = (0, 0, 255) if eyes_closed else (0, 255, 0)

            cv2.putText(img, text, (40, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 5)


    cv2.imshow("video", img)

    cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()
