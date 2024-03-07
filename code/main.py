import pygame , sys, random
import tuberia, background, bird
from config import *

class flapy_bird:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode(PANTALLA)
        pygame.display.set_caption('Flappy Bird')
        self.grupo_tuberias = pygame.sprite.Group()
        self.grupo_conseguir_puntos = []

        self.imagenes_fondo = []
        self.juego_activo = False  

        self.pajaro = bird.bird()

        self.ultima_vez_cayendo = 0
        self.veces_pulsado_espacio = 0

        self.vivo = True
        self.puntos = 0

        
        crear_archivo()

    def colisiones(self):
        for tuberia in self.grupo_tuberias:
            if tuberia.rect.colliderect(self.pajaro.rect):
                self.vivo = False

        if self.vivo:
            for puntos_colision in self.grupo_conseguir_puntos:
                if puntos_colision.rect.colliderect(self.pajaro.rect):
                    self.grupo_conseguir_puntos.remove(puntos_colision)
                    self.puntos += 1

            if self.pajaro.rect.y <= -5 or self.pajaro.rect.y >= PANTALLA[1] - 30:
                self.vivo = False

    def menu_muerte(self):
        
        font = pygame.font.Font(None, 36)
        menu_activo = True
        puntuacion_max = leer_contenido()
        while menu_activo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Si se presiona la tecla Enter, reinicia el juego
                        menu_activo = False
                        self.run()

            # Renderizar texto
            text = font.render("¡Has muerto!", True, WHITE)
            text_gameover = font.render("Presiona ENTER para \n    jugar de nuevo", True, WHITE)
            text_score = font.render(f"Puntuación: {self.puntos}", True, WHITE)
            text_max_score = font.render(f"Puntuación max : {puntuacion_max}", True, WHITE)

            # Centrar textos en pantalla
            text_rect = text.get_rect(center=(PANTALLA[0] // 2, PANTALLA[1] // 2 - 50))
            text_gameover_rect = text_gameover.get_rect(center=(PANTALLA[0] // 2, PANTALLA[1] // 2 + 50))
            text_score_rect = text_score.get_rect(center=(PANTALLA[0] // 2, PANTALLA[1] // 2))
            text_max_score_rect = text_max_score.get_rect(center=(PANTALLA[0] // 2, PANTALLA[1] // 2 - 200))

            # Rellenar la pantalla con color negro
            self.ventana.fill(BLACK)

            # Dibujar textos en pantalla
            self.ventana.blit(text, text_rect)
            self.ventana.blit(text_gameover, text_gameover_rect)
            self.ventana.blit(text_score, text_score_rect)
            self.ventana.blit(text_max_score, text_max_score_rect)

            # Actualizar la pantalla
            pygame.display.flip()

    def run(self):
        font = pygame.font.Font(None, 100)
        font_text = pygame.font.Font(None, 40)
        
        self.grupo_tuberias = pygame.sprite.Group()
        self.grupo_conseguir_puntos = []

        self.imagenes_fondo = []
        self.juego_activo = False  

        self.pajaro = bird.bird()

        self.ultima_vez_cayendo = 0
        self.veces_pulsado_espacio = 0

        self.vivo = True
        self.puntos = 0
        ultima_creacion_tuberias = 0

        self.imagenes_fondo.append(background.background(0,0))

        
        while self.vivo:
            puntuacion = font.render(str(self.puntos), True, (212, 175, 55)) # color dorado
            texto_inicial = font_text.render('pulsa ESPACIO \n para empeza', True, (255, 255, 255)) # color dorado

            tiempo_actual = pygame.time.get_ticks()

            if tiempo_actual - self.ultima_vez_cayendo > 300:
                self.pajaro.estado = 'bajar'

                self.ultima_vez_cayendo = tiempo_actual

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.veces_pulsado_espacio += 1
                        if self.juego_activo == True:
                            self.pajaro.estado = 'subir'
                            self.pajaro.movement()
                        if self.veces_pulsado_espacio == 1:
                            self.juego_activo = True  

            # generar tuberias
            if tiempo_actual - ultima_creacion_tuberias > 2000 and self.juego_activo:
                y_tuberia = random.randint(450,750)
                self.tuberia_arriba = tuberia.tuberia(300,y_tuberia,1)
                self.grupo_tuberias.add(self.tuberia_arriba)

                rectangulo_punto = tuberia.rectangulo_punto(300,y_tuberia - 480)
                self.grupo_conseguir_puntos.append(rectangulo_punto)

                self.tuberia_arriba = tuberia.tuberia(300,y_tuberia - 450,2)
                self.grupo_tuberias.add(self.tuberia_arriba)

                ultima_creacion_tuberias = tiempo_actual

            # generar fondo
            for fondo in self.imagenes_fondo:
                movimiento = fondo.move(self.ventana,tiempo_actual)
                if fondo.rect.x == -600:
                    self.imagenes_fondo.append(background.background(300,0)) 
                elif fondo.rect.x == -900:
                    self.imagenes_fondo.remove(fondo)
            
            # movimiento tuberia
            if self.juego_activo:
                for tub in self.grupo_tuberias:
                    tub.move(tiempo_actual)
                    if tub.rect.x == -100:
                        self.grupo_tuberias.remove(tub)
                self.grupo_tuberias.draw(self.ventana)

            for rectangulo_de_punto in self.grupo_conseguir_puntos:
                rectangulo_de_punto.move(tiempo_actual)
                if rectangulo_de_punto.rect.x == -100:
                    self.grupo_conseguir_puntos.remove(rectangulo_de_punto)


                self.pajaro.update(tiempo_actual)
                ''' Para saver colisiones de puntos
                for puntos_colision in self.grupo_conseguir_puntos:
                    self.ventana.blit(puntos_colision.image,puntos_colision.rect)'''
            self.ventana.blit(self.pajaro.bird,self.pajaro.rect)
            
            self.colisiones()
            if not self.juego_activo:
                self.ventana.blit(texto_inicial, (50,100))
            else:
                self.ventana.blit(puntuacion, (0, 0))

            self.pajaro.animacion(tiempo_actual)
            pygame.display.flip()
        
        # mostrar menu muerte
        puntuacion_anterior = int(leer_contenido())
        if puntuacion_anterior < self.puntos:
            guardar_info(self.puntos)
        self.menu_muerte()

if __name__ == '__main__':
	game = flapy_bird()
	game.run()
