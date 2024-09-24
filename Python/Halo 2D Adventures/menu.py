import pygame
import sys

# Inicialización de Pygame
pygame.init()

#Cargamos los sprites
#Background
background = pygame.image.load("imagenes/menu.jpeg")
background = pygame.transform.scale(background, (800,600))

musica_menu = pygame.mixer.Sound("sonidos/menu.mp3")

# Dimensiones de la pantalla
pantalla_ancho = 800
pantalla_alto = 600

# Colores
black = (0, 0, 0)
white = (255, 255, 255)
gray = (210,210,210)

# Configuración de la pantalla
pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))

# Coordenadas del centro de la pantalla
centro_x = pantalla_ancho // 2
centro_y = pantalla_alto // 2

# Tamaño de los rectángulos
rectangulo_ancho = 200
rectangulo_alto = 50

# Coordenadas para los tres rectángulos en el centro
rectangulo1_x = centro_x - rectangulo_ancho // 2
rectangulo1_y = centro_y - rectangulo_alto // 2 + 50

rectangulo2_x = centro_x - rectangulo_ancho // 2
rectangulo2_y = centro_y - rectangulo_alto // 2 - 50

rectangulo3_x = centro_x - rectangulo_ancho // 2
rectangulo3_y = centro_y - rectangulo_alto // 2 + 150

# Función que contiene el menú
def menu():
    running = True
    musica_menu.play()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if rectangulo2_x <= event.pos[0] <= rectangulo2_x + rectangulo_ancho and rectangulo2_y <= event.pos[1] <= rectangulo2_y + rectangulo_alto:
                    import nivel
                    musica_menu.stop()
                    nivel.juego()
                elif rectangulo1_x <= event.pos[0] <= rectangulo1_x + rectangulo_ancho and rectangulo1_y <= event.pos[1] <= rectangulo1_y + rectangulo_alto:
                    import wardog
                    musica_menu.stop()
                    wardog.juego()
                elif rectangulo3_x <= event.pos[0] <= rectangulo3_x + rectangulo_ancho and rectangulo3_y <= event.pos[1] <= rectangulo3_y + rectangulo_alto:
                    import survival
                    musica_menu.stop()
                    survival.juego()

        # Limpiar la pantalla
        pantalla.blit(background, (0,0))

        # Dibujar los tres rectángulos
        pygame.draw.rect(pantalla, gray, (rectangulo1_x, rectangulo1_y, rectangulo_ancho, rectangulo_alto))
        pygame.draw.rect(pantalla, gray, (rectangulo2_x, rectangulo2_y, rectangulo_ancho, rectangulo_alto))
        pygame.draw.rect(pantalla, gray, (rectangulo3_x, rectangulo3_y, rectangulo_ancho, rectangulo_alto))
        
        #Dibujar el borde de los botones
        pygame.draw.rect(pantalla, black, (rectangulo1_x, rectangulo1_y, rectangulo_ancho, rectangulo_alto), 2)
        pygame.draw.rect(pantalla, black, (rectangulo2_x, rectangulo2_y, rectangulo_ancho, rectangulo_alto), 2)
        pygame.draw.rect(pantalla, black, (rectangulo3_x, rectangulo3_y, rectangulo_ancho, rectangulo_alto), 2)

        # Actualizar la pantalla
        pygame.display.update()

    # Finalizar Pygame
    pygame.quit()
    sys.exit()

# Llamar a la función del menú
menu()