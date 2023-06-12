import pygame
from definicja_klas import *
import time
window = pygame.display.set_mode((800, 600)) #tworzy okno
pygame.font.init()

def level_one(iloscTali):
    talia=Talia(iloscTali)
    PrzyciskPasu=True
    punktyZAsemGracza=0
    punktyZAsemBrukiera=0
    run=True
    clock=0
    punkty=0
    tlo_gra=pygame.image.load("zdjecia\Beznazwy.png")
    punktyBrukiera=0
    kartygracza=0
    punktyGracza=0
    losuj = True
    tablicaObiektow=[]
    tablicaObiektowBrukier=[]
    przyciskDoboruBool=True
    last_created_time = time.time()
    iloscpostaci=0
    start_time = pygame.time.get_ticks()
    while run:
        rewerse = pygame.image.load("zdjecia\wrew.png")
        cofanie_button = Button(600, 50, "zdjecia\cofanie.png", "zdjecia\cofanie1.png")
        current_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        keys = pygame.key.get_pressed()
        window.fill((181,11,11))
        window.blit(tlo_gra, (0, 0))
