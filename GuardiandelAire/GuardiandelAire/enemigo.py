import pygame
from random import randint
import os

currentPath = os.path.dirname(__file__) #path where is main.py
#resourcePath = os.path.join(currentPath, 'GuardiandelAire')
imagePath = os.path.join(currentPath, 'assets') #path where the images are
musicPath = os.path.join(imagePath, 'musica') #path where misuc are

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, posX, posY):
        #self.image = pygame.image.load("assets/nube.png")
        self.image = pygame.image.load(os.path.join(imagePath,"nube.png"))
        self.rayo = pygame.image.load(os.path.join(imagePath,"rayo.png"))
        self.rect = self.rayo.get_rect()
        self.nube = self.image.get_rect()
        self.listaRayos = []
        self.velocidad = 1
        self.nube.left = posX
        self.nube.top = posY
        self.rangoDisparo = 5
        self.sonidoDisparo = pygame.mixer.Sound(os.path.join(musicPath,"rayo.wav"))
        self.sonidoDisparo.set_volume(0.2)

    def Movimiento(self, avance):
        if avance:
            if self.nube.x >= 700:
                avance = False
                return avance
            else:
                self.nube.x += self.velocidad
                return avance
        else:
            if self.nube.x <= 0:
                avance = True
                return avance
            else:
                self.nube.x -= self.velocidad
                return avance
    def ataque(self):
        if (randint(0,300)<self.rangoDisparo):
            self.disparo()
    def disparo(self):
        x,y  = self.nube.center
        y += 20
        miProyectil = pygame.Rect((x, y), (10, 10))
        self.listaRayos.append(miProyectil)
        self.sonidoDisparo.play()
    def trayectoria(self, rayo):
        if rayo.y < 600:
            rayo.y += 3
        else:
            del rayo
