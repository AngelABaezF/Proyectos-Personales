import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
pantalla_ancho, pantalla_alto = 800, 600

# Colores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREY = (150, 150, 150)

# Configuración de la ventana
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
pygame.display.set_caption("Movimiento y disparo")

# Reloj para controlar la velocidad del juego
clock = pygame.time.Clock()

# Lista para almacenar datos de los cuadrados y disparos
cuadrados = [
    {"x": 800, "y": 300, "velocidad": -5, "disparos": []},
    {"x": 800, "y": 300, "velocidad": -5, "disparos": []},
]

# Función para dibujar un cuadrado
def draw_square(x, y, color):
    pygame.draw.rect(pantalla, color, (x, y, 50, 50))

# Función para dibujar los disparos
def draw_shots(disparos, color):
    for disparo in disparos:
        pygame.draw.rect(pantalla, color, disparo)

# Función principal
def main():
    global cuadrados

    tiempo_nuevo_cuadrado = pygame.time.get_ticks() + 10000  # Nuevo cuadrado cada 10 segundos

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tiempo_actual = pygame.time.get_ticks()

        # Generar un nuevo cuadrado cada 10 segundos
        if tiempo_actual > tiempo_nuevo_cuadrado:
            nuevo_cuadrado = {"x": 800, "y": 300, "velocidad": -5, "disparos": []}
            cuadrados.append(nuevo_cuadrado)
            tiempo_nuevo_cuadrado = tiempo_actual + 10000  # Reiniciar el temporizador

        for cuadrado in cuadrados:
            # Mover el cuadrado
            if cuadrado["x"] >= 499:
                cuadrado["x"] += cuadrado["velocidad"]

            # Verificar si el cuadrado llegó a x=499
            if cuadrado["x"] <= 499:
                # Crear un nuevo disparo cada 5 frames
                if tiempo_actual % 15 == 1:
                    disparo = pygame.Rect(cuadrado["x"], cuadrado["y"] + 25, 10, 5)
                    cuadrado["disparos"].append(disparo)

            # Mover los disparos
            cuadrado["disparos"] = [disparo for disparo in cuadrado["disparos"] if disparo.x > 0]
            for disparo in cuadrado["disparos"]:
                disparo.x -= 5  # Velocidad del disparo

        # Limpiar la pantalla
        pantalla.fill((0, 0, 0))

        # Dibujar los cuadrados y los disparos
        for cuadrado in cuadrados:
            draw_square(cuadrado["x"], cuadrado["y"], WHITE)
            draw_shots(cuadrado["disparos"], GREY)

        # Actualizar la ventana
        pygame.display.flip()

        # Establecer el FPS
        clock.tick(30)

if __name__ == "__main__":
    main()