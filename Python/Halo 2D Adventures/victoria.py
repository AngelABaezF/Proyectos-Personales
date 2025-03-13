import pygame
import sys
import math
import random
import time

def victoria():
    # Inicialización de Pygame
    pygame.init()
    
    musica_victoria = pygame.mixer.Sound("sonidos/victoria.mp3")
    musica_victoria.play()
    
    background = pygame.image.load("imagenes/backgroundSurvival.png")
    background = pygame.transform.scale(background, (800,600))

    # Dimensiones de la pantalla
    pantalla_ancho = 800
    pantalla_alto = 600


    # Colores
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (150, 150, 150)
    
    # Configuración de la pantalla
    pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
    
    font = pygame.font.Font(None, 36)
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 360 <= event.pos[0] <= 410 and 10 <= event.pos[1] <= 50:
                    # Hacer clic en el botón de salida
                    musica_victoria.stop()
                    import menu
                    menu.menu()
                
        # Limpiar la pantalla
        pantalla.blit(background,(0,0))
        # Boton de salida
        pygame.draw.rect(pantalla, (200,200,200), (360, 10, 50, 40))
        
        # Mostrar el contador de cuadrados rojos eliminados

        victoria = font.render(f'VICTORIA', True, (0,255,0))
        pantalla.blit(victoria, (pantalla_ancho/2-60, pantalla_alto/2-7.5))

        # Actualizar la pantalla
        pygame.display.update()
        pygame.time.delay(15)
        

    # Finalizar Pygame
    pygame.quit()
    sys.exit()

# Ejecutar la función del juego
if __name__ == "__main__":
    victoria()
