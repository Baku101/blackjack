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
    plik1=open("zapisyWPR.txt", "r")

    if plik1.readable():
        linesSprawdza = plik1.readlines()
        if len(linesSprawdza) >= 3:
            plik1.seek(0)
            lines = plik1.readlines()
            last_three_lines = lines[-3:]
            wygrana=int(last_three_lines[0])
            przegrana=int(last_three_lines[1])
            remis=int(last_three_lines[2])



    matrix=pygame.image.load("zdjecia\poop.png")
    tlo_menu = pygame.image.load("zdjecia\menu.png")
    run=True
    play_button=Button(100, 200,"zdjecia\przycisk.png", "zdjecia\przycisk_hovered.png")
    tworcy_butoon=Button(100, 420, "zdjecia\zdjtworcy.png", "zdjecia\zdjtworcy1.png")

    iloscTali=1
    window.blit(tlo_menu, (0, 0))
    plik1 = open("zapisyWPR.txt", "w")
    while run:
        reser_button = Button(100, 300, "zdjecia\wreser.png", "zdjecia\wreset1.png")
        clock += pygame.time.Clock().tick(60) / 1000  # maksymalnie 60 fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                plik1.close()
                run = False
                    
        wygranapunkyM = pygame.font.Font.render(pygame.font.SysFont("arial", 50), str(wygrana) + ("-wygranych"), True,
                                                (0, 0, 0))
        przegranPunktyM = pygame.font.Font.render(pygame.font.SysFont("arial", 50), str(przegrana) + ("-przegranych"),
                                                  True, (0, 0, 0))
        remisPunktyM = pygame.font.Font.render(pygame.font.SysFont("arial", 50), str(remis) + ("-remis"), True,
                                               (0, 0, 0))
        if play_button.tick():
           y=level_one(iloscTali)
           if y==5:
               wygrana+=1
           if y==7:
               przegrana+=1
           if y==1:
               remis+=1
           if plik1.writable():
                 if reser_button.tick():
            wygrana=0
            przegrana=0
            remis=0

        window.blit(tlo_menu, (0, 0))
        window.blit(przegranPunktyM, (450, 210))
        window.blit(wygranapunkyM, (450, 280))
        window.blit(remisPunktyM, (450, 350))
        tworcy_butoon.draw(window)
        reser_button.draw(window)
        play_button.draw(window)
        pygame.display.update()

if __name__=="__main__":

    main()
       
