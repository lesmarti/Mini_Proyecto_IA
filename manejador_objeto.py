import random

# Definir los iconos y áreas
icono_pos = (150, 50)  # Cuadro blanco 
icono_basura_pos = (150, 150)  # Cuadro rojo 
tamano_icono = 80

# Lista de pelotas
pelotas = []
pelota_seleccionada = None
agarrando_icono = False

# Función para agregar una nueva pelota
def agregar_pelota():
    pelotas.append({
        'x': random.randint(200, 600),
        'y': random.randint(150, 400),
        'radio': 40,
        'agarrada': False
    })

# Función para verificar si un punto está dentro de un área
def esta_en_icono(x, y, icono_pos):
    return (icono_pos[0] - tamano_icono // 2) <= x <= (icono_pos[0] + tamano_icono // 2) and \
           (icono_pos[1] - tamano_icono // 2) <= y <= (icono_pos[1] + tamano_icono // 2)

# Función para verificar si el dedo está sobre el área del icono de basura
def eliminar_pelota(index_x, index_y):
    global pelota_seleccionada
    if esta_en_icono(index_x, index_y, icono_basura_pos) and pelota_seleccionada:
        pelotas.remove(pelota_seleccionada)
        pelota_seleccionada = None

# Función para verificar si se debe agarrar o mover una pelota
def manejar_pelotas(index_x, index_y, gesto_agarre):
    global pelota_seleccionada, agarrando_icono

    if gesto_agarre and pelota_seleccionada is None:
        for pelota in pelotas:
            if (pelota['x'] - pelota['radio'] <= index_x <= pelota['x'] + pelota['radio']) and \
               (pelota['y'] - pelota['radio'] <= index_y <= pelota['y'] + pelota['radio']):
                pelota_seleccionada = pelota
                pelota['agarrada'] = True
                break

    # Si ya se está agarrando una pelota, actualizar su posición
    if pelota_seleccionada:
        if gesto_agarre:
            pelota_seleccionada['x'], pelota_seleccionada['y'] = index_x, index_y
        else:
            pelota_seleccionada['agarrada'] = False
            pelota_seleccionada = None
