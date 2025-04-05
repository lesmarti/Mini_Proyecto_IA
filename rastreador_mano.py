import cv2
import mediapipe as mp

mp_manos = mp.solutions.hands
manos = mp_manos.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_dibujo = mp.solutions.drawing_utils

# Función  detectar si el gesto es un agarre
def es_gesto_agarre(marcadores_mano):
    punta_pulgar = marcadores_mano.landmark[mp_manos.HandLandmark.THUMB_TIP]
    punta_indice = marcadores_mano.landmark[mp_manos.HandLandmark.INDEX_FINGER_TIP]
    return abs(punta_pulgar.x - punta_indice.x) < 0.05 and abs(punta_pulgar.y - punta_indice.y) < 0.05

# Función para obtener la posición del dedo índice y si se está realizando el gesto de agarre
def obtener_posicion_mano(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = manos.process(frame_rgb)

    indice_x, indice_y = -1, -1
    gesto_agarre = False

    if resultados.multi_hand_landmarks:
        for marcadores_mano in resultados.multi_hand_landmarks:
            punta_indice = marcadores_mano.landmark[mp_manos.HandLandmark.INDEX_FINGER_TIP]
            indice_x, indice_y = int(punta_indice.x * frame.shape[1]), int(punta_indice.y * frame.shape[0])
            gesto_agarre = es_gesto_agarre(marcadores_mano)
            mp_dibujo.draw_landmarks(frame, marcadores_mano, mp_manos.HAND_CONNECTIONS)

    return indice_x, indice_y, gesto_agarre
