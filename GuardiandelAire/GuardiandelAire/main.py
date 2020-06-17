import pygame, os, player, time, enemigo
from pygame.locals import *

currentPath = os.path.dirname(__file__) #path where is main.py
imagePath = os.path.join(currentPath, 'assets') #path where the images are
musicPath = os.path.join(imagePath, 'musica') #path where misuc are
pausaPath = os.path.join(imagePath, 'pausa') #path wgere is pausa
menuPath = os.path.join(imagePath, 'menu') #path where is menu
#Inicizalizar
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
# Path
current_path = os.path.dirname(__file__)  # Where your .py file is located
resource_path = os.path.join(current_path, 'assets')  # The resource folder path
image_path = os.path.join(resource_path, 'menu')  # The image folder path
#Pantalla
pygame.display.set_caption("El guardian del aire")
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 20)

#pause
Nivel1Restart = True
Nivel2Restart = True
Nivel3Restart = True
ppause = False
def complet(estado, n):
    global Nivel1Restart, Nivel2Restart, Nivel3Restart
    boton1=Boton(play1,play2,411,239)
    boton2=Boton(regres,regres1,408,254)
    boton3=Boton(exitt,exitt1,750,69)
    cursor1=Cursor()
    salir=False
    while salir!=True:
        if estado:
            screen.blit(completado, (0,0))
            boton1.update(screen,cursor1)
            boton3.update(screen,cursor1)
        else:
            screen.blit(incompleto, (0,0))
            boton2.update(screen,cursor1)
            boton3.update(screen,cursor1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    if n < 1 and n > 3:
                        return False
                if cursor1.colliderect(boton2.rect):
                    if n == 1:
                        Nivel1Restart = True
                    if n == 2:
                        Nivel2Restart = True
                    if n == 3:
                        Nivel3Restart = True
                    return True
                if cursor1.colliderect(boton3.rect):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join(musicPath,"menumusic.mp3"))
                    pygame.mixer.music.play()
                    ppause = True
                    return False
            if event.type == pygame.QUIT:
                salir=True
            reloj1.tick(100)
            cursor1.update()
def Pause(n):
    global Nivel1Restart, Nivel2Restart, Nivel3Restart, ppause
    boton1=Boton(play1,play2,427,268)
    boton2=Boton(regres,regres1,295,231)
    boton3=Boton(exitt,exitt1,550,231)
    cursor1=Cursor()
    salir=False
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    salir = True
                if cursor1.colliderect(boton2.rect):
                    if n == 1:
                        Nivel1Restart = True
                    if n == 2:
                        Nivel2Restart = True
                    if n == 3:
                        Nivel3Restart = True
                    return True
                if cursor1.colliderect(boton3.rect):
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(os.path.join(musicPath,"menumusic.mp3"))
                    pygame.mixer.music.play()
                    ppause = True
                    return False
            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        screen.blit(menpause, (0,0))
        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
    return True
