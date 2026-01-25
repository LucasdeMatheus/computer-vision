import cv2
import pickle


img = cv2.imread("project1/estacionamento.png")

spaces = []

for i in range(69):
    space = cv2.selectROI('spaces', img, False)
    cv2.destroyWindow('spaces')
    spaces.append((space))

    for x, y, w, h in spaces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

with open('spaces.pkl', 'wb') as file:
    pickle.dump(spaces, file)