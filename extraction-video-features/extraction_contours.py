import cv2
import numpy as np
cap = cv2.VideoCapture("formas-geometricas.mov")
triangle = 0
rectangle = 0
circle = 0

list_order = []
status = 4
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_COMPLEX

    y, x, rgb = frame.shape

    padding = 83

    start_point = (int((x/2)-padding), int((y/2)-padding))
    end_point = (int((x/2)+padding), int((y/2)+padding))
        #    B   R   G
    color = (0, 255, 0)

    thickness = 2 # BORDER

    frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
    ret, imagem_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
    imagem_trat = img[start_point[1]:end_point[1],start_point[0]:end_point[0]]

    contorno, hierarquia = cv2.findContours(imagem_trat, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    key = cv2.waitKey(1)
    if np.mean(imagem_trat) > 100:
        status = 0
        for idx, obj in enumerate(contorno):
            perimetro = cv2.arcLength(obj, True)
            poligono = cv2.approxPolyDP(obj, 0.01 * perimetro, True)
            if len(poligono) == 3:
                triangle += 1
                break
            elif len(poligono) == 4:
                rectangle += 1
                break
            elif len(poligono) == 2:
                circle += 1
                break

    else:
        soma = rectangle+triangle+circle
        if triangle > soma*0.50:
            list_order.append("Triangle")
            triangle = 0
            rectangle = 0
            circle = 0
            status = 4
        if rectangle > soma*0.50:
            list_order.append("Rectangle")
            triangle = 0
            rectangle = 0
            circle = 0
            status = 4
        if circle > soma*0.50:
            list_order.append("Circle")
            triangle = 0
            rectangle = 0
            circle = 0
            status = 4

    cv2.imshow('frame', frame)
    cv2.imshow('frame_trat', imagem_trat)
    if key & 0xFF == ord('q'):
        break

    if key & 0xFF == ord('p'):
        cv2.waitKey(-1)


print(list_order)

cap.release()
cv2.destroyAllWindows()