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
        ilosc_punktow_aktualna = pygame.font.Font.render(pygame.font.SysFont("arial", 200), str(punktyGracza), True,
                                                         (0, 0, 0))
        ilosc_punktow_aktualna_brukiera = pygame.font.Font.render(pygame.font.SysFont("arial", 200),str(punktyBrukiera), True, (0, 0, 0))

        window.blit(ilosc_punktow_aktualna_brukiera, (0, 0))



        window.blit(ilosc_punktow_aktualna, (0, 400)
def main(): #to jest menu

    wygrana=0
    remis=0
    przegrana=0
    clock=0
    plik1=open("D:\karty\zapisyWPR.txt", "r")

    if plik1.readable():
        linesSprawdza = plik1.readlines()
        if len(linesSprawdza) >= 3:
            plik1.seek(0)
            lines = plik1.readlines()
            last_three_lines = lines[-3:]
            wygrana=int(last_three_lines[0])
            przegrana=int(last_three_lines[1])
            remis=int(last_three_lines[2])



    matrix=pygame.image.load("D:\karty\poop.png")
    tlo_menu = pygame.image.load("D:\menu.png")
    run=True
    play_button=Button(100, 200,"D:\przycisk.png", "D:\przycisk_hovered.png")
    tworcy_butoon=Button(100, 420, "D:\karty\zdjtworcy.png", "D:\karty\zdjtworcy1.png")

    iloscTali=1
    window.blit(tlo_menu, (0, 0))
    plik1 = open("D:\karty\zapisyWPR.txt", "w")
    ###
    reser_button = Button(100, 300, "D:\karty\wreser.png", "D:\karty\wreset1.png")
    
