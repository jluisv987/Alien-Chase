import pygame
from characters import *
import random
segment_width = 32
segment_height = 32
# reloj
clock = pygame.time.Clock()
done = False
# Iniciamos pygame
pygame.init()
# Creamos una ventana
screen = pygame.display.set_mode([ANCHO, ALTO])
# titulo del juego
pygame.display.set_caption('Alien Chase')
# Creamos el astronauta y los aliens
astronauta = Astronauta()
alien_verde = Alien()
alien_rojo = Alien()
alien_azul = Alien()
alien_rosa = Alien()
# posiciones iniciales
astronauta.rect.x = 32
astronauta.rect.y = 32

alien_verde.rect.x = 288
alien_verde.rect.y = 224

alien_rojo.rect.x = 288
alien_rojo.rect.y = 352

alien_azul.rect.x = 384
alien_azul.rect.y = 224

alien_rosa.rect.x = 384
alien_rosa.rect.y = 352

# lista de los bloques y sprites para la funcion dibujar
block_list = pygame.sprite.Group()
movingsprites = pygame.sprite.Group()
# cargamos astronauta y aliens
movingsprites.add(astronauta)
movingsprites.add(alien_verde)
movingsprites.add(alien_rojo)
movingsprites.add(alien_azul)
movingsprites.add(alien_rosa)

# cargamos mapa
y = 0
# recorremos la matriz del mapa y creamos los objetos de los bloques para dibujarlos despues
for row in game_map:
    x = 0
    for tile in row:
        if tile == '0':
            espacio = Espacio()
            espacio.rect.x = x*32
            espacio.rect.y = y*32
            block_list.add(espacio)
        if tile == '1':
            piso = Piso()
            piso.rect.x = x*32
            piso.rect.y = y*32
            block_list.add(piso)
        x += 1
    y += 1

# se le pasa una coordenada (x,y) y te dice si esta es una coordenada de pared


def colision_pared(x, y):
    if game_map[int((y)/32)][int((x)/32)] == '0':
        return True
    else:
        return False

# Si un alien esta en una intersseción %50 de probabilidades de cambiar de dirección


def cambio_intersección(x, y):
    caminos = 0
    randi = random.randint(1, 4)
    if randi == 1 or randi == 2:
        if x >= 10 and x <= 13 and y >= 8 and y <= 12:
            return False
        if game_map[y-1][x] == '1':
            caminos += 1
        if game_map[y+1][x] == '1':
            caminos += 1
        if game_map[y][x-1] == '1':
            caminos += 1
        if game_map[y][x+1] == '1':
            caminos += 1
        if caminos >= 3:
            return True
    return False


def mover_alien(alien):
    # variables para regresar a la posición anterior si el movimiento causo una colision con la pared
    posx = alien.rect.x
    posy = alien.rect.y
    # Si el alien no tiene una direccion se le da una y seguira con esta hasta topar con pared

    if cambio_intersección(int(posx/32), int(posy/32)) == True or alien.dir_mov == 0:
        alien.direccion()
    if alien.dir_mov == 1:
        alien.movimiento(-32, 0)  # izquierda
    if alien.dir_mov == 2:
        alien.movimiento(0, -32)  # arriba
    if alien.dir_mov == 3:
        alien.movimiento(32, 0)  # derecha
    if alien.dir_mov == 4:
        alien.movimiento(0, 32)  # abajo
    # Si el alien llega a una pared se regresa a las coordenadas anteriores y reinicia movimiento
    if colision_pared(alien.rect.x, alien.rect.y):
        alien.rect.x = posx
        alien.rect.y = posy
        alien.dir_mov = 0


while not done:
    # Quitamos el juego al presiona x en la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # movimiento del astronauta por teclado
        posx = astronauta.rect.x
        posy = astronauta.rect.y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                astronauta.moverse(-32, 0)
            if event.key == pygame.K_UP:
                astronauta.moverse(0, -32)
            if event.key == pygame.K_RIGHT:
                astronauta.moverse(32, 0)
            if event.key == pygame.K_DOWN:
                astronauta.moverse(0, 32)
            # si se colisiona con una pared se regresa a la posición anterior
            if colision_pared(astronauta.rect.x, astronauta.rect.y):
                astronauta.rect.x = posx
                astronauta.rect.y = posy
    screen.fill(WHITE)
    # dibujamos mapa
    block_list.draw(screen)
    # movimiento alien
    mover_alien(alien_verde)
    mover_alien(alien_rojo)
    mover_alien(alien_azul)
    mover_alien(alien_rosa)
    # dibujamos sprites
    movingsprites.draw(screen)
    pygame.display.flip()
    clock.tick(5)
