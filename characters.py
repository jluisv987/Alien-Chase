import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ANCHO = 21*32
ALTO = 19*32
game_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '1', '0', '1', '1', '1', '0', '0',
                '1', '0', '0', '1', '1', '1', '1', '1', '1', '0'],
            ['0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0',
                '1', '0', '0', '1', '0', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '0',
                '1', '0', '0', '1', '0', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0',
                '1', '0', '0', '1', '0', '1', '1', '1', '1', '0'],
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1',
                '1', '1', '1', '1', '1', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0',
                '1', '0', '0', '0', '0', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1',
                '1', '1', '0', '1', '1', '1', '0', '0', '1', '0'],
            ['0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1',
                '1', '1', '1', '1', '0', '1', '1', '1', '1', '0'],
            ['0', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1',
                '1', '1', '0', '0', '0', '1', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1',
                '1', '1', '1', '1', '0', '1', '1', '1', '1', '0'],
            ['0', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1',
                '1', '1', '0', '1', '1', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '0', '0', '1', '0', '1', '0', '0', '0',
                '1', '0', '0', '0', '0', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1',
                '1', '1', '1', '1', '1', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '1', '0', '0', '0', '0', '1', '0', '0',
                '1', '0', '0', '1', '0', '1', '1', '1', '1', '0'],
            ['0', '1', '0', '1', '1', '1', '1', '0', '1', '0', '0',
                '1', '0', '0', '1', '0', '1', '0', '0', '1', '0'],
            ['0', '1', '0', '1', '1', '0', '1', '0', '1', '0', '0',
                '1', '0', '0', '1', '0', '1', '0', '0', '1', '0'],
            ['0', '1', '1', '1', '1', '0', '1', '1', '1', '0', '0',
                '1', '0', '0', '1', '1', '1', '1', '1', '1', '0'],
            ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'], ]


class Piso(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Imagenes/Piso.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


class Espacio(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Imagenes/Espacio.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()


class Astronauta(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Astronauta.png").convert()
        self.image.set_colorkey((0, 0, 0))
        # coordenadas de la imagen
        self.rect = self.image.get_rect()

    def moverse(self, x, y):
        if self.rect.x+x < 0:
            self.rect.x = ANCHO-32
        elif self.rect.x+x < ANCHO:
            self.rect.x += x
        else:
            self.rect.x = 0

        if self.rect.y+y < 0:
            self.rect.y = ALTO-32
        elif self.rect.y+y < ALTO:
            self.rect.y += y
        else:
            self.rect.y = 0


class Alien(pygame.sprite.Sprite):
    dir_mov = 0

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Imagenes/Alien rojo.png").convert()
        self.image.set_colorkey((0, 0, 0))
        # coordenadas de la imagen
        self.rect = self.image.get_rect()

    def movimiento(self, x, y):
        if self.rect.x+x < 0:
            self.rect.x = ANCHO-32
        elif self.rect.x+x < ANCHO:
            self.rect.x += x
        else:
            self.rect.x = 0

        if self.rect.y+y < 0:
            self.rect.y = ALTO-32
        elif self.rect.y+y < ALTO:
            self.rect.y += y
        else:
            self.rect.y = 0

    def direccion(self):
        randi = random.randint(1, 4)
        # izquierda
        if randi == 1:
            self.dir_mov = 1
        elif randi == 2:
            self.dir_mov = 2
        elif randi == 3:
            self.dir_mov = 3
        elif randi == 4:
            self.dir_mov = 4
