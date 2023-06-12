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
