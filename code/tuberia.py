import pygame

class tuberia(pygame.sprite.Sprite):
    def __init__(self,x,y,num_tuberia):
        super().__init__()
        pygame.init()

        self.columna_1 = pygame.image.load(f"../flappy bird/Imagenes/tuberia_{str(num_tuberia)}.png").convert_alpha()
        self.image = self.columna_1
        self.rect = self.image.get_rect()

        self.image = pygame.transform.scale(self.columna_1,((self.rect.width)/1.5, (self.rect.height)/1.5))
        self.rect = self.image.get_rect()

        self.rect.bottomleft = (x,y)
        self.tiempo_ulti_move = 0
    
    def move(self,tiempo_actual):
        if tiempo_actual - self.tiempo_ulti_move > 8:
            self.rect.x -= 1

            self.tiempo_ulti_move = tiempo_actual

class rectangulo_punto(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        pygame.init()

        self.rect = pygame.rect.Rect(x,y,50,200)
        self.image = pygame.Surface([50, 200])
        self.image.fill((255,255,255))

        self.tiempo_ulti_move = 0
    
    def move(self,tiempo_actual):
        if tiempo_actual - self.tiempo_ulti_move > 8:
            self.rect.x -= 1

            self.tiempo_ulti_move = tiempo_actual
