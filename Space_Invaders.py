import pygame, sys, random
pygame.init()
BLACK = (0,0,0)
WHITE= (255,255,255)
RED = (255,0,0)
size = (1000, 600)#800 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock() #Tener control de los frames

#Coordenadas del cuadrado
coord_x = 10
coord_y = 10
#Velocidad
x_speed = 0
y_speed = 0

background = pygame.image.load("backgala.webp").convert()
nave = pygame.image.load("nave.png").convert()
nave.set_colorkey([0,0,0])#Quitar fondo negro de la imagen
meteorito = pygame.image.load("meteorito.png").convert()
meteorito.set_colorkey([0,0,0])#Quitar fondo negro de la imagen

def movimiento_teclado(event,x_speed,y_speed):

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

listacord = [] #para guardar unas coordenadas fijas y no nos salgan constantemente
i=0

while i<= 15:
    #Tenemos que incluir x e y porque sino solo nos salen los puntos en una recta
    obj_x = random.randint(0,800)
    obj_y = random.randint(0,500)
    pygame.draw.circle(screen,RED, (obj_x,obj_y), 5)
    listacord.append([obj_x,obj_y])
    i=i+1


        
def caida_objetos():
    for coordenada in listacord:
        screen.blit(meteorito,coordenada)
        coordenada[1] += 1 #Aumentamos la Y para que parezca que baja
        if coordenada[1]>500:
            coordenada[1]=0



        
#Bucle principal


fin_juego=False
while not fin_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        x_speed=movimiento_teclado(evento,x_speed,y_speed)[0]
        y_speed=movimiento_teclado(evento,x_speed,y_speed)[1]
        #print(coord_x)
        print(coord_y)
    #screen.fill(WHITE)
    screen.blit(background, [0, 0])#añadir imagen
    caida_objetos()
    coord_x += x_speed
    coord_y += y_speed
    screen.blit(nave, [coord_x,coord_y])

    if coord_x > 702 :#limites del cubo con los bordes laterales
        coord_x=702
    elif coord_x <= 0:
        coord_x=0           
    if coord_y > 400 :#limites del cubo con los bordes laterales
        coord_y=400
    elif coord_y <= 0:
        coord_y=0           
    
    #pygame.draw.rect(screen, RED, (coord_x, coord_y, 50, 50))

    
    pygame.display.flip()
    clock.tick(70) #Frames por segundo
    
