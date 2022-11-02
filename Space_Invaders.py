import pygame, sys
pygame.init()
BLACK = (0,0,0)
WHITE= (255,255,255)
RED = (255,0,0)
size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock() #Tener control de los frames

#Coordenadas del cuadrado
coord_x = 10
coord_y = 10
#Velocidad
x_speed = 0
y_speed = 0

def izq_der_teclado(event,x_speed,y_speed):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_speed = -3
        if event.key == pygame.K_RIGHT:
            x_speed = 3
        if event.key == pygame.K_UP:
            y_speed = -3
        if event.key == pygame.K_DOWN:
            y_speed = 3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            x_speed = 0
        if event.key == pygame.K_RIGHT:
            x_speed = 0
        if event.key == pygame.K_UP:
            y_speed = 0
        if event.key == pygame.K_DOWN:
            y_speed = 0
    

    return [x_speed,y_speed]




while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        x_speed=izq_der_teclado(evento,x_speed,y_speed)[0]
        y_speed=izq_der_teclado(evento,x_speed,y_speed)[1]
    screen.fill(WHITE)
    coord_x += x_speed
    coord_y += y_speed                
    pygame.draw.rect(screen, RED, (coord_x, coord_y, 100, 100))
    pygame.display.flip()
    clock.tick(60) #Frames por segundo
    
