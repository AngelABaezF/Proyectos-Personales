import pygame
import sys
import math
import random
import time

def juego():
    # Inicialización de Pygame
    pygame.init()
    
    musica_survival = pygame.mixer.Sound("sonidos/survival.mp3")
    musica_survival.play()
    pistola = pygame.mixer.Sound("sonidos/pistola.mp3")
    
    salud=100

    #Cargamos los sprites
    #Background
    background = pygame.image.load("imagenes/backgroundSurvival.png")
    background = pygame.transform.scale(background, (800,600))
    
    disparo = pygame.image.load("imagenes/fuego_disparo_1.png")
    disparo = pygame.transform.scale(disparo, (30, 20))
    disparo2 = pygame.image.load("imagenes/fuego_disparo_2.png")
    disparo2 = pygame.transform.scale(disparo2, (30, 20))
    bola_de_plasma_2 = pygame.image.load("imagenes/bola_plasma_2.png")
    bola_de_plasma_2 = pygame.transform.scale(bola_de_plasma_2, (30,20))
    bola_de_plasma_3 = pygame.image.load("imagenes/bola_plasma_3.png")
    bola_de_plasma_3 = pygame.transform.scale(bola_de_plasma_3, (30,20))
    vida1 = pygame.image.load("imagenes/vidas/vidas_1.png")
    vida1 = pygame.transform.scale(vida1, (200,50))
    vida2 = pygame.image.load("imagenes/vidas/vidas_2.png")
    vida2 = pygame.transform.scale(vida2, (200,50))
    vida3 = pygame.image.load("imagenes/vidas/vidas_3.png")
    vida3 = pygame.transform.scale(vida3, (200,50))
    vida4 = pygame.image.load("imagenes/vidas/vidas_4.png")
    vida4 = pygame.transform.scale(vida4, (200,50))
    vida5 = pygame.image.load("imagenes/vidas/vidas_5.png")
    vida5 = pygame.transform.scale(vida5, (200,50))
    vida6 = pygame.image.load("imagenes/vidas/vidas_6.png")
    vida6 = pygame.transform.scale(vida6, (200,50))
    vida7 = pygame.image.load("imagenes/vidas/vidas_7.png")
    vida7 = pygame.transform.scale(vida7, (200,50))
    vida8 = pygame.image.load("imagenes/vidas/vidas_8.png")
    vida8 = pygame.transform.scale(vida8, (200,50))
    vida9 = pygame.image.load("imagenes/vidas/vidas_9.png")
    vida9 = pygame.transform.scale(vida9, (200,50))

    #Funcion para cargar una lista de imagenes para animaciones.
    def cargar_imagenes(prefijo, sufijo, n, escala):
        images = []
        for i in range (1,n+1):
            image = pygame.image.load(prefijo + str(i) + sufijo)
            image = pygame.transform.scale(image, escala)
            images.append(image)
        return images

    def mostrar_animacion_correr_f(n, images, x, y):
        if moverse_derecha == True and moverse_izquierda == False and actualizar_agachado == False:
            frame = int(time.time()*(n-1))%len(images)
            pantalla.blit(images[frame], (x, y))
    def mostrar_animacion_correr_b(n, images, x, y):
        if moverse_izquierda == True and moverse_derecha == False and actualizar_agachado == False:
            frame = int(time.time()*(n-1))%len(images)
            pantalla.blit(images[frame], (x, y))
    def mostrar_animacion_agachado_f(n, images, x, y):
        if moverse_derecha == True and actualizar_agachado == True and moverse_izquierda == False:
            frame = int(time.time()*(n-1))%len(images)
            pantalla.blit(images[frame], (x, y))
    def mostrar_animacion_agachado_b(n, images, x, y):
        if moverse_izquierda == True and actualizar_agachado == True and moverse_derecha == False:
            frame = int(time.time()*(n-1))%len(images)
            pantalla.blit(images[frame], (x, y))
    def mostrar_animacion(n, images, x, y):
        frame = int(time.time()*(n-1))%len(images)
        pantalla.blit(images[frame], (x, y))
        
    #Personaje
    jefe_correr_f = cargar_imagenes("imagenes/jefe_correr_f/jefe_correr_f_", ".png", 6, (50,100))
    jefe_correr_b = cargar_imagenes("imagenes/jefe_correr_b/jefe_correr_b_", ".png", 6, (50,100))
    jefe_agachado_f = cargar_imagenes("imagenes/jefe_agachado_f/jefe_agachado_f_", ".png", 4, (50,50))
    jefe_agachado_b = cargar_imagenes("imagenes/jefe_agachado_b/jefe_agachado_b_", ".png", 4, (50,50))
    jefe_normal = pygame.image.load("imagenes/jefe_maestro/jefe_maestro_1.png")
    elite_corriendo_f = cargar_imagenes("imagenes/elite_corriendo_f/elite_corriendo_f_", ".png", 6, (50,100))
    elite_corriendo_b = cargar_imagenes("imagenes/elite_corriendo_b/elite_corriendo_b_", ".png", 6, (50,100))
    jefe_normal = pygame.transform.scale(jefe_normal,(50,100))
    jefe_normal_agachado = pygame.image.load("imagenes/jefe_maestro/jefe_agachado_f.png")
    jefe_normal_agachado = pygame.transform.scale(jefe_normal_agachado,(50,50))

    

    # Dimensiones de la pantalla
    pantalla_ancho = 800
    pantalla_alto = 600


    # Colores
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (150, 150, 150)

    # Configuración de la pantalla
    pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))

    # Cubo
    cuadrado_tamaño = 50
    cuadrado_x = 350
    cuadrado_y = 449
    cuadrado_posicion_originaly = 299
    cuadrado_velocidad = 2

    # Velocidad de movimiento
    salto_distancia = 5
    salto_duracion = 20
    salto_contador = 0
    saltando = False

    # Altura del cuadrado
    cuadrado_altura_normal = 100
    cuadrado_altura_agachado = 50
    actualizar_agachado = False
    cuadrado_altura = cuadrado_altura_normal  # Inicialmente en altura normal

    # Movimiento horizontal
    moverse_izquierda = False
    moverse_derecha = False

    # Disparo
    velocidad_disparo = 5
    projectiles = []

    # Variable para rastrear si el botón derecho del ratón está presionado
    boton_derecho_presionado = False

    # Temporizador para controlar la frecuencia de los disparos
    temporizador_disparo = 0
    frecuencia_disparo = 10  # Puedes ajustar esta frecuencia según tus preferencias

    # Velocidad del cuadrado rojo
    cuadrado_rojo_velocidad = 1  # Ajusta esta velocidad según lo que desees

    def actualizar_cuadrado_salto():
        nonlocal cuadrado_y, saltando, salto_contador, actualizar_agachado
        if saltando:
            if salto_contador < salto_duracion:
                cuadrado_y -= salto_distancia
                salto_contador += 1
            else:
                if cuadrado_y < 449:
                    cuadrado_y += salto_distancia
                    if cuadrado_y >= 449:
                        saltando = False
                        salto_contador = 0

    # Función para cambiar la altura del cuadrado cuando se presiona/despresiona la tecla S
    def actualizar_altura_cuadrado(agachado):
        nonlocal cuadrado_altura, cuadrado_y
        if agachado:
            cuadrado_altura = cuadrado_altura_agachado
            cuadrado_y = cuadrado_y + 50
        elif cuadrado_y == 499:
            cuadrado_altura = cuadrado_altura_normal
            cuadrado_y = 449

    # Función para actualizar la posición horizontal
    def actualizar_cuadrado_horizontal():
        nonlocal cuadrado_x
        if moverse_derecha and cuadrado_x < 800:
            cuadrado_x += cuadrado_velocidad
        if moverse_izquierda and cuadrado_x > 0:
            cuadrado_x -= cuadrado_velocidad

    # Función para disparar automáticamente hacia el cursor
    def disparo_automatico():
        nonlocal temporizador_disparo
        if temporizador_disparo >= frecuencia_disparo:
            disparar_hacia_cursor()
            temporizador_disparo = 0  # Reiniciar el temporizador

    # Función para disparar hacia el cursor
    def disparar_hacia_cursor():
        cursor_x, cursor_y = pygame.mouse.get_pos()
        delta_x = cursor_x - cuadrado_x + cuadrado_tamaño
        delta_y = cursor_y - cuadrado_y
        distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
        pistola.play()
        if distancia == 0:
            return

        velocidad_x = (delta_x / distancia) * velocidad_disparo
        velocidad_y = (delta_y / distancia) * velocidad_disparo

        # Condicional para el origen del disparo (si esta agachado)
        if not moverse_izquierda :
            nuevo_disparo = {'x': cuadrado_x + cuadrado_tamaño, 'y': cuadrado_y + 13,
                              'velocidad_x': velocidad_x, 'velocidad_y': velocidad_y}
            pantalla.blit(disparo, (cuadrado_x + cuadrado_tamaño, cuadrado_y + 13))
            print("!!")
        elif moverse_izquierda and moverse_derecha:
            nuevo_disparo = {'x': cuadrado_x + cuadrado_tamaño, 'y': cuadrado_y + 13,
                              'velocidad_x': velocidad_x, 'velocidad_y': velocidad_y}
        elif moverse_izquierda:
            nuevo_disparo = {'x': cuadrado_x , 'y': cuadrado_y + 13,
                              'velocidad_x': velocidad_x, 'velocidad_y': velocidad_y}
            

        projectiles.append(nuevo_disparo)

    
    class CuadradoRojo:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.ancho = 50
            self.alto = 100
            self.color = (255, 0, 0)
            self.colisiones = 0

        def draw(self, pantalla):
            mostrar_animacion(6,elite_corriendo_b,self.x,self.y)
        def colisionar(self):
            self.colisiones += 1

        def eliminar(self):
            return self.colisiones >= 5

    # Lista para almacenar los cuadrados rojos
    cuadrados_rojos = []

    # Crear un objeto CuadradoRojo inicial
    cuadrados_rojos.append(CuadradoRojo(700, 449))

    # Contador de cuadrados rojos eliminados
    cuadrados_rojos_eliminados = 0

    class CuadradoAzul:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.ancho = 50
            self.alto = 100
            self.color = (255, 0, 0)
            self.colisiones = 0

        def draw(self, pantalla):
            mostrar_animacion(6,elite_corriendo_f,self.x,self.y)
            
        def colisionar(self):
            self.colisiones += 1

        def eliminar(self):
            return self.colisiones >= 5

    # Lista para almacenar los cuadrados azules
    cuadrados_azules = []

    # Crear un objeto CuadradoAzul inicial
    cuadrados_azules.append(CuadradoAzul(0, 449))

    # Contador de cuadrados azules eliminados
    cuadrados_azules_eliminados = 0

    # Bucle principal del juego
    running = True
    automatico = False

    # Función para generar un nuevo cuadrado rojo
    def generar_cuadrado_rojo():
        x = pantalla_ancho
        y = 449  # Altura fija
        nuevo_cuadrado_rojo = CuadradoRojo(x, y)
        cuadrados_rojos.append(nuevo_cuadrado_rojo)

    generar_cuadrado_rojo()  # Generar el primer cuadrado rojo

    # Función para generar un nuevo cuadrado azul
    def generar_cuadrado_derecho():
        x = 0  # Comienza desde la izquierda de la pantalla
        y = 449  # Altura fija
        nuevo_cuadrado_derecho = CuadradoAzul(x, y)
        cuadrados_azules.append(nuevo_cuadrado_derecho)

    generar_cuadrado_derecho()  # Generar el primer cuadrado azul

    # Fuente para el marcador de cuadrados rojos eliminados
    font = pygame.font.Font(None, 36)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not saltando and not actualizar_agachado:
                    saltando = True
                elif event.key == pygame.K_d:
                    moverse_derecha = True
                elif event.key == pygame.K_a:
                    moverse_izquierda = True
                elif event.key == pygame.K_r and not boton_derecho_presionado:
                    automatico = not automatico
                elif event.key == pygame.K_s and not saltando:
                    actualizar_altura_cuadrado(True)
                    actualizar_agachado = True  # Cuando se presiona S, agacharse
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    moverse_derecha = False
                elif event.key == pygame.K_a:
                    moverse_izquierda = False
                elif event.key == pygame.K_s:
                    actualizar_altura_cuadrado(False)
                    actualizar_agachado = False  # Cuando se suelta S, volver a altura normal
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not automatico:
                # Disparar cuando se hace clic izquierdo hacia el cursor
                pantalla.blit(disparo, (300,400))
                disparar_hacia_cursor()
                if 360 <= event.pos[0] <= 410 and 10 <= event.pos[1] <= 50:
                    # Hacer clic en el botón de salida
                    musica_survival.stop()
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
            if cuadrado_rojo.x == cuadrado_x:
                salud -= 49
                continue

        # Actualizar la posición de los cuadrados azules
        for cuadrado_derecho in cuadrados_azules:
            cuadrado_derecho.x += cuadrado_rojo_velocidad / 2  # Se mueve más lentamente que los rojos
            if cuadrado_derecho.x == cuadrado_x:
                salud -= 49
                continue

        # Incrementar el temporizador de disparo
        if temporizador_disparo < frecuencia_disparo:
            temporizador_disparo += 1

        # Eliminar cuadrados rojos si han sido alcanzados por 5 balas
        for i, cuadrado_rojo in enumerate(cuadrados_rojos):
            for j, projectil in enumerate(projectiles):
                if cuadrado_rojo and cuadrado_rojo.x < projectil['x'] < cuadrado_rojo.x + cuadrado_rojo.ancho and cuadrado_rojo.y < projectil['y'] < cuadrado_rojo.y + cuadrado_rojo.alto:
                    cuadrado_rojo.colisionar()
                    del projectiles[j]

        # Incrementar el contador de cuadrados rojos eliminados
        for cuadrado_rojo in cuadrados_rojos:
            if cuadrado_rojo.eliminar():
                cuadrados_rojos_eliminados += 1

        # Eliminar los cuadrados rojos que han sido alcanzados por 5 balas
        cuadrados_rojos = [cuadrado_rojo for cuadrado_rojo in cuadrados_rojos if not cuadrado_rojo.eliminar()]

        # Eliminar cuadrados azules si han sido alcanzados por 5 balas
        for i, cuadrado_derecho in enumerate(cuadrados_azules):
            for j, projectil in enumerate(projectiles):
                if cuadrado_derecho and cuadrado_derecho.x < projectil['x'] < cuadrado_derecho.x + cuadrado_derecho.ancho and cuadrado_derecho.y < projectil['y'] < cuadrado_derecho.y + cuadrado_derecho.alto:
                    cuadrado_derecho.colisionar()
                    del projectiles[j]

        # Incrementar el contador de cuadrados azules eliminados
        for cuadrado_derecho in cuadrados_azules:
            if cuadrado_derecho.eliminar():
                cuadrados_azules_eliminados += 1

        # Eliminar los cuadrados azules que han sido alcanzados por 5 balas
        cuadrados_azules = [cuadrado_derecho for cuadrado_derecho in cuadrados_azules if not cuadrado_derecho.eliminar()]

        # Generar nuevos cuadrados rojos de forma aleatoria
        if random.randint(1, 100) == 1:
            generar_cuadrado_rojo()

        # Generar nuevos cuadrados azules de forma aleatoria
        if random.randint(1, 100) == 1:
            generar_cuadrado_derecho()

        # Actualizar posición del cuadrado si está saltando
        actualizar_cuadrado_salto()

        # Actualizar posición horizontal
        actualizar_cuadrado_horizontal()

        # Actualizar la posición de los proyectiles
        for projectil in projectiles:
            projectil['x'] += projectil['velocidad_x']
            projectil['y'] += projectil['velocidad_y']

        # Llamar a la función de disparo automático mientras el botón derecho del ratón está presionado
        if boton_derecho_presionado:
            disparo_automatico()

        # Limpiar la pantalla
        pantalla.blit(background,(0,0))

        # Dibujar la línea horizontal
        pygame.draw.line(pantalla, grey, (0, 550), (pantalla_ancho, 550), 5)

        # Dibujar el cuadrado
        mostrar_animacion_correr_f(6,jefe_correr_f,cuadrado_x,cuadrado_y)
        mostrar_animacion_correr_b(6,jefe_correr_b,cuadrado_x,cuadrado_y)
        mostrar_animacion_agachado_f(4,jefe_agachado_f,cuadrado_x,cuadrado_y)
        mostrar_animacion_agachado_b(4,jefe_agachado_b,cuadrado_x,cuadrado_y)
        if ((moverse_derecha == False and moverse_izquierda == False) or (moverse_derecha == True and moverse_izquierda == True)) and actualizar_agachado == False:
            pantalla.blit(jefe_normal, (cuadrado_x, cuadrado_y))
        if ((moverse_derecha == False and moverse_izquierda == False) or (moverse_derecha == True and moverse_izquierda == True)) and actualizar_agachado == True:
            pantalla.blit(jefe_normal_agachado, (cuadrado_x, cuadrado_y))
            
        # Boton de salida
        pygame.draw.rect(pantalla, (200,200,200), (360, 10, 50, 40))

        # Dibujar los proyectiles
        for projectil in projectiles:
            if math.sqrt((projectil['x'] - cuadrado_x)**2 + (projectil['y'] - cuadrado_y)**2)< 75 and moverse_izquierda and moverse_derecha:
                pantalla.blit(disparo, (cuadrado_x + cuadrado_tamaño,cuadrado_y ))
                print(math.sqrt((projectil['x'] - cuadrado_x)**2 + (projectil['y'] - cuadrado_y)**2))
            elif math.sqrt((projectil['x'] - cuadrado_x)**2 + (projectil['y'] - cuadrado_y)**2)< 75 and moverse_derecha:
                pantalla.blit(disparo, (cuadrado_x + cuadrado_tamaño,cuadrado_y ))
                print(math.sqrt((projectil['x'] - cuadrado_x)**2 + (projectil['y'] - cuadrado_y)**2))
            elif math.sqrt((projectil['x'] - cuadrado_x)**2 + (projectil['y'] - cuadrado_y)**2)< 75 and not moverse_derecha and not moverse_izquierda:
                pantalla.blit(disparo, (cuadrado_x + cuadrado_tamaño,cuadrado_y ))
                print(math.sqrt((projectil['x'] - cuadrado_x)**2 + (projectil['y'] - cuadrado_y)**2))
            elif math.sqrt((projectil['x'] - cuadrado_x)**2 + (projectil['y'] - cuadrado_y)**2)< 75 and moverse_izquierda :
                pantalla.blit(disparo2, (cuadrado_x - 29 ,cuadrado_y ))
                print(math.sqrt((projectil['x'] - cuadrado_x)**2 + (projectil['y'] - cuadrado_y)**2))
            pygame.draw.circle(pantalla, (212,175,55), (projectil['x'], projectil['y']), 2)

        # Dibujar los cuadrados rojos
        for cuadrado_rojo in cuadrados_rojos:
            cuadrado_rojo.draw(pantalla)

        # Dibujar los cuadrados azules
        for cuadrado_derecho in cuadrados_azules:
            cuadrado_derecho.draw(pantalla)
        
        if salud == 100:
            pantalla.blit(vida9, (10,40))
        elif salud>83:
            pantalla.blit(vida8, (10,40))
        elif salud>67:
            pantalla.blit(vida7, (10,40))
        elif salud>51:
            pantalla.blit(vida6, (10,40))
        elif salud>40:
            pantalla.blit(vida5, (10,40))
        elif salud>30:
            pantalla.blit(vida4, (10,40))
        elif salud>20:
            pantalla.blit(vida3, (10,40))
        elif salud>10:
            pantalla.blit(vida2, (10,40))
        elif salud>0:
            pantalla.blit(vida1, (10,40))
        elif salud<=0:
            musica_nivel.stop()
            import derrota
            derrota.victoria()

        # Mostrar el contador de cuadrados rojos eliminados
        marcador_rojo = font.render(f'Puntos: {cuadrados_rojos_eliminados+cuadrados_azules_eliminados}', True, black)
        pantalla.blit(marcador_rojo, (650, 10))
        
        # Mostrar el contador de cuadrados rojos eliminados
        vida = font.render(f'Salud: {salud}', True, black)
        pantalla.blit(vida, (10, 10))

        # Actualizar la pantalla
        pygame.display.update()
        pygame.time.delay(15)

    # Finalizar Pygame
    pygame.quit()
    sys.exit()

# Ejecutar la función del juego
if __name__ == "__main__":
    juego()