import pygame
from config import *

class background:
    def __init__(self,x,y):
        self.fondo = pygame.image.load("../flappy bird/Imagenes/background.png").convert_alpha()
        self.rect = self.fondo.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.ultimo_movimiento = 0

    def mostrar_en_pantalla(self,ventana):
        ventana.blit(self.fondo,(self.rect.x,self.rect.y))

    def move(self,ventana,tiempo_actual):
        if tiempo_actual - self.ultimo_movimiento > 10:
            self.rect.x -= 1

            self.ultimo_movimiento = tiempo_actual
            self.mostrar_en_pantalla(ventana)


        
