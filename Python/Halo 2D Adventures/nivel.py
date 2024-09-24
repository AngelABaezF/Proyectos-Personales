import pygame
import sys
import math
import random
import time

#Definimos todo el nivel como funcion para poder ejecutarlo desde el menu
def juego():
    global x, y, disparos_g
    # Inicialización de Pygame
    pygame.init()
    musica_nivel = pygame.mixer.Sound("sonidos/nivel.mp3")
    musica_nivel.play()
    
    # Bucle principal del juego
    running = True
    automatico = False

    #Cargamos el background y definimos las posiciones del background
    background = pygame.image.load("imagenes/nivel1.png")
    background = pygame.transform.scale(background, (800,600))
    xbackground1 = 0
    xbackground2 = 800
    
    musica = pygame
    
    # Dimensiones de la pantalla
    pantalla_ancho = 800
    pantalla_alto = 600
    pantalla = pygame.display.set_mode((pantalla_ancho, pantalla_alto))
    
    salud = 100
    
    #Funcion para cargar una lista de imagenes para animaciones.
    def cargar_imagenes(prefijo, sufijo, n, escala):
        images = []
        for i in range (1,n+1):
            image = pygame.image.load(prefijo + str(i) + sufijo)
            image = pygame.transform.scale(image, escala)
            images.append(image)
        return images

    #Funsiones para cargar las animaciones con con
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
    def mostrar_animacion_agachado_b(n, images, x, y):
        if moverse_izquierda == True and actualizar_agachado == True and moverse_derecha == False:
            frame = int(time.time()*(n-1))%len(images)
            pantalla.blit(images[frame], (x, y))
    def mostrar_animacion(n, images, x, y):
        frame = int(time.time()*(n-1))%len(images)
        pantalla.blit(images[frame], (x, y))

    #Cargamos listas con nuestros sprites        
    jefe_correr_f = cargar_imagenes("imagenes/jefe_correr_f/jefe_correr_f_", ".png", 10, (50,100))
    jefe_correr_b = cargar_imagenes("imagenes/jefe_correr_b/jefe_correr_b_", ".png", 10, (50,100))
    jefe_agachado_f = cargar_imagenes("imagenes/jefe_agachado_f/jefe_agachado_f_", ".png", 4, (50,50))
    jefe_agachado_b = cargar_imagenes("imagenes/jefe_agachado_b/jefe_agachado_b_", ".png", 4, (50,50))
    grunt_corriendo_b = cargar_imagenes("imagenes/grunt_corriendo_b/grunt_corriendo_", ".png", 8, (35,70))
    elite_corriendo_b = cargar_imagenes("imagenes/elite_corriendo_b/elite_corriendo_b_", ".png", 6, (50,100))
    yakal_corriendo_b = cargar_imagenes("imagenes/yakal_corriendo_b/yakal_corriendo_b_", ".png", 7, (40,80))
    jakal_normal = pygame.image.load("imagenes/enemigos_normales/jakal.png")
    jakal_normal = pygame.transform.scale(jakal_normal, (40,80))
    grunt_normal = pygame.image.load("imagenes/enemigos_normales/grunt.png")
    grunt_normal = pygame.transform.scale(grunt_normal, (40,80))
    jefe_normal = pygame.image.load("imagenes/jefe_maestro/jefe_maestro_1.png")
    jefe_normal = pygame.transform.scale(jefe_normal,(50,100))
    jefe_normal_agachado = pygame.image.load("imagenes/jefe_maestro/jefe_agachado_f.png")
    jefe_normal_agachado = pygame.transform.scale(jefe_normal_agachado,(50,50))

    # Colores
    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (150, 150, 150)

    #====Datos del personaje====#
    # cuadrado
    cuadrado_tamaño = 50
    cuadrado_x = 0
    cuadrado_y = 299
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

    #====Datos para los disparos====#
    # Disparo
    velocidad_disparo = 5
    projectiles = []
    
    # Lista para almacenar los disparos_g
    disparos_g = []

    # Variable para rastrear si el botón derecho del ratón está presionado
    boton_derecho_presionado = False
    
    # Reloj para controlar la velocidad del juego
    clock = pygame.time.Clock()

    # Temporizador para controlar la frecuencia de los disparos
    temporizador_disparo = 0
    frecuencia_disparo = 10  # Puedes ajustar esta frecuencia según tus preferencias

    #====Datos de los enemigos====#
    # Velocidad del cuadrado rojo
    elite_amarillo_velocidad = 1  # Ajusta esta velocidad según lo que desees
    grunt_velocidad = 1
    jakal_velocidad = 1

    #====Funciones del personaje====#
    # Función para actualizar la posición del personaje si está saltando
    def actualizar_cuadrado_salto():
        nonlocal cuadrado_y, saltando, salto_contador, actualizar_agachado
        if saltando:
            if salto_contador < salto_duracion:
                cuadrado_y -= salto_distancia
                salto_contador += 1
            else:
                if cuadrado_y < 299:
                    cuadrado_y += salto_distancia
                    if cuadrado_y >= 299:
                        saltando = False
                        salto_contador = 0

    # Función para cambiar la altura del personaje cuando se presiona/despresiona la tecla S
    def actualizar_altura_cuadrado(agachado):
        nonlocal cuadrado_altura, cuadrado_y
        if agachado:
            cuadrado_altura = cuadrado_altura_agachado
            cuadrado_y = cuadrado_y + 50
        elif cuadrado_y == 349:
            cuadrado_altura = cuadrado_altura_normal
            cuadrado_y = 299

    # Función para actualizar la posición horizontal del personaje
    def actualizar_cuadrado_horizontal():
        nonlocal cuadrado_x
        if moverse_derecha and cuadrado_x <= 450:
            cuadrado_x += cuadrado_velocidad

        if moverse_izquierda and cuadrado_x > 0:
            cuadrado_x -= cuadrado_velocidad

    #====Funciones de disparo del personaje====#
    # Función para disparar automáticamente hacia el cursor
    def disparo_automatico():
        nonlocal temporizador_disparo
        if temporizador_disparo >= frecuencia_disparo:
            disparar_hacia_cursor()
            temporizador_disparo = 0  # Reiniciar el temporizador

    # Función para disparar hacia el cursor
    def disparar_hacia_cursor():
        cursor_x, cursor_y = pygame.mouse.get_pos()
        delta_x = cursor_x - cuadrado_x
        delta_y = cursor_y - cuadrado_y
        distancia = math.sqrt(delta_x ** 2 + delta_y ** 2)
        if distancia == 0:
            return

        velocidad_x = (delta_x / distancia) * velocidad_disparo
        velocidad_y = (delta_y / distancia) * velocidad_disparo

        # Condicional para el origen del disparo (si esta agachado)
        if not actualizar_agachado:
            nuevo_disparo = {'x': cuadrado_x + cuadrado_tamaño, 'y': cuadrado_y + cuadrado_tamaño / 4,
                              'velocidad_x': velocidad_x, 'velocidad_y': velocidad_y}
        elif actualizar_agachado:
            nuevo_disparo = {'x': cuadrado_x + cuadrado_tamaño, 'y': cuadrado_y + cuadrado_tamaño / 8,
                              'velocidad_x': velocidad_x, 'velocidad_y': velocidad_y}
        projectiles.append(nuevo_disparo)

    # Función para dibujar los disparos_g
    def grunt_disparo(disparos_g):
        for disparo_g in disparos_g:
            pygame.draw.rect(pantalla, grey, disparo)
            
    #====Clases de los enemigos y sus funciones====#
    #==Clase del elite amarillo==#
    class Elite_amarillo:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.size = 100
            self.color = (255, 0, 0)
            self.colisiones = 0

        def draw(self, pantalla):
            mostrar_animacion(10,elite_corriendo_b,self.x,self.y)

        def colisionar(self):
            self.colisiones += 1

        def eliminar(self):
            return self.colisiones >= 6

    # Lista para almacenar los elites amarillos
    elites_amarillos = []

    # Crear un objeto elite amarillo inicial
    elites_amarillos.append(Elite_amarillo(700, 299))

    # Contador de elites amarillos eliminados
    elites_amarillos_eliminados = 0

    # Función para generar un nuevo elite amarillo
    def generar_elite_amarillo():
        x = pantalla_ancho
        y = 299  # Altura fija
        nuevo_elite_amarillo = Elite_amarillo(x, y)
        elites_amarillos.append(nuevo_elite_amarillo)

    generar_elite_amarillo()  # Generar el primer elite amarillo

    # Fuente para el marcador de elites amarillos eliminados
    font = pygame.font.Font(None, 36)
    
    #==Clase del grunt==#
    class Grunt:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.color = (255, 0, 0)
            self.colisiones = 0
            self.size = 70
            self.moverse = 0
            
        def draw(self, pantalla):
            mostrar_animacion(8,grunt_corriendo_b,self.x,self.y)

        def colisionar(self):
            self.colisiones += 1

        def eliminar(self):
            return self.colisiones >= 3

    # Lista para almacenar los grunts
    grunts = []

    # Crear un objeto Grunt inicial
    grunts.append(Grunt(700, 329))

    # Contador de grunts eliminados
    grunts_eliminados = 0

    # Función para generar un nuevo grunt
    def generar_grunt():
        x = pantalla_ancho
        y = 329  # Altura fija
        nuevo_grunt = Grunt(x, y)
        grunts.append(nuevo_grunt)

    generar_grunt()  # Generar el primer grunt
    
    #==Clase del jakal==#
    class Jakal:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.color = (255, 0, 0)
            self.colisiones = 0
            self.size = 80
            self.moverse = 0

        def draw(self, pantalla):
            mostrar_animacion(7,yakal_corriendo_b,self.x,self.y)
            
        def colisionar(self):
            self.colisiones += 1

        def eliminar(self):
            return self.colisiones >= 4

    # Lista para almacenar los jakals
    jakals = []

    # Crear un objeto Jakal inicial
    jakals.append(Jakal(700, 319))

    # Contador de jakals eliminados
    jakals_eliminados = 0

    # Función para generar un nuevo jakal
    def generar_jakal():
        x = pantalla_ancho
        y = 319  # Altura fija
        nuevo_jakal = Jakal(x, y)
        jakals.append(nuevo_jakal)

    generar_jakal()  # Generar el primer cuadrado rojo

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
                disparar_hacia_cursor()
                if 360 <= event.pos[0] <= 410 and 10 <= event.pos[1] <= 50:
                    # Hacer clic en el botón de salida
                    musica_nivel.stop()
                    import menu
                    menu.menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and automatico:
                # Botón derecho del ratón presionado
                boton_derecho_presionado = True
                if 360 <= event.pos[0] <= 410 and 10 <= event.pos[1] <= 50:
                    # Hacer clic en el botón de salida
                    musica_nivel.stop()
                    running = False
                    import menu
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and automatico:
                # Botón derecho del ratón liberado
                boton_derecho_presionado = False
                
        # Actualizar la posición de los cuadrados rojos
        for elite_amarillo in elites_amarillos:
            elite_amarillo.x -= elite_amarillo_velocidad
    
            #Daño
            if elite_amarillo.x == cuadrado_x:
                salud -= 49
            
        # Eliminar elites amarillos si han sido alcanzados por 5 balas
        for i, elite_amarillo in enumerate(elites_amarillos):
            for j, projectil in enumerate(projectiles):
                if elite_amarillo and elite_amarillo.x < projectil['x'] < elite_amarillo.x + elite_amarillo.size and elite_amarillo.y < projectil['y'] < elite_amarillo.y + elite_amarillo.size:
                    elite_amarillo.colisionar()
                    del projectiles[j]
                    
        # Incrementar el contador de cuadrados rojos eliminados
        for elite_amarillo in elites_amarillos:
            if elite_amarillo.eliminar():
                elites_amarillos_eliminados += 4
                
        # Eliminar los cuadrados rojos que han sido alcanzados por 5 balas
        elites_amarillos = [elite_amarillo for elite_amarillo in elites_amarillos if not elite_amarillo.eliminar()]
        
        # Generar nuevos cuadrados rojos de forma aleatoria
        if random.randint(1, 600) == 1:
            generar_elite_amarillo()
        
        for grunt in grunts:
            if grunt.x > 499:
                grunt.moverse = 1
                grunt.x -= grunt_velocidad
            if moverse_derecha == True and cuadrado_x > 449 and grunt.moverse == 0:
                grunt.x -= 1
            if grunt.x <= 499:
                # Crear un nuevo disparo cada 5 frames
                if pygame.time.get_ticks() % 15 == 1:
                    disparo_g = pygame.Rect(x,y + 25, 10, 5)
                    disparos_g.append(disparo_g)

        # Mover los disparos_g
        for disparo_g in disparos_g:
            grunt_disparo.x -= 5  # Velocidad del disparo

        # Eliminar disparos_g que salieron de la pantalla
        disparos_g = [disparo_g for disparo_g in disparos_g if grunt_disparo.x < pantalla_ancho]
        
        # Eliminar grunts si han sido alcanzados por 5 balas
        for i, grunt in enumerate(grunts):
            for j, projectil in enumerate(projectiles):
                if grunt and grunt.x < projectil['x'] < grunt.x + grunt.size and grunt.y < projectil['y'] < grunt.y + grunt.size:
                    grunt.colisionar()
                    del projectiles[j]
                    
        # Incrementar el contador de grunts  eliminados
        for grunt in grunts:
            if grunt.eliminar():
                grunts_eliminados += 1
        
        # Eliminar los grunts que han sido alcanzados por los proyectiles
        grunts = [grunt for grunt in grunts if not grunt.eliminar()]
        
        # Generar nuevos grunt de forma aleatoria
        if random.randint(1, 100) == 1:
            generar_grunt()
        
        for jakal in jakals:
            if jakal.x > 449:
                jakal.moverse = 1
                jakal.x -= jakal_velocidad
            else: jakal.moverse = 0
            if moverse_derecha == True and cuadrado_x > 449 and jakal.moverse == 0:
                jakal.x -= 1
            
        # Eliminar grunts si han sido alcanzados por 5 balas
        for i, jakal in enumerate(jakals):
            for j, projectil in enumerate(projectiles):
                if jakal and jakal.x < projectil['x'] < jakal.x + jakal.size and jakal.y < projectil['y'] < jakal.y + jakal.size:
                    jakal.colisionar()
                    del projectiles[j]

        # Incrementar el contador de cuadrados rojos eliminados
        for jakal in jakals:
            if jakal.eliminar():
                jakals_eliminados += 2

        # Eliminar los cuadrados rojos que han sido alcanzados por 5 balas
        jakals = [jakal for jakal in jakals if not jakal.eliminar()]

        # Generar nuevos cuadrados rojos de forma aleatoria
        if random.randint(1, 200) == 1:
            generar_jakal()

        # Incrementar el temporizador de disparo
        if temporizador_disparo < frecuencia_disparo:
            temporizador_disparo += 1
            
        # Actualizar la posición de los proyectiles
        for projectil in projectiles:
            projectil['x'] += projectil['velocidad_x']
            projectil['y'] += projectil['velocidad_y']

        # Actualizar posición del cuadrado si está saltando
        actualizar_cuadrado_salto()

        # Actualizar posición horizontal
        actualizar_cuadrado_horizontal()
        
        # Llamar a la función de disparo automático mientras el botón derecho del ratón está presionado
        if boton_derecho_presionado:
            disparo_automatico()

        # Limpiar la pantalla
        if moverse_derecha == True and cuadrado_x > 400:
            xbackground1 -= 1
            xbackground2 -=1
            elite_amarillo_velocidad = 3.6
            grunt_velocidad = 2
            jakal_velocidad = 2
        else:
            elite_amarillo_velocidad = 3
            grunt_velocidad = 1
            jakal_velocidad = 1
            
        if xbackground1 == -800:
            xbackground1 = 0
        if xbackground2 == 0:
            xbackground2 = 800
            
        pantalla.blit(background,(xbackground1,0))
        pantalla.blit(background,(xbackground2,0))

        # Dibujar la línea horizontal
        pygame.draw.line(pantalla, black, (0, 400), (pantalla_ancho, 400), 5)

        # Dibujar el cuadrado
        mostrar_animacion_correr_f(10,jefe_correr_f,cuadrado_x,cuadrado_y)
        mostrar_animacion_correr_b(10,jefe_correr_b,cuadrado_x,cuadrado_y)
        mostrar_animacion_agachado_f(4,jefe_agachado_f,cuadrado_x,cuadrado_y)
        mostrar_animacion_agachado_b(4,jefe_agachado_b,cuadrado_x,cuadrado_y)
        if ((moverse_derecha == False and moverse_izquierda == False) or (moverse_derecha == True and moverse_izquierda == True)) and actualizar_agachado == False:
            pantalla.blit(jefe_normal, (cuadrado_x, cuadrado_y))
        if ((moverse_derecha == False and moverse_izquierda == False) or (moverse_derecha == True and moverse_izquierda == True)) and actualizar_agachado == True:
            pantalla.blit(jefe_normal_agachado, (cuadrado_x, cuadrado_y))
        
        # Boton de salida
        pygame.draw.rect(pantalla, white, (360, 10, 50, 40))

        # Dibujar los proyectiles
        for projectil in projectiles:
            pygame.draw.rect(pantalla, white, (projectil['x'], projectil['y'], 5, 5))

        # Dibujar los cuadrados rojos
        for elite_amarillo in elites_amarillos:
            elite_amarillo.draw(pantalla)

        for grunt in grunts:
            if grunt.moverse == 1:
                grunt.draw(pantalla)
            else: pantalla.blit(grunt_normal, (grunt.x, grunt.y))
            
        grunt_disparo(disparos_g)
            
        for jakal in jakals:
            if jakal.moverse == 1:
                jakal.draw(pantalla)
            else: pantalla.blit(jakal_normal, (jakal.x, jakal.y))

        # Mostrar el contador de cuadrados rojos eliminados
        marcador = font.render(f'Puntos: {elites_amarillos_eliminados+jakals_eliminados+grunts_eliminados}', True, white)
        pantalla.blit(marcador, (650, 10))
        
        vida = font.render(f'Salud: {salud}', True, white)
        pantalla.blit(vida, (10, 10))
        

        # Actualizar la pantalla
        pygame.display.update()
        pygame.time.delay(15)

    # Contador de eliminados
    jakals_eliminados = 0
    grunts_eliminados = 0
    elites_amarillos_eliminados = 0
    salud = 100
    
    # Finalizar Pygame
    pygame.quit()
    sys.exit()

# Ejecutar la función del juego
if __name__ == "__main__":
    juego()