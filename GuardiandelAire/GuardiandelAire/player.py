import pygame
import os

currentPath = os.path.dirname(__file__) #path where is main.py
imagePath = os.path.join(currentPath, 'assets') #path where the images are
musicPath = os.path.join(imagePath, 'musica') #path where misuc are

salto = False
bajada = False
class Mono(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load(os.path.join(imagePath,'player.png'))
        self.sheet.set_clip(pygame.Rect(0, 0, 51, 106))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 6: (0, 106, 51, 106), 5: (63, 106, 51, 106), 4: (126, 106, 57, 106), 3: (189, 106, 51, 106), 2: (252, 106, 51, 106), 1: (315, 106, 63, 106), 0: (378, 106, 51, 106) }
        self.right_states = { 0: (0, 0, 51, 106), 1: (63, 0, 51, 106), 2: (126, 0, 57, 106), 3: (189, 0, 51, 106), 4: (252, 0, 51, 106), 5: (315, 0, 63, 106), 6: (378, 0, 51, 106) }
        self.stun = False
        self.imgstun = pygame.image.load(os.path.join(imagePath,'playerstun.png'))
        self.condicion = 0

    def get_frame(self, frame_set):
        if self.condicion > 5:
            self.frame += 1
            self.condicion = 0
        else:
            self.condicion += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            if self.rect.x > 10:
                self.clip(self.left_states)
                if not self.stun:
                    self.rect.x -= 5
        if direction == 'right':
            if self.rect.x < 842:
                self.clip(self.right_states)
                if not self.stun:
                    self.rect.x += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, e):
        global salto
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                self.update('left')
            if e.key == pygame.K_RIGHT:
                self.update('right')
            if not self.stun:
                if e.key == pygame.K_UP and self.rect.y == 450:
                    salto = True
        if e.type == pygame.KEYUP:

            if e.key == pygame.K_LEFT:
                self.update('stand_left')
            if e.key == pygame.K_RIGHT:
                self.update('stand_right')
            if e.key == pygame.K_UP:
                salto = False
        self.brinco()

    def brinco(self):
        global salto, bajada
        if not bajada :
            if self.rect.y < 450 and self.rect.y >= 350:
                self.rect.y -= 5
            if salto and self.rect.y == 450 and not self.stun:
                self.rect.y -= 5
            if self.rect.y == 345:
                bajada = True
        else:
            if self.rect.y < 450:
                self.rect.y += 5
            if self.rect.y == 450:
                bajada = False

class Mona(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load(os.path.join(imagePath,'playermujer1.png'))
        self.sheet.set_clip(pygame.Rect(0, 0, 51, 106))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 6: (0, 106, 51, 106), 5: (63, 106, 51, 106), 4: (126, 106, 57, 106), 3: (189, 106, 51, 106), 2: (252, 106, 51, 106), 1: (315, 106, 63, 106), 0: (378, 106, 51, 106) }
        self.right_states = { 0: (0, 0, 52, 106), 1: (63, 0, 51, 106), 2: (126, 0, 57, 106), 3: (189, 0, 51, 106), 4: (252, 0, 51, 106), 5: (315, 0, 63, 106), 6: (378, 0, 51, 106) }
        self.condicion = 0

    def get_frame(self, frame_set):
        if self.condicion > 5:
            self.frame += 1
            self.condicion = 0
        else:
            self.condicion += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            if self.rect.x > 10:
                self.clip(self.left_states)
                self.rect.x -= 5
        if direction == 'right':
            if self.rect.x < 842:
                self.clip(self.right_states)
                self.rect.x += 5

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, e):
        global salto
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:

            if e.key == pygame.K_LEFT:
                self.update('left')
            if e.key == pygame.K_RIGHT:
                self.update('right')
        if e.type == pygame.KEYUP:

            if e.key == pygame.K_LEFT:
                self.update('stand_left')
            if e.key == pygame.K_RIGHT:
                self.update('stand_right')
