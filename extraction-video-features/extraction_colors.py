# Bibliotecas
import cv2

import numpy as np

cap = cv2.VideoCapture("objetos-coloridos.mov")
r_count = 0
g_count = 0
b_count = 0

list_order = []
status = 4
while cap.isOpened():
    ret, frame = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)

    # print(fps)
    key = cv2.waitKey(1)
    if not ret:
        break
    if key & 0xFF == ord('q'):
        break

    if key & 0xFF == ord('p'):
        cv2.waitKey(-1)

    y, x, rgb = frame.shape

    padding = 83

    start_point = (int((x / 2) - padding), int((y / 2) - padding))
    end_point = (int((x / 2) + padding), int((y / 2) + padding))
    #    B   R   G
    color = (0, 255, 0)

    thickness = 2  # BORDER

    imagem_trat = frame[start_point[1]:end_point[1], start_point[0]:end_point[0]]
    b, g, r = cv2.split(imagem_trat)

    frame = cv2.rectangle(frame, start_point, end_point, color, thickness)

    # print(np.mean(r), np.mean(g), np.mean(b))
    if np.mean(r) < 252 or np.mean(g) < 252 or np.mean(b) < 252:

        if np.mean(r) > np.mean(g) and np.mean(r) > np.mean(b) and status != 0:

            list_order.append("Red")
            status = 0
        elif np.mean(g) > np.mean(r) and np.mean(g) > np.mean(b) and status != 1:

            list_order.append("Gree")
            status = 1
        elif np.mean(b) > np.mean(r) and np.mean(b) > np.mean(g) and status != 2:

            list_order.append("Blue")
            status = 2

    else:
        status = 4

    cv2.imshow('frame', frame)
    cv2.imshow('frame_trat', imagem_trat)

print(list_order)

cap.release()
cv2.destroyAllWindows()