#Juego
bg_image = pygame.image.load(os.path.join(imagePath,"fondolevel1.png"))
bg_image2 = pygame.image.load(os.path.join(imagePath,"fondolevel2.png"))
bg_image3 = pygame.image.load(os.path.join(imagePath,"fondolevel3.png"))
arbol1 = pygame.image.load(os.path.join(imagePath,"arbol1.png"))
arbol2 = pygame.image.load(os.path.join(imagePath,"arbol2.png"))
arbol3 = pygame.image.load(os.path.join(imagePath,"arbol3.png"))
Player = player.Mono((900/2, 450))
Playar = player.Mona((900/2, 450))
#Fondos
running = True
#Clases
class Arboles(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        self.normal = pygame.image.load(os.path.join(imagePath,"arbol3.png"))
        self.image = self.normal
        self.quemado1 = pygame.image.load(os.path.join(imagePath,"arbol4.png"))
        self.quemado2 = pygame.image.load(os.path.join(imagePath,"arbol5.png"))
        self.rect = self.image.get_rect()
        self.rect.x = posX
        self.rect.y = posY
        self.n = 100
        self.estado = True
        self.colision = False
        self.fuego = False
        self.ny = posY
        self.tiempoEncendido = 0
    def encendido(self):
        if self.n % 100 == 0:
            if self.estado:
                self.image = self.quemado1
                self.rect.y = self.ny - 4
                self.estado = False
            else:
                self.image = self.quemado2
                self.rect.y = self.ny - 12
                self.estado = True
        if self.n > 10000:
            self.n = 100
        self.n += 1

class Ranura(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(os.path.join(imagePath,"ranura.png"))
        self.ran1 = self.image.get_rect()
        self.ran1.x = 61
        self.ran1.y = 524
        self.ran2 = self.image.get_rect()
        self.ran2.x = 299
        self.ran2.y = 524
        self.ran3 = self.image.get_rect()
        self.ran3.x = 539
        self.ran3.y = 524
        self.ran4 = self.image.get_rect()
        self.ran4.x = 772
        self.ran4.y = 524
class Pasto(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(os.path.join(imagePath,"pasto.png"))
pasto = Pasto()

class Barra(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(os.path.join(imagePath,"barra.png"))
barra = Barra()

class Vida(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(os.path.join(imagePath,"vida.png"))
vida = Vida()

class Reloj(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(os.path.join(imagePath,"reloj.png"))
reloj = Reloj()

class Jarron(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(os.path.join(imagePath,"jarron.png"))
jarron = Jarron()
nube = enemigo.Enemigo(0, 55)

def Nivel1(sexo):
    nube.rangoDisparo = 5
    nube.velocidad = 1
    global running, Nivel1Restart, ppause
    cursor1=Cursor()
    boton1=Boton(pause,pause,845,77)
    ranura = Ranura()
    completo = False
    avance = True
    running = True
    jugador = False
    nArboles = 0
    nArboles2 = [False, False, False, False]
    a1= False
    a2= False
    a3= False
    a4= False
    a5= False
    a = False
    b = False
    c = False
    d = False
    f = False
    score = 0
    segundos = 300
    tiempo = 0
    tiempo2 = 2
    vidas = 3
    arbol01 = Arboles(57, 409)
    arbol02 = Arboles(294, 409)
    arbol03 = Arboles(534, 409)
    arbol04 = Arboles(768, 409)
    arbol01.colision = False
    arbol02.colision = False
    arbol03.colision = False
    arbol04.colision = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(musicPath,"levelsmusic.mp3"))
    pygame.mixer.music.play()
    Intro(screen, 1)
    while running:
        if arbol01.tiempoEncendido > 5:
            vidas -= 1
            arbol01.tiempoEncendido = 0
            arbol01.fuego = False
            arbol01.colision = False
            a1 = False
            a = False
            nArboles2[0] = False
            nArboles -= 1
        if arbol02.tiempoEncendido > 5:
            vidas -= 1
            arbol02.tiempoEncendido = 0
            arbol02.fuego = False
            arbol02.colision = False
            a2 = False
            b = False
            nArboles2[1] = False
            nArboles -= 1
        if arbol03.tiempoEncendido > 5:
            vidas -= 1
            arbol03.tiempoEncendido = 0
            arbol03.fuego = False
            arbol03.colision = False
            a3 = False
            c = False
            nArboles2[2] = False
            nArboles -= 1
        if arbol04.tiempoEncendido > 5:
            vidas -= 1
            arbol04.tiempoEncendido = 0
            arbol04.fuego = False
            arbol04.colision = False
            a4 = False
            d = False
            nArboles2[3] = False
            nArboles -= 1
        if vida == 0:
            completo = False
            running = False
        if Nivel1Restart:
            nube.nube.x = 0
            nube.nube.y = 55
            Player.rect.x = 900/2
            Player.rect.x = 450
            avance = True
            running = True
            jugador = False
            a1= False
            a2= False
            a3= False
            a4= False
            a5= False
            a = False
            b = False
            c = False
            d = False
            f = False
            arbol01.colision = False
            arbol02.colision = False
            arbol03.colision = False
            arbol04.colision = False
            score = 0
            segundos = 300
            tiempo = 0
            tiempo2 = 0
            nArboles = 0
            nArboles2 = [False, False, False, False]
            vidas = 3
            Nivel1Restart = False
        avance = nube.Movimiento(avance)
        segundos -= 0.05
        for eventos in pygame.event.get():
            jugador = True
            if eventos.type == pygame.QUIT:
                running = Pause(1)
            if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_ESCAPE:
                running = Pause(1)
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    running = Pause(1)

        screen.blit(bg_image,(0,0))
        screen.blit(pause, (845, 77))
        cursor1.update()
        screen.blit(ranura.image, (61, 524))
        screen.blit(ranura.image, (299, 524))
        screen.blit(ranura.image, (539, 524))
        screen.blit(ranura.image, (772, 524))
        screen.blit(pasto.image, (250, 549))
        screen.blit(pasto.image, (784, 568))
        screen.blit(pasto.image, (80, 540))
        screen.blit(jarron.image, (23, 516))
        screen.blit(jarron.image, (354, 548))
        screen.blit(jarron.image, (756, 504))
        screen.blit(jarron.image, (860, 509))
        screen.blit(barra.image, (0, 0))
        if vidas >= 1:
            screen.blit(vida.image, (717,9))
        if vidas >= 2:
            screen.blit(vida.image, (771,9))
        if vidas >= 3:
            screen.blit(vida.image, (827,9))
        screen.blit(reloj.image, (14, 6))

        if a1:
            if time.time() > a1Future:
                screen.blit(arbol2, (74,447))
                if not a:
                    a1Fut = time.time() + 5
                    a = True
            else:
                screen.blit(arbol1, (74,472))
        if a2:
            if time.time() > a2Future:
                screen.blit(arbol2, (312,447))
                if not b:
                    a2Fut = time.time() + 5
                    b = True
            else:
                screen.blit(arbol1, (312,472))
        if a3:
            if time.time() > a3Future:
                screen.blit(arbol2, (549,447))
                if not c:
                    a3Fut = time.time() + 5
                    c = True
            else:
                screen.blit(arbol1, (549,472))
        if a4:
            if time.time() > a4Future:
                screen.blit(arbol2, (785,447))
                if not d:
                    a4Fut = time.time() + 5
                    d = True
            else:
                screen.blit(arbol1, (785,472))

        if a and time.time() > a1Fut:
            if arbol01.fuego:
                arbol01.encendido()
                arbol01.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol01.rect.x, arbol01.rect.y-5, arbol01.tiempoEncendido*100/5, 5))
            if not nArboles2[0]:
                nArboles2[0] = True
                nArboles += 1
            arbol01.colision = True
            screen.blit(arbol01.image, arbol01.rect)
            a1 = False
        if b and time.time() > a2Fut:
            if arbol02.fuego:
                arbol02.encendido()
                arbol02.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol02.rect.x, arbol03.rect.y-5, arbol02.tiempoEncendido*100/5, 5))
            if not nArboles2[1]:
                nArboles2[1] = True
                nArboles += 1
            arbol02.colision = True
            screen.blit(arbol02.image, arbol02.rect)
            a2 = False
        if c and time.time() > a3Fut:
            if arbol03.fuego:
                arbol03.encendido()
                arbol03.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol03.rect.x, arbol03.rect.y-5, arbol03.tiempoEncendido*100/5, 5))
            if not nArboles2[2]:
                nArboles2[2] = True
                nArboles += 1
            arbol03.colision = True
            screen.blit(arbol03.image, arbol03.rect)
            a3 = False
        if d and time.time() > a4Fut:
            if arbol04.fuego:
                arbol04.encendido()
                arbol04.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol04.rect.x, arbol04.rect.y-5, arbol04.tiempoEncendido*100/5, 5))
            if not nArboles2[3]:
                nArboles2[3] = True
                nArboles += 1
            arbol04.colision = True
            screen.blit(arbol04.image, arbol04.rect)
            a4 = False

        xd = "Puntuacion: " + str(score)
        if segundos <= 0 and vidas >= 1:
            if nArboles >= 4:
                running = complet(True, 1)
            else:
                running = complet(False, 1)
                Nivel1Restart = True
        elif segundos <= 0 and vidas == 0:
            running = complet(False, 1)
        else:
            pygame.draw.rect(screen, (255, 255, 0), (80, 10, 300, 30))
            pygame.draw.rect(screen, (255, 255, 255), (80, 10, segundos, 30))
        if jugador:
            if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                tiempo += 0.01
                tiempo2 += 0.02
                if Player.rect.colliderect(ranura.ran1):
                    if arbol01.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol01.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol01.fuego = False
                            arbol01.image = arbol01.normal
                            arbol01.n = 100
                            arbol01.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol01.tiempoEncendido = 0
                    else:
                        if not a1 and not a:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a1:
                            a1 = True
                            score += 20
                            a1Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran2):
                    if arbol02.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol02.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol02.fuego = False
                            arbol02.image = arbol02.normal
                            arbol02.n = 100
                            arbol02.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol02.tiempoEncendido = 0
                    else:
                        if not a2 and not b:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a2:
                            a2 = True
                            score += 20
                            a2Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran3):
                    if arbol03.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol03.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol03.fuego = False
                            arbol03.image = arbol03.normal
                            arbol03.n = 100
                            arbol03.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol03.tiempoEncendido = 0
                    else:
                        if not a3 and not c:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a3:
                            a3 = True
                            score += 20
                            a3Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran4):
                    if arbol04.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol04.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol04.fuego = False
                            arbol04.image = arbol04.normal
                            arbol04.n = 100
                            arbol04.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol04.tiempoEncendido = 0
                    else:
                        if not a4 and not d:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a4:
                            a4 = True
                            score += 20
                            a4Future = time.time() + 5
            else:
                tiempo2 = 0
                tiempo = 0
            if sexo == 'hombre':
                Player.handle_event(eventos)
                screen.blit(Player.image, Player.rect)
                if Player.stun:
                    screen.blit(Player.imgstun, Player.rect)
                    Player.stun = False
            if sexo == 'mujer':
                Player.handle_event(eventos)
                Playar.handle_event(eventos)
                screen.blit(Playar.image, Player.rect)
                if Player.stun:
                    screen.blit(Player.imgstun, Player.rect)
                    Player.stun = False
        screen.blit(nube.image, (nube.nube))
        nube.ataque()
        if len(nube.listaRayos) > 0:
            for x in nube.listaRayos:
                screen.blit(nube.rayo, x)
                nube.trayectoria(x)
                if arbol01.colision and x.colliderect(arbol01.rect):
                    arbol01.fuego = True
                    x.y += 400
                if arbol02.colision and x.colliderect(arbol02.rect):
                    arbol02.fuego = True
                    x.y += 400
                if arbol03.colision and x.colliderect(arbol03.rect):
                    arbol03.fuego = True
                    x.y += 400
                if arbol04.colision and x.colliderect(arbol04.rect):
                    arbol04.fuego = True
                    x.y += 400
                if x.colliderect(Player.rect):
                    Player.stun = True
                    tiempo = 0
            if vidas == 0:
                running = complet(False, 1)
        pygame.display.flip()
        clock.tick(80)
    if not ppause:
        Nivel2(sexo)
        ppause = False
