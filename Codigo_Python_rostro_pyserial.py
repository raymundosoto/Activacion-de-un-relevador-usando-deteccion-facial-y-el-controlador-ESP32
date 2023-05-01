# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 12:03:34 2023

@author: Precision
"""

import cv2
import time
import serial


# Cargar el clasificador preentrenado de rostros
face_cascade = cv2.CascadeClassifier('C:/Users/Precision/anaconda3/envs/mediapipe_env/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# Inicializar la cámara web
cap = cv2.VideoCapture(0)



while True:
    # Leer un fotograma de la cámara web
    ret, img = cap.read()

    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar los rostros en el fotograma
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces)>0:
        print('Rostro detectado a')
        print("Activación del relevador")
        ser = serial.Serial('COM6', 9600, timeout=0.050)
        ser.write('a'.encode())
        
        
    else:
        print('Rostro No detectado, no hay activación del relevador')
        ser = serial.Serial('COM6', 9600, timeout=0.050)
        ser.write('b'.encode())
        
    # Dibujar un rectángulo alrededor de cada rostro detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Mostrar el fotograma con los rostros detectados
    cv2.imshow('img', img)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ser.close()
    time.sleep(1)
# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
