from typing import Any
import pygame
from config import *

class bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        pygame.init()

        self.animacion_num = 0

        self.bird = pygame.transform.scale(pygame.image.load(f"flappy bird/Imagenes/bird/{self.animacion_num}.png"),(50,50))
        self.image = self.bird
        self.rect = self.image.get_rect()

        self.rect.y = 170
        self.rect.x = 20

        self.estado = 'bajar'

        self.ultima_vez_animado = 0
        self.ultima_vez_gravedad = 0

    def animacion(self,tiempo_actual):
        if tiempo_actual - self.ultima_vez_animado > 100:
            self.animacion_num += 1
            if self.animacion_num == 3:
                self.animacion_num = 0
            self.bird = pygame.transform.scale(pygame.image.load(f"flappy bird/Imagenes/bird/{self.animacion_num}.png"),(50,50))

            self.ultima_vez_animado = tiempo_actual

    def movement(self):
        self.rect.y -= 20

    def gravedad(self,tiempo_actual):
        if tiempo_actual - self.ultima_vez_gravedad > 6:
            self.rect.y += 1

            self.ultima_vez_gravedad = tiempo_actual

    def update(self,tiempo_actual):

        if self.estado == 'bajar':
            self.gravedad(tiempo_actual)