def Nivel2(sexo):
    nube.velocidad = 5
    nube.rangoDisparo = 7
    global running, Nivel2Restart, ppause
    cursor1=Cursor()
    boton1=Boton(pause,pause,845,77)
    ranura = Ranura()
    completo = False
    avance = True
    running = True
    jugador = False
    nArboles = 4
    nArboles2 = [False, False, False, False]
    a1= False
    a2= False
    a3= False
    a4= False
    a5= False
    a = False
    b = False
    c = False
    d = False
    f = False
    score = 0
    segundos = 3
    tiempo = 0
    tiempo2 = 2
    vidas = 3
    arbol01 = Arboles(57, 409)
    arbol02 = Arboles(294, 409)
    arbol03 = Arboles(534, 409)
    arbol04 = Arboles(768, 409)
    arbol01.colision = False
    arbol02.colision = False
    arbol03.colision = False
    arbol04.colision = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(musicPath,"levelsmusic.mp3"))
    pygame.mixer.music.play()
    Intro(screen, 2)
    while running:
        if arbol01.tiempoEncendido > 5:
            vidas -= 1
            arbol01.tiempoEncendido = 0
            arbol01.fuego = False
            arbol01.colision = False
            a1 = False
            a = False
            nArboles2[0] = False
            nArboles -= 1
        if arbol02.tiempoEncendido > 5:
            vidas -= 1
            arbol02.tiempoEncendido = 0
            arbol02.fuego = False
            arbol02.colision = False
            a2 = False
            b = False
            nArboles2[1] = False
            nArboles -= 1
        if arbol03.tiempoEncendido > 5:
            vidas -= 1
            arbol03.tiempoEncendido = 0
            arbol03.fuego = False
            arbol03.colision = False
            a3 = False
            c = False
            nArboles2[2] = False
            nArboles -= 1
        if arbol04.tiempoEncendido > 5:
            vidas -= 1
            arbol04.tiempoEncendido = 0
            arbol04.fuego = False
            arbol04.colision = False
            a4 = False
            d = False
            nArboles2[3] = False
            nArboles -= 1
        if vida == 0:
            completo = False
            running = False
        if Nivel2Restart:
            nube.nube.x = 0
            nube.nube.y = 55
            Player.rect.x = 900/2
            Player.rect.x = 450
            avance = True
            running = True
            jugador = False
            a1= False
            a2= False
            a3= False
            a4= False
            a5= False
            a = False
            b = False
            c = False
            d = False
            f = False
            arbol01.colision = False
            arbol02.colision = False
            arbol03.colision = False
            arbol04.colision = False
            score = 0
            segundos = 300
            tiempo = 0
            tiempo2 = 0
            nArboles = 0
            nArboles2 = [False, False, False, False]
            vidas = 3
            Nivel2Restart = False
        avance = nube.Movimiento(avance)
        segundos -= 0.05
        for eventos in pygame.event.get():
            jugador = True
            if eventos.type == pygame.QUIT:
                running = Pause(2)
            if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_ESCAPE:
                running = Pause(2)
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    running = Pause(2)
        screen.blit(bg_image2,(0,0))
        screen.blit(pause, (845, 77))
        cursor1.update()
        screen.blit(ranura.image, (61, 524))
        screen.blit(ranura.image, (299, 524))
        screen.blit(ranura.image, (539, 524))
        screen.blit(ranura.image, (772, 524))
        screen.blit(pasto.image, (250, 549))
        screen.blit(pasto.image, (784, 568))
        screen.blit(pasto.image, (80, 540))
        screen.blit(jarron.image, (23, 516))
        screen.blit(jarron.image, (354, 548))
        screen.blit(jarron.image, (756, 504))
        screen.blit(jarron.image, (860, 509))
        screen.blit(barra.image, (0, 0))
        if vidas >= 1:
            screen.blit(vida.image, (717,9))
        if vidas >= 2:
            screen.blit(vida.image, (771,9))
        if vidas >= 3:
            screen.blit(vida.image, (827,9))
        screen.blit(reloj.image, (14, 6))

        if a1:
            if time.time() > a1Future:
                screen.blit(arbol2, (74,447))
                if not a:
                    a1Fut = time.time() + 5
                    a = True
            else:
                screen.blit(arbol1, (74,472))
        if a2:
            if time.time() > a2Future:
                screen.blit(arbol2, (312,447))
                if not b:
                    a2Fut = time.time() + 5
                    b = True
            else:
                screen.blit(arbol1, (312,472))
        if a3:
            if time.time() > a3Future:
                screen.blit(arbol2, (549,447))
                if not c:
                    a3Fut = time.time() + 5
                    c = True
            else:
                screen.blit(arbol1, (549,472))
        if a4:
            if time.time() > a4Future:
                screen.blit(arbol2, (785,447))
                if not d:
                    a4Fut = time.time() + 5
                    d = True
            else:
                screen.blit(arbol1, (785,472))

        if a and time.time() > a1Fut:
            if arbol01.fuego:
                arbol01.encendido()
                arbol01.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol01.rect.x, arbol01.rect.y-5, arbol01.tiempoEncendido*100/5, 5))
            if not nArboles2[0]:
                nArboles2[0] = True
                nArboles += 1
            arbol01.colision = True
            screen.blit(arbol01.image, arbol01.rect)
            a1 = False
        if b and time.time() > a2Fut:
            if arbol02.fuego:
                arbol02.encendido()
                arbol02.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol02.rect.x, arbol03.rect.y-5, arbol02.tiempoEncendido*100/5, 5))
            if not nArboles2[1]:
                nArboles2[1] = True
                nArboles += 1
            arbol02.colision = True
            screen.blit(arbol02.image, arbol02.rect)
            a2 = False
        if c and time.time() > a3Fut:
            if arbol03.fuego:
                arbol03.encendido()
                arbol03.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol03.rect.x, arbol03.rect.y-5, arbol03.tiempoEncendido*100/5, 5))
            if not nArboles2[2]:
                nArboles2[2] = True
                nArboles += 1
            arbol03.colision = True
            screen.blit(arbol03.image, arbol03.rect)
            a3 = False
        if d and time.time() > a4Fut:
            if arbol04.fuego:
                arbol04.encendido()
                arbol04.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol04.rect.x, arbol04.rect.y-5, arbol04.tiempoEncendido*100/5, 5))
            if not nArboles2[3]:
                nArboles2[3] = True
                nArboles += 1
            arbol04.colision = True
            screen.blit(arbol04.image, arbol04.rect)
            a4 = False

        xd = "Puntuacion: " + str(score)
        if segundos <= 0 and vidas >= 1:
            if nArboles >= 4:
                running = complet(True, 2)
            else:
                running = complet(False, 2)
                Nivel2Restart = True
        elif segundos <= 0 and vidas == 0:
            running = complet(False, 2)
        else:
            pygame.draw.rect(screen, (255, 255, 0), (80, 10, 300, 30))
            pygame.draw.rect(screen, (255, 255, 255), (80, 10, segundos, 30))
        if jugador:
            if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                tiempo += 0.01
                tiempo2 += 0.02
                if Player.rect.colliderect(ranura.ran1):
                    if arbol01.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol01.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol01.fuego = False
                            arbol01.image = arbol01.normal
                            arbol01.n = 100
                            arbol01.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol01.tiempoEncendido = 0
                    else:
                        if not a1 and not a:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a1:
                            a1 = True
                            score += 20
                            a1Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran2):
                    if arbol02.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol02.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol02.fuego = False
                            arbol02.image = arbol02.normal
                            arbol02.n = 100
                            arbol02.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol02.tiempoEncendido = 0
                    else:
                        if not a2 and not b:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a2:
                            a2 = True
                            score += 20
                            a2Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran3):
                    if arbol03.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol03.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol03.fuego = False
                            arbol03.image = arbol03.normal
                            arbol03.n = 100
                            arbol03.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol03.tiempoEncendido = 0
                    else:
                        if not a3 and not c:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a3:
                            a3 = True
                            score += 20
                            a3Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran4):
                    if arbol04.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol04.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol04.fuego = False
                            arbol04.image = arbol04.normal
                            arbol04.n = 100
                            arbol04.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol04.tiempoEncendido = 0
                    else:
                        if not a4 and not d:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a4:
                            a4 = True
                            score += 20
                            a4Future = time.time() + 5
            else:
                tiempo2 = 0
                tiempo = 0
            if sexo == 'hombre':
                Player.handle_event(eventos)
                screen.blit(Player.image, Player.rect)
                if Player.stun:
                    screen.blit(Player.imgstun, Player.rect)
                    Player.stun = False
            if sexo == 'mujer':
                Player.handle_event(eventos)
                Playar.handle_event(eventos)
                screen.blit(Playar.image, Player.rect)
                if Player.stun:
                    screen.blit(Player.imgstun, Player.rect)
                    Player.stun = False
        screen.blit(nube.image, (nube.nube))
        nube.ataque()
        if len(nube.listaRayos) > 0:
            for x in nube.listaRayos:
                screen.blit(nube.rayo, x)
                nube.trayectoria(x)
                if arbol01.colision and x.colliderect(arbol01.rect):
                    arbol01.fuego = True
                    x.y += 400
                if arbol02.colision and x.colliderect(arbol02.rect):
                    arbol02.fuego = True
                    x.y += 400
                if arbol03.colision and x.colliderect(arbol03.rect):
                    arbol03.fuego = True
                    x.y += 400
                if arbol04.colision and x.colliderect(arbol04.rect):
                    arbol04.fuego = True
                    x.y += 400
                if x.colliderect(Player.rect):
                    Player.stun = True
                    tiempo = 0
            if vidas == 0:
                running = complet(False, 2)
        pygame.display.flip()
        clock.tick(80)
    if not ppause:
        Nivel3(sexo)
        ppause = False
def Nivel3(sexo):
    nube.velocidad = 5
    nube.rangoDisparo = 7
    global running, Nivel3Restart
    cursor1=Cursor()
    boton1=Boton(pause,pause,845,77)
    ranura = Ranura()
    completo = False
    avance = True
    running = True
    jugador = False
    nArboles = 0
    nArboles2 = [False, False, False, False]
    a1= False
    a2= False
    a3= False
    a4= False
    a5= False
    a = False
    b = False
    c = False
    d = False
    f = False
    score = 0
    segundos = 300
    tiempo = 0
    tiempo2 = 2
    vidas = 3
    arbol01 = Arboles(57, 409)
    arbol02 = Arboles(294, 409)
    arbol03 = Arboles(534, 409)
    arbol04 = Arboles(768, 409)
    arbol01.colision = False
    arbol02.colision = False
    arbol03.colision = False
    arbol04.colision = False
    pygame.mixer.music.stop()
    pygame.mixer.music.load(os.path.join(musicPath,"levelsmusic.mp3"))
    pygame.mixer.music.play()
    Intro(screen, 3)
    while running:
        if arbol01.tiempoEncendido > 5:
            vidas -= 1
            arbol01.tiempoEncendido = 0
            arbol01.fuego = False
            arbol01.colision = False
            a1 = False
            a = False
            nArboles2[0] = False
            nArboles -= 1
        if arbol02.tiempoEncendido > 5:
            vidas -= 1
            arbol02.tiempoEncendido = 0
            arbol02.fuego = False
            arbol02.colision = False
            a2 = False
            b = False
            nArboles2[1] = False
            nArboles -= 1
        if arbol03.tiempoEncendido > 5:
            vidas -= 1
            arbol03.tiempoEncendido = 0
            arbol03.fuego = False
            arbol03.colision = False
            a3 = False
            c = False
            nArboles2[2] = False
            nArboles -= 1
        if arbol04.tiempoEncendido > 5:
            vidas -= 1
            arbol04.tiempoEncendido = 0
            arbol04.fuego = False
            arbol04.colision = False
            a4 = False
            d = False
            nArboles2[3] = False
            nArboles -= 1
        if vida == 0:
            completo = False
            running = False
        if Nivel3Restart:
            nube.nube.x = 0
            nube.nube.y = 55
            Player.rect.x = 900/2
            Player.rect.x = 450
            avance = True
            running = True
            jugador = False
            a1= False
            a2= False
            a3= False
            a4= False
            a5= False
            a = False
            b = False
            c = False
            d = False
            f = False
            arbol01.colision = False
            arbol02.colision = False
            arbol03.colision = False
            arbol04.colision = False
            score = 0
            segundos = 300
            tiempo = 0
            tiempo2 = 0
            nArboles = 0
            nArboles2 = [False, False, False, False]
            vidas = 3
            Nivel3Restart = False
        avance = nube.Movimiento(avance)
        segundos -= 0.05
        for eventos in pygame.event.get():
            jugador = True
            if eventos.type == pygame.QUIT:
                running = Pause(3)
            if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_ESCAPE:
                running = Pause(3)
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    running = Pause(3)

        screen.blit(bg_image3,(0,-75))
        screen.blit(pause, (845, 77))
        cursor1.update()
        screen.blit(ranura.image, (61, 524))
        screen.blit(ranura.image, (299, 524))
        screen.blit(ranura.image, (539, 524))
        screen.blit(ranura.image, (772, 524))
        screen.blit(pasto.image, (250, 549))
        screen.blit(pasto.image, (784, 568))
        screen.blit(pasto.image, (80, 540))
        screen.blit(jarron.image, (23, 516))
        screen.blit(jarron.image, (354, 548))
        screen.blit(jarron.image, (756, 504))
        screen.blit(jarron.image, (860, 509))
        screen.blit(barra.image, (0, 0))
        if vidas >= 1:
            screen.blit(vida.image, (717,9))
        if vidas >= 2:
            screen.blit(vida.image, (771,9))
        if vidas >= 3:
            screen.blit(vida.image, (827,9))
        screen.blit(reloj.image, (14, 6))

        if a1:
            if time.time() > a1Future:
                screen.blit(arbol2, (74,447))
                if not a:
                    a1Fut = time.time() + 5
                    a = True
            else:
                screen.blit(arbol1, (74,472))
        if a2:
            if time.time() > a2Future:
                screen.blit(arbol2, (312,447))
                if not b:
                    a2Fut = time.time() + 5
                    b = True
            else:
                screen.blit(arbol1, (312,472))
        if a3:
            if time.time() > a3Future:
                screen.blit(arbol2, (549,447))
                if not c:
                    a3Fut = time.time() + 5
                    c = True
            else:
                screen.blit(arbol1, (549,472))
        if a4:
            if time.time() > a4Future:
                screen.blit(arbol2, (785,447))
                if not d:
                    a4Fut = time.time() + 5
                    d = True
            else:
                screen.blit(arbol1, (785,472))

        if a and time.time() > a1Fut:
            if arbol01.fuego:
                arbol01.encendido()
                arbol01.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol01.rect.x, arbol01.rect.y-5, arbol01.tiempoEncendido*100/5, 5))
            if not nArboles2[0]:
                nArboles2[0] = True
                nArboles += 1
            arbol01.colision = True
            screen.blit(arbol01.image, arbol01.rect)
            a1 = False
        if b and time.time() > a2Fut:
            if arbol02.fuego:
                arbol02.encendido()
                arbol02.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol02.rect.x, arbol03.rect.y-5, arbol02.tiempoEncendido*100/5, 5))
            if not nArboles2[1]:
                nArboles2[1] = True
                nArboles += 1
            arbol02.colision = True
            screen.blit(arbol02.image, arbol02.rect)
            a2 = False
        if c and time.time() > a3Fut:
            if arbol03.fuego:
                arbol03.encendido()
                arbol03.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol03.rect.x, arbol03.rect.y-5, arbol03.tiempoEncendido*100/5, 5))
            if not nArboles2[2]:
                nArboles2[2] = True
                nArboles += 1
            arbol03.colision = True
            screen.blit(arbol03.image, arbol03.rect)
            a3 = False
        if d and time.time() > a4Fut:
            if arbol04.fuego:
                arbol04.encendido()
                arbol04.tiempoEncendido += 0.01
                pygame.draw.rect(screen, (255, 0, 0), (arbol04.rect.x, arbol04.rect.y-5, arbol04.tiempoEncendido*100/5, 5))
            if not nArboles2[3]:
                nArboles2[3] = True
                nArboles += 1
            arbol04.colision = True
            screen.blit(arbol04.image, arbol04.rect)
            a4 = False

        xd = "Puntuacion: " + str(score)
        if segundos <= 0 and vidas >= 1:
            if nArboles >= 4:
                running = complet(True, 3)
            else:
                running = complet(False, 3)
                Nivel3Restart = True
        elif segundos <= 0 and vidas == 0:
            running = complet(False, 3)
        else:
            pygame.draw.rect(screen, (255, 255, 0), (80, 10, 300, 30))
            pygame.draw.rect(screen, (255, 255, 255), (80, 10, segundos, 30))
        if jugador:
            if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                tiempo += 0.01
                tiempo2 += 0.02
                if Player.rect.colliderect(ranura.ran1):
                    if arbol01.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol01.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol01.fuego = False
                            arbol01.image = arbol01.normal
                            arbol01.n = 100
                            arbol01.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol01.tiempoEncendido = 0
                    else:
                        if not a1 and not a:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a1:
                            a1 = True
                            score += 20
                            a1Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran2):
                    if arbol02.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol02.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol02.fuego = False
                            arbol02.image = arbol02.normal
                            arbol02.n = 100
                            arbol02.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol02.tiempoEncendido = 0
                    else:
                        if not a2 and not b:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a2:
                            a2 = True
                            score += 20
                            a2Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran3):
                    if arbol03.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol03.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol03.fuego = False
                            arbol03.image = arbol03.normal
                            arbol03.n = 100
                            arbol03.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol03.tiempoEncendido = 0
                    else:
                        if not a3 and not c:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a3:
                            a3 = True
                            score += 20
                            a3Future = time.time() + 5
                if Player.rect.colliderect(ranura.ran4):
                    if arbol04.fuego:
                        pygame.draw.rect(screen, (95, 102, 233), (Player.rect.x-20,Player.rect.y - 10, (tiempo2*80)/3, 5))
                        arbol04.tiempoEncendido -= 0.01
                        if tiempo2 >= 3:
                            arbol04.fuego = False
                            arbol04.image = arbol04.normal
                            arbol04.n = 100
                            arbol04.rect.y = 409
                            tiempo2 = 0
                            tiempo = 0
                            arbol04.tiempoEncendido = 0
                    else:
                        if not a4 and not d:
                            pygame.draw.rect(screen, (17, 140, 44), (Player.rect.x-20,Player.rect.y - 10, (tiempo*80)/1.5, 5))
                    if tiempo >= 1.5:
                        tiempo = 0
                        if not a4:
                            a4 = True
                            score += 20
                            a4Future = time.time() + 5
            else:
                tiempo2 = 0
                tiempo = 0
            if sexo == 'hombre':
                Player.handle_event(eventos)
                screen.blit(Player.image, Player.rect)
                if Player.stun:
                    screen.blit(Player.imgstun, Player.rect)
                    Player.stun = False
            if sexo == 'mujer':
                Player.handle_event(eventos)
                Playar.handle_event(eventos)
                screen.blit(Playar.image, Player.rect)
                if Player.stun:
                    screen.blit(Player.imgstun, Player.rect)
                    Player.stun = False
        screen.blit(nube.image, (nube.nube))
        nube.ataque()
        if len(nube.listaRayos) > 0:
            for x in nube.listaRayos:
                screen.blit(nube.rayo, x)
                nube.trayectoria(x)
                if arbol01.colision and x.colliderect(arbol01.rect):
                    arbol01.fuego = True
                    x.y += 400
                if arbol02.colision and x.colliderect(arbol02.rect):
                    arbol02.fuego = True
                    x.y += 400
                if arbol03.colision and x.colliderect(arbol03.rect):
                    arbol03.fuego = True
                    x.y += 400
                if arbol04.colision and x.colliderect(arbol04.rect):
                    arbol04.fuego = True
                    x.y += 400
                if x.colliderect(Player.rect):
                    Player.stun = True
                    tiempo = 0
                    if segundos <= 300:
                        segundos += 0.5
            if vidas == 0:
                running = complet(False, 3)
        pygame.display.flip()
        clock.tick(80)

