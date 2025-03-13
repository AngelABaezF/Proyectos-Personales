import pygame
import sys
import math
import random
import time

def juego():
    # Inicialización de Pygame
    pygame.init()
    musica_wardog = pygame.mixer.Sound("sonidos/wardog.mp3")
    
    musica_wardog.play()

    #Cargamos los sprites
    #Background
    background = pygame.image.load("imagenes/backgroundWardog.png")
    background = pygame.transform.scale(background, (800,600))
    
    pelican = pygame.image.load("imagenes/pelican_mini.png")
    pelican = pygame.transform.scale(pelican, (250, 150))
    pelican_x = 0
    pelican_ancho = 250
    pelican_golpes = 0
    
    disparo = pygame.image.load("imagenes/disparo_3.png")
    disparo = pygame.transform.scale(disparo, (20, 30))

        

    
    #Funcion para cargar una lista de imagenes para animaciones.
    def cargar_imagenes(prefijo, sufijo, n, escala):
        images = []
        for i in range (1,n+1):
            image = pygame.image.load(prefijo + str(i) + sufijo)
            image = pygame.transform.scale(image, escala)
            images.append(image)
        return images

    def mostrar_animacion(n, images, x, y):
        frame = int(time.time()*(n-1))%len(images)
        pantalla.blit(images[frame], (x, y))
        
    warthog = cargar_imagenes("imagenes/warthog/warthog_", ".png", 4, (200,100))
    banshee = cargar_imagenes("imagenes/banshee_b/banshee_", ".png", 3, (110,50))
    explosion = cargar_imagenes("imagenes/explosion/explosion_",".png", 7, (50,100))
    
    # Dimensiones de la pantalla
    pantalla_ancho = 800
    pantalla_alto = 600
    xbackground1 = 0
    xbackground2 = 800

    # Colores
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (150, 150, 150)

    # Configuración de la pantalla
    pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))

    # Cubo
    cuadrado_tamaño = 50
    cuadrado_x = 0
    cuadrado_y = 540
    cuadrado_posicion_originaly = 540
    cuadrado_velocidad = 2

    # Velocidad de movimiento
    salto_distancia = 5
    salto_duracion = 20
    salto_contador = 0
    saltando = False

    # Altura del cuadrado
    cuadrado_altura_normal = 50
    cuadrado_altura_agachado = 25
    actualizar_agachado = False
    cuadrado_altura = cuadrado_altura_normal  # Inicialmente en altura normal

    # Movimiento horizontal
    moverse_izquierda = False
    moverse_derecha = False

    # Disparo
    velocidad_disparo = 5
    projectiles = []
    salida_disparo_x, salida_disparo_y = 80, 500


    # Variable para rastrear si el botón derecho del ratón está presionado
    boton_derecho_presionado = False

    # Temporizador para controlar la frecuencia de los disparos
    temporizador_disparo = 0
    frecuencia_disparo = 7  # Puedes ajustar esta frecuencia según tus preferencias

    # Velocidad del cuadrado rojo
    cuadrado_rojo_velocidad = 1  # Ajusta esta velocidad según lo que desees

    # Función para disparar automáticamente hacia el cursor
    def disparo_automatico():
        nonlocal temporizador_disparo
        if temporizador_disparo >= frecuencia_disparo:
            disparar_hacia_cursor()
            temporizador_disparo = 0  # Reiniciar el temporizador

    # Función para disparar hacia el cursor
    def disparar_hacia_cursor():
        cursor_x, cursor_y = pygame.mouse.get_pos()
        delta_x = cursor_x - salida_disparo_x
        delta_y = cursor_y - salida_disparo_y
        distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
        if distancia == 0:
            return

        velocidad_x = (delta_x / distancia) * velocidad_disparo
        velocidad_y = (delta_y / distancia) * velocidad_disparo


        nuevo_disparo = {'x': salida_disparo_x, 'y': salida_disparo_y,
                              'velocidad_x': velocidad_x, 'velocidad_y': velocidad_y}
        projectiles.append(nuevo_disparo)

    class CuadradoRojo:
        def __init__(self, x, y):
            self.x = x
            self.y = 150
            cuadrado_rojo_velocidad = 1
            self.alto = 50
            self.ancho = 75
            self.color = (255, 0, 0)
            self.colisiones = 0

        def draw(self, pantalla):
            mostrar_animacion(3, banshee, self.x, self.y)

        def colisionar(self):
                self.colisiones += 1

        def eliminar(self):
            return self.colisiones >= 10

    # Lista para almacenar los cuadrados rojos
    cuadrados_rojos = []

    # Crear un objeto CuadradoRojo inicial
    cuadrados_rojos.append(CuadradoRojo(700, 150))

    # Contador de cuadrados rojos eliminados
    cuadrados_rojos_eliminados = 0

    # Bucle principal del juego
    running = True
    automatico = False

    # Función para generar un nuevo cuadrado rojo
    def generar_cuadrado_rojo():
        x = pantalla_ancho
        y = 150  # Altura fija
        nuevo_cuadrado_rojo = CuadradoRojo(x, y)
        cuadrados_rojos.append(nuevo_cuadrado_rojo)

    generar_cuadrado_rojo()  # Generar el primer cuadrado rojo

    # Fuente para el marcador de cuadrados rojos eliminados
    font = pygame.font.Font(None, 36)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and not boton_derecho_presionado:
                    automatico = not automatico
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not automatico:
                # Disparar cuando se hace clic izquierdo hacia el cursor
                disparar_hacia_cursor()
                if 360 <= event.pos[0] <= 410 and 10 <= event.pos[1] <= 50:
                    # Hacer clic en el botón de salida
                    musica_wardog.stop()
                    import menu
                    menu.menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and automatico:
                # Botón derecho del ratón presionado
                boton_derecho_presionado = True
                if 360 <= event.pos[0] <= 410 and 10 <= event.pos[1] <= 50:
                    # Hacer clic en el botón de salida
                    running = False
                    import menu
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and automatico:
                # Botón derecho del ratón liberado
                boton_derecho_presionado = False
        # Actualizar la posición de los cuadrados rojos
        for cuadrado_rojo in cuadrados_rojos:
            cuadrado_rojo.x -= cuadrado_rojo_velocidad

        # Incrementar el temporizador de disparo
        if temporizador_disparo < frecuencia_disparo:
            temporizador_disparo += 1

        # Eliminar cuadrados rojos si han sido alcanzados por 5 balas
        for i, cuadrado_rojo in enumerate(cuadrados_rojos):
            if cuadrado_rojo.x <= pelican_x + pelican_ancho:
                cuadrado_rojo.colisionar()
            for j, projectil in enumerate(projectiles):
                if cuadrado_rojo and cuadrado_rojo.x < projectil['x'] < cuadrado_rojo.x + cuadrado_rojo.ancho and cuadrado_rojo.y < projectil['y'] < cuadrado_rojo.y + cuadrado_rojo.alto:
                    cuadrado_rojo.colisionar()
                    del projectiles[j]


        # Incrementar el contador de cuadrados rojos eliminados
        for cuadrado_rojo in cuadrados_rojos:
            if cuadrado_rojo.eliminar() and cuadrado_rojo.x > 250:
                cuadrados_rojos_eliminados += 1
            elif cuadrado_rojo.eliminar() and cuadrado_rojo.x <= 250:
                pelican_golpes += 1
            if cuadrados_rojos_eliminados == 15:
                musica_wardog.stop()
                import victoria
                victoria.victoria()

        # Eliminar los cuadrados rojos que han sido alcanzados por 5 balas
        cuadrados_rojos = [cuadrado_rojo for cuadrado_rojo in cuadrados_rojos if not cuadrado_rojo.eliminar()]

        # Generar nuevos cuadrados rojos de forma aleatoria
        if random.randint(1, 200) == 1:
            generar_cuadrado_rojo()

        # Actualizar la posición de los proyectiles
        for projectil in projectiles:
            projectil['x'] += projectil['velocidad_x']
            projectil['y'] += projectil['velocidad_y']

        # Llamar a la función de disparo automático mientras el botón derecho del ratón está presionado
        if boton_derecho_presionado:
            disparo_automatico()

        # Limpiar la pantalla
        pantalla.blit(background, (xbackground1,0))
        if xbackground1 > -800:
            xbackground1 -= 2
        else: xbackground1 = 0
        pantalla.blit(background, (xbackground2,0))
        if xbackground2 > 0:
            xbackground2 -= 2
        else: xbackground2 = 800

        # Dibujar el cuadrado
        mostrar_animacion(4, warthog, cuadrado_x, 495)

        # Boton de salida
        pygame.draw.rect(pantalla, white, (360, 10, 50, 40))

        # Dibujar los proyectiles
        for projectil in projectiles:
            if math.sqrt((projectil['x'] - salida_disparo_x)**2 + (projectil['y'] - 540)**2)< 75:
                pantalla.blit(disparo, (salida_disparo_x-4, salida_disparo_y - 33 ))
            pygame.draw.circle(pantalla, (212,175,55), (projectil['x'], projectil['y']), 2)

        # Dibujar los cuadrados rojos
        for cuadrado_rojo in cuadrados_rojos:
            cuadrado_rojo.draw(pantalla)
            
        if pelican_golpes < 6:
            pantalla.blit(pelican, (pelican_x,75))
        else:
            musica_wardog.stop()
            import derrota
            derrota.victoria()
        print(pelican_golpes)
        


        # Mostrar el contador de cuadrados rojos eliminados
        marcador = font.render(f'Puntos: {cuadrados_rojos_eliminados}', True, white)
        pantalla.blit(marcador, (10, 10))

        # Actualizar la pantalla
        pygame.display.update()
        pygame.time.delay(15)

    # Finalizar Pygame
    pygame.quit()
    sys.exit()

# Ejecutar la función del juego
if __name__ == "__main__":
    juego()