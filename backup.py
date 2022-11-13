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
        

	def update(self,choque):
		if choque==True:
			self.rect.y = 600	  
		self.rect.y +=1        
		if self.rect.y > 600 :
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
VIDA=3


#Coordenadas de la nave al inicio
coord_x = 500
coord_y = 500
#Velocidad teclado
x_speed = 0
y_speed = 0

ListaMeteoritos = pygame.sprite.Group()
TodosSprite = pygame.sprite.Group()

#Creamos todos los meteoritos

def crear_meteoritos(aviso):
    if aviso == True:
        meteorito=Meteorito()
        meteorito.rect.x = random.randrange(1000)
        meteorito.rect.y = random.randrange(100)
        ListaMeteoritos.add(meteorito)
        TodosSprite.add(meteorito)
    else:
        time.sleep(0.5)
        for i in range(5):
            
            meteorito = Meteorito()
            meteorito.rect.x = random.randrange(1000)
            meteorito.rect.y = random.randrange(100)
            ListaMeteoritos.add(meteorito)
            TodosSprite.add(meteorito)
    

nave = Nave()
TodosSprite.add(nave)


#Control de las distinas pantallas
juego_en_pausa = False
estado_menu = "menuInicial"



fuente=pygame.font.SysFont("arialblack",40)

#Pantalla Menu y Fin
def texto_menu(text, font, text_col, x, y ):

    img=fuente.render(text,True, text_col)    
    screen.blit(img,(1000,600))



    if screen == "jugando":
        pass
    elif screen == "pausa":
        pass
    elif screen == "menuInicial":
        pass
    elif screen == "menuFinal":
        pass


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




Choque=False
tiempoSinChoque=0
avisoTiempoSinChoque=False
crear_meteoritos(avisoTiempoSinChoque)

game_mode= "jugando"

while not fin_juego:
    if game_mode == "partida_pausada": 
       # fuente.render(text,True, text_col)  
        reactivar = False
        while reactivar == False:
            screen.blit(fuente.render("JUEGO EN PAUSA", True,WHITE ), (160, 250))
            pygame.display.flip()
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_p:
                        game_mode = "jugando"
                        reactivar=True
                        pygame.display.flip()
                        print("frantxu30")

    elif game_mode == "jugando":
        if tiempoSinChoque == 1000:#subir de dificultad periodicamente
            avisoTiempoSinChoque=True
            crear_meteoritos(avisoTiempoSinChoque)
            tiempoSinChoque=0
            avisoTiempoSinChoque=False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                sys.exit()
            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_p:
                    game_mode = "partida_pausada"
                    #texto_menu("Partida Pausada", fuente, WHITE, 160, 250)

            x_speed=movimiento_teclado(evento,x_speed,y_speed)[0]
            y_speed=movimiento_teclado(evento,x_speed,y_speed)[1]
            
        screen.blit(background, [0, 0])#añadir imagen
        TodosSprite.update(Choque) 
        coord_x += x_speed
        coord_y += y_speed
        nave.rect.x = coord_x
        nave.rect.y = coord_y
        numcolisiones=pygame.sprite.spritecollide(nave, ListaMeteoritos, True)
        for colisiones in numcolisiones:
            Choque =True
            avisoTiempoSinChoque=False
            TodosSprite.update(Choque)
            #time.sleep(0.25)
            coord_x = 500
            coord_y = 500
            time.sleep(0.10)
            #crear_meteoritos(avisoTiempoSinChoque)
            VIDA -=1 
            print("LE QUEDAN " + str(VIDA)+" VIDAS")    
            if VIDA == 0:
                print("GAME OVER")
                fin_juego=True
        Choque=False
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
        tiempoSinChoque+=1
        #print(tiempoSinChoque)
        

        clock.tick(170) #Frames por segundo  