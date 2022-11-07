import pygame, random, sys, time

print("BIENVENIDO, DISPONES DE 3 VIDAS")
BLACK = (0,0,0)
WHITE= (255,255,255)
RED = (255,0,0)
#Creamos las clases necesarias(Meteoritos y Nave)

class Meteorito(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("meteorito.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()#Guardar posición

	def update(self):
		self.rect.y += 1
		if self.rect.y > 600:
			self.rect.y = -5
			self.rect.x = random.randrange(1000)


class Nave(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("nave.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()




pygame.init()
#Aqui puedo poner en una ventana con timesleep el inico o asi
size = (1000, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock() #Tener control de los frames
background = pygame.image.load("backgala.webp").convert()
fin_juego=False
VIDA=3

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
#Coordenadas de la nave al inicio
coord_x = 500
coord_y = 300
#Velocidad teclado
x_speed = 0
y_speed = 0

ListaMeteoritos = pygame.sprite.Group()
TodosSprite = pygame.sprite.Group()

#Creamos todos los meteoritos

##posible
def crearMeteorito():
    for i in range(20):
        
        meteorito = Meteorito()
        meteorito.rect.x = random.randrange(1000)
        meteorito.rect.y = random.randrange(600)

        ListaMeteoritos.add(meteorito)
        TodosSprite.add(meteorito)

def controltime():
    time.sleep(5)

nave = Nave()
TodosSprite.add(nave)



while not fin_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        x_speed=movimiento_teclado(evento,x_speed,y_speed)[0]
        y_speed=movimiento_teclado(evento,x_speed,y_speed)[1]
        
    screen.blit(background, [0, 0])#añadir imagen
    TodosSprite.update()
    coord_x += x_speed
    coord_y += y_speed
    nave.rect.x = coord_x
    nave.rect.y = coord_y
    numcolisiones=pygame.sprite.spritecollide(nave, ListaMeteoritos, True)
    for colisiones in numcolisiones:
        VIDA -=1 
        print("LE QUEDAN " + str(VIDA)+" VIDAS")
        if VIDA == 0:
            print("GAME OVER")
            fin_juego=True
    TodosSprite.draw(screen)

    ###DELIMITAMOS BORDES###
    if coord_x > 904 :#limites del cubo con los bordes laterales
        coord_x=904
    elif coord_x <= 0:
        coord_x=0           
    if coord_y > 526 :#limites del cubo con los bordes laterales
        coord_y=526
    elif coord_y <= 0:
        coord_y=0        
    ###DELIMITAMOS BORDES###   


    pygame.display.flip()
    clock.tick(70) #Frames por segundo  
    ###########

    		self.rect = self.image.get_rect()#Guardar posición
	def update(self):
		self.rect.y += 1
		if self.rect.y > 600:
			self.rect.y = -5
			self.rect.x = random.randrange(1000)


class Nave(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load("nave.png").convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()




pygame.init()

size = (1000, 600)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock() #Tener control de los frames
background = pygame.image.load("backgala.webp").convert()
fin_juego=False

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
#Coordenadas de la nave al inicio
coord_x = 10
coord_y = 10
#Velocidad teclado
x_speed = 0
y_speed = 0

ListaMeteoritos = pygame.sprite.Group()
TodosSprite = pygame.sprite.Group()

#Creamos todos los meteoritos

for i in range(20):

    meteorito = Meteorito()
    meteorito.rect.x = random.randrange(1000)
    meteorito.rect.y = random.randrange(600)

    ListaMeteoritos.add(meteorito)
    TodosSprite.add(meteorito)

nave = Nave()
TodosSprite.add(nave)



while not fin_juego:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        x_speed=movimiento_teclado(evento,x_speed,y_speed)[0]
        y_speed=movimiento_teclado(evento,x_speed,y_speed)[1]
        
    screen.blit(background, [0, 0])#añadir imagen
    TodosSprite.update()
    coord_x += x_speed
    coord_y += y_speed
    nave.rect.x = coord_x
    nave.rect.y = coord_y
    pygame.sprite.spritecollide(nave, ListaMeteoritos, True)
    TodosSprite.draw(screen)
    print(coord_y)

    ###DELIMITAMOS BORDES###
    if coord_x > 904 :#limites del cubo con los bordes laterales
        coord_x=904
    elif coord_x <= 0:
        coord_x=0           
    if coord_y > 526 :#limites del cubo con los bordes laterales
        coord_y=526
    elif coord_y <= 0:
        coord_y=0        
    ###DELIMITAMOS BORDES###   


    pygame.display.flip()
    clock.tick(70) #Frames por segundo 