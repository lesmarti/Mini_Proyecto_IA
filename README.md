# Información sobre cómo se realizó el proyecto
Este proyecto es como un juego interactivo que usa la cámara de tu computadora o dispositivo para seguir los movimientos de tus manos en tiempo real. Usamos una librería llamada **MediaPipe** que nos permite rastrear las manos, y con eso el sistema te permite manipular unas pelotas virtuales en la pantalla. La idea es que, con tus gestos, puedas mover las pelotas, agarrarlas o incluso eliminarlas, todo de manera dinámica y bastante divertida.

#Link del video 
https://drive.google.com/file/d/11yGEwZydtCWefIzYaxtAhdzfzWfQeM0P/view?usp=sharing

# Estructura General del Proyecto

# rastreador_mano.py
Este archivo es el que se encarga de hacer el trabajo pesado con las manos. Básicamente, toma las imágenes de la cámara y las pasa por el modelo de **MediaPipe**, que es un sistema de inteligencia artificial que nos dice dónde están las manos y, dentro de ellas, qué dedo está en qué posición. Lo más interesante es que **MediaPipe** puede detectar hasta 21 puntos diferentes en cada mano, o sea, no solo la mano como tal, sino también los dedos y la muñeca.

## Cómo funciona:
- **Detección de la mano**: Lo que hace el archivo es que toma las imágenes de la cámara y las pasa por MediaPipe, que se encarga de detectar la mano y te devuelve un montón de coordenadas que corresponden a puntos clave en la mano (como los dedos). Esta parte es fundamental porque sin eso no podríamos seguir los movimientos de la mano.
  
- **Detección de gestos**: Además de detectar las manos, el sistema también puede detectar algunos gestos. Un gesto que usamos es el de "agarrar". Si el pulgar y el índice se acercan mucho entre sí, el sistema interpreta que estás agarrando algo. Esto es útil para interactuar con las pelotas más tarde.

# manejador_objeto.py
Este archivo es el encargado de las pelotas virtuales en la pantalla. Piensa en él como el que se encarga de gestionar todo lo relacionado con las pelotas: cómo agregarlas a la pantalla, cómo moverlas cuando las agarras y, lo más importante, cómo eliminarlas cuando las "lanzas" a la basura.

## Cómo funciona:
- **Agregar pelotas**: Al arrancar el proyecto, el archivo agrega pelotas a la escena en posiciones aleatorias. No hay mucha lógica detrás de esto, solo poner algunas pelotas en lugares distintos para que el usuario pueda empezar a interactuar con ellas.

- **Mover las pelotas**: Aquí es donde entra lo divertido. Cuando el usuario hace un gesto de "agarrar", el sistema identifica qué pelota está más cerca y la "agarra". Luego, la pelota se va moviendo por la pantalla a medida que el usuario mueve su mano, como si estuvieras realmente moviendo la pelota.

- **Eliminar pelotas**: Si logras mover una pelota hacia un área específica (como un icono de basura), el sistema la elimina. Esto lo hace verificando constantemente si la pelota ha llegado a esa área, y si es así, la borra de la pantalla. Es como si estuvieras tirando una pelota a la basura.

# main.py
Este archivo es el cerebro del proyecto. Es el que conecta todo: la cámara, la detección de la mano y el manejo de las pelotas. Su función es capturar el video en vivo desde la cámara, analizar cada fotograma para ver qué está pasando con la mano y las pelotas, y luego actualizar todo en la pantalla. Si el usuario mueve la mano o hace algún gesto, este archivo se encarga de hacer que todo se vea bien en la interfaz.

## Cómo funciona:
- **Captura de cámara**: Este archivo comienza tomando las imágenes en vivo de la cámara. Cada fotograma se procesa de inmediato para buscar las manos y las pelotas. Esto hace que todo se vea en tiempo real, sin demora.
  
- **Procesamiento de la mano**: A través de la función `detectar_mano()` que viene de `rastreador_mano.py`, este archivo encuentra las manos en los fotogramas. Luego, con las coordenadas de los dedos, detecta gestos como el "agarrar". Sin esta parte, el proyecto no sabría cuándo estás moviendo una pelota.

- **Interacción con las pelotas**: Cuando se detecta que el usuario está haciendo un gesto de "agarrar", el archivo interactúa con el archivo `manejador_objeto.py` para mover la pelota. Si el gesto es para eliminarla, el sistema la lanza hacia el área de la basura, y listo, desaparece.

- **Visualización**: Al final, el archivo actualiza todo lo que ves en pantalla. Así, en tiempo real, puedes ver las pelotas moverse, eliminarlas o agarrarlas según los gestos que hagas con tus manos. Todo esto se actualiza constantemente, haciendo que la experiencia sea dinámica y fluida.

