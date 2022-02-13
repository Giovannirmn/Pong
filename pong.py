import pygame
import random
import math
from pygame.locals import *

pygame.init()
win = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Pong")
fps = pygame.time.Clock()
font = pygame.font.SysFont(None, 23)

running = True
nero = (0, 0, 0)
bianco = (255, 255, 255)
punteggio1 = 0
punteggio2 = 0

class Player:
    def __init__(self, x, y):
        self.colore = (255, 255, 255)
        self.vel = 9
        self.coll = pygame.Rect(x, y, 15, 100)
    
    def disegna(self):
        pygame.draw.rect(win, self.colore, self.coll)

class Palla:
    def __init__(self, x, y):
        self.colore = (255, 255, 255)
        self.vel = 9
        self.yvel = 7
        self.xdir = -1
        self.ydir = randomdir()
        self.xvel = math.sqrt(self.vel**2 - (self.yvel*self.ydir)**2)
        self.coll = pygame.Rect(x, y, 15, 15)

    def spawn(self, dir):
        self.ydir = randomdir()
        self.xvel = math.sqrt(self.vel**2 - (self.yvel*self.ydir)**2)
        self.coll.x = 443
        self.coll.y = 293
        if dir == 1:
            self.xdir = -1     
        elif dir == -1:
            self.xdir = 1

    def check(self):
        global punteggio1, punteggio2, running

        if self.coll.bottom > 600 or self.coll.top < 0:
            self.ydir *= -1
        elif self.coll.right >= 900:
            self.spawn(1)
            punteggio1 += 1
            if punteggio1 == 10:
                running = False
        elif self.coll.left <= 0:
            self.spawn(-1)
            punteggio2 += 1
            if punteggio2 == 10:
                running = False

        if self.coll.colliderect(player1.coll) or self.coll.colliderect(player2.coll):
            if abs(player1.coll.top - palla.coll.bottom) < 10 and palla.ydir < 0:
                palla.ydir *= -1
            if abs(player1.coll.bottom - palla.coll.top) < 10 and palla.ydir > 0:
                palla.ydir *= -1
            if abs(player1.coll.right - palla.coll.left) < 10 and palla.xdir < 0:
                palla.xdir *= -1
            if abs(player2.coll.top - palla.coll.bottom) < 10 and palla.ydir < 0:
                palla.ydir *= -1
            if abs(player2.coll.bottom - palla.coll.top) < 10 and palla.ydir > 0:
                palla.ydir *= -1
            if abs(player2.coll.left - palla.coll.right) < 10 and palla.xdir > 0:
                palla.xdir *= -1

    def disegna(self):
        self.coll.x += self.xvel * self.xdir
        self.coll.y += self.vel * self.ydir
        pygame.draw.rect(win, bianco, palla.coll)
  

def move():
    keys = pygame.key.get_pressed()       
    if keys[pygame.K_UP] and player2.coll.top >= 0: 
        player2.coll.y -= player2.vel         
    if keys[pygame.K_DOWN] and player2.coll.bottom <= 600: 
        player2.coll.y += player2.vel        
    if keys[pygame.K_w] and player1.coll.top >= 0: 
        player1.coll.y -= player1.vel          
    if keys[pygame.K_s] and player1.coll.bottom <= 600: 
        player1.coll.y += player1.vel

def randomdir():
    a = random.uniform(0.2, 0.8)
    b = random.uniform(-0.2, -0.8)
    scelta = random.randint(0, 1)
    if scelta == 0:
        return a
    else:
        return b

def punteggio():
    testo1 = font.render("Punteggio: " + str(punteggio1), True, bianco)
    testo2 = font.render("Punteggio: " + str(punteggio2), True, bianco)
    win.blit(testo1, (130, 5))
    win.blit(testo2, (700, 5))


player1 = Player(20, 250)
player2 = Player(860, 250)
palla = Palla(443, 293)

while running:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move()
    palla.check()
    win.fill(nero)
    player1.disegna()
    player2.disegna()
    palla.disegna()
    punteggio()
    pygame.display.update()
    fps.tick(60)
    
pygame.quit()