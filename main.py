import cv2
import time
from rastreador_mano import obtener_posicion_mano
from manejador_objeto import agregar_pelota, manejar_pelotas, eliminar_pelota, icono_pos, icono_basura_pos, tamano_icono, esta_en_icono, pelotas

# Iniciar la cámara
cap = cv2.VideoCapture(0)
time.sleep(1)

# Inicializar la primera pelota
agregar_pelota()

agarrando_icono = False
pelota_seleccionada = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Obtener posición de la mano y gesto de agarre
    index_x, index_y, gesto_agarre = obtener_posicion_mano(frame)

    # Verificar si se agrega una pelota
    if gesto_agarre and esta_en_icono(index_x, index_y, icono_pos) and not agarrando_icono:
        agregar_pelota()
        agarrando_icono = True

    if not gesto_agarre:
        agarrando_icono = False

    # Manejar pelotas y eliminarlas si es necesario
    manejar_pelotas(index_x, index_y, gesto_agarre)
    eliminar_pelota(index_x, index_y)

    # Dibujar los iconos
    cv2.rectangle(frame, (icono_pos[0] - tamano_icono // 2, icono_pos[1] - tamano_icono // 2),
                  (icono_pos[0] + tamano_icono // 2, icono_pos[1] + tamano_icono // 2),
                  (255, 255, 255), -1)
    cv2.rectangle(frame, (icono_basura_pos[0] - tamano_icono // 2, icono_basura_pos[1] - tamano_icono // 2),
                  (icono_basura_pos[0] + tamano_icono // 2, icono_basura_pos[1] + tamano_icono // 2),
                  (0, 0, 255), -1)

    # Dibujar las pelotas
    for pelota in pelotas:
        color = (0, 255, 255) if not pelota['agarrada'] else (255, 0, 0)
        cv2.circle(frame, (pelota['x'], pelota['y']), pelota['radio'], color, -1)

    # Mostrar la ventana
    cv2.imshow('Cerrar la camara', frame)
    if cv2.waitKey(1) & 0xFF == ord('w'):
        break

cap.release()
cv2.destroyAllWindows()