class Cursor(pygame.Rect):
        def __init__(self):
            pygame.Rect.__init__(self,0,0,1,1)
        def update(self):
            self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
            self.imagen_normal=imagen1
            self.imagen_seleccion=imagen2
            self.imagen_actual=self.imagen_normal
            self.rect=self.imagen_actual.get_rect()
            self.rect.left,self.rect.top=(x,y)

    def update(self,screen,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal


        screen.blit(self.imagen_actual,self.rect)
reloj1=pygame.time.Clock()
play1=pygame.image.load(os.path.join(image_path, 'play1.png'))
play2=pygame.image.load(os.path.join(image_path, 'play2.png'))
options1=pygame.image.load(os.path.join(image_path, 'options1.png'))
options2=pygame.image.load(os.path.join(image_path, 'options2.png'))
exit1=pygame.image.load(os.path.join(image_path, 'exit1.png'))
exit2=pygame.image.load(os.path.join(image_path, 'exit2.png'))
fondo=pygame.image.load(os.path.join(image_path, 'menu.png'))
selecper=pygame.image.load(os.path.join(image_path, 'selecper.png'))
menuopt=pygame.image.load(os.path.join(image_path, 'menuopt.png'))
hombre1=pygame.image.load(os.path.join(image_path, 'hombre2.png'))
hombre2=pygame.image.load(os.path.join(image_path, 'hombre1.png'))
mujer1=pygame.image.load(os.path.join(image_path, 'mujer1.png'))
mujer2=pygame.image.load(os.path.join(image_path, 'mujer2.png'))
back1=pygame.image.load(os.path.join(image_path, 'back1.png'))
back2=pygame.image.load(os.path.join(image_path, 'back2.png'))
regres=pygame.image.load(os.path.join(pausaPath, "back1.png"))
regres1=pygame.image.load(os.path.join(pausaPath, "back2.png"))
exitt=pygame.image.load(os.path.join(pausaPath,"exit1.png"))
exitt1=pygame.image.load(os.path.join(pausaPath,"exit2.png"))
sound1=pygame.image.load(os.path.join(image_path, 'sound1.png'))
notsound1=pygame.image.load(os.path.join(image_path, 'notsound1.png'))
sound2=pygame.image.load(os.path.join(image_path, 'sound2.png'))
notsound2=pygame.image.load(os.path.join(image_path, 'notsound2.png'))
pause=pygame.image.load(os.path.join(image_path, 'pause.png'))
menpause=pygame.image.load(os.path.join(image_path, 'menpause.png'))
completado=pygame.image.load(os.path.join(image_path, 'completado.png'))
incompleto=pygame.image.load(os.path.join(image_path, 'incompleto.png'))

def seleccionDePersonaje():
    global selecper
    seleccion = False
    boton1=Boton(hombre1,hombre2,113,187)
    boton2=Boton(mujer1,mujer2,490,187)
    boton3=Boton(exit1,exit2,814,17)
    cursor1=Cursor()
    while seleccion!=True:
        screen.blit(selecper, (0,0))
        reloj1.tick(30)
        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
        for eventos in pygame.event.get():
            if eventos.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    seleccion = True
                    Nivel1("hombre")
                    return
                if cursor1.colliderect(boton2.rect):
                    seleccion = True
                    Nivel1("mujer")
                    return
                if cursor1.colliderect(boton3.rect):
                    return
            if eventos.type == pygame.QUIT:
                salir=True

# Opciones
def opciones():
    global menuopt
    seleccion = False
    boton3=Boton(back1,back2,33,25)
    boton2=Boton(sound1,sound2,284,214)
    boton1=Boton(notsound1,notsound2,492,214)

    cursor1=Cursor()
    while seleccion!=True:
        screen.blit(menuopt, (0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    pygame.mixer.music.set_volume(0)
                if cursor1.colliderect(boton2.rect):
                    pygame.mixer.music.set_volume(0.2)
                if cursor1.colliderect(boton3.rect):
                    return

            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
def Menu():
    pygame.mixer.music.load(os.path.join(musicPath,"menumusic.mp3"))
    pygame.mixer.music.play(4)
    pygame.mixer.music.set_volume(0.2)
    boton1=Boton(play1,play2,404,249)
    boton2=Boton(options1,options2,33,11)
    boton3=Boton(exit1,exit2,814,17)
    cursor1=Cursor()
    salir=False
    while salir!=True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    seleccionDePersonaje()
                if cursor1.colliderect(boton2.rect):
                    opciones()
                if cursor1.colliderect(boton3.rect):
                    salir = True
            if event.type == pygame.QUIT:
                salir=True
        reloj1.tick(30)
        screen.blit(fondo, (0,0))
        cursor1.update()
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
    pygame.quit()

menu1 = pygame.image.load(os.path.join(image_path, 'menu1.png'))
menu2 = pygame.image.load(os.path.join(image_path, 'menu2.png'))
menu3 = pygame.image.load(os.path.join(image_path, 'menu3.png'))
menu4 = pygame.image.load(os.path.join(image_path, 'menu4.png'))
menuint = pygame.image.load(os.path.join(image_path, 'intjug.png'))
int1 = pygame.image.load(os.path.join(image_path, 'int1.png'))
int2 = pygame.image.load(os.path.join(image_path, 'int2.png'))
int3 = pygame.image.load(os.path.join(image_path, 'int3.png'))
int4 = pygame.image.load(os.path.join(image_path, 'int4.png'))
int5 = pygame.image.load(os.path.join(image_path, 'int5.png'))
int6 = pygame.image.load(os.path.join(image_path, 'int6.png'))
int8 = pygame.image.load(os.path.join(image_path, 'int8.png'))
int9 = pygame.image.load(os.path.join(image_path, 'int9.png'))
def Intro(screen, n):
    option = 0
    running = True
    evento = False
    if n == 1:
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(menu1, (0,0))
            pygame.display.update()
        running = True
        evento = False
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menu2, (0,0))
            pygame.display.update()
        running = True
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menuint, (0,0))
            screen.blit(int1, (287,41))
            pygame.display.update()
        running = True
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menuint, (0,0))
            screen.blit(int2, (287,41))
            pygame.display.update()
        running = True
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menuint, (0,0))
            screen.blit(int3, (287,41))
            pygame.display.update()
        running = True
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menuint, (0,0))
            screen.blit(int4, (287,41))
            pygame.display.update()
        running = True
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menuint, (0,0))
            screen.blit(int5, (287,41))
            pygame.display.update()
        running = True
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menuint, (0,0))
            screen.blit(int6, (287,41))
            pygame.display.update()
        running = True
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menuint, (0,0))
            screen.blit(int8, (287,41))
            pygame.display.update()
        running = True
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image, (0,0))
            screen.blit(menuint, (0,0))
            screen.blit(int9, (287,41))
            pygame.display.update()
    if n == 2:
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image2, (0,0))
            screen.blit(menu3, (0,0))
            pygame.display.update()
        running = True
    if n == 3:
        while running:
            for eventos in pygame.event.get():
                if eventos.type == pygame.QUIT:
                    running = False
                if eventos.type == pygame.KEYDOWN and eventos.key == pygame.K_SPACE:
                    running = False
            screen.blit(bg_image3, (0,0))
            screen.blit(menu4, (0,0))
            pygame.display.update()
        running = True
Menu()
