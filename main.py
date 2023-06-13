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
        if(len(tablicaObiektow)<2):
            losujkartePrzycisk = Button(600, 200, "D:\karty\przyciskLOS.png", "D:\karty\przyciskLOS1.png")

            losujkartePrzycisk.draw(window)

        if (punktyGracza < 21 and len(tablicaObiektow) > 4):
            cofanie_button.draw(window)
            if (cofanie_button.tick()):
                cofanie_button.draw(window)
                if cofanie_button.tick():
                    iloscpostaci-=1
                    kartygracza -= 1
                    ostatniaKarta = tablicaObiektow.pop()
                    punktyGracza -= int(ostatniaKarta.figura)
        if losujkartePrzycisk.tick() and len(tablicaObiektow)<2:

            if current_time - last_created_time > 1.0:  # utwórz nowy obiekt co 1 sekundę
                x=talia.losuj_karte()

                karta1 = Karta(x[0], x[1], iloscpostaci*110+300, 400) #tworzy dwie pierwsze nasze karty
                tablicaObiektow.append(karta1)
                last_created_time = current_time
                iloscpostaci += 1
                print(x[1])
                if (int(x[1]) == 14):
                    punktyZAsemGracza += 10
                    punktyGracza+=1
                else:
                    punktyZAsemGracza += get_wartosc(int(x[1]))
                    punktyGracza+=get_wartosc(int(x[1]))
                print("Z asem ", punktyZAsemGracza)
                print(" Bez asa ", punktyGracza)
          if(len(tablicaObiektow)==2): #1 karta brukiera
            if current_time - last_created_time > 1.0:
                p=talia.losuj_karte()
                if (int(p[1]) == 14):
                    punktyZAsemBrukiera += 10
                    punktyBrukiera+=1
                else:
                    punktyZAsemBrukiera += get_wartosc(int(p[1]))
                    punktyBrukiera+=get_wartosc(int(p[1]))
                print("Z asem ", punktyZAsemBrukiera)
                print(" Bez asa ", punkty)


                karta1 = Karta(p[0], p[1], 300, 50)
                tablicaObiektow.append(karta1)
                tablicaObiektowBrukier.append(karta1)
                last_created_time = current_time


        if(len(tablicaObiektow)==3):

            #window.blit(rewerse, (0, 0))
            g=["wrew", ""]
            karta1=Karta(g[0], g[1], 410, 50)
            tablicaObiektow.append(karta1)

        if (punktyGracza > 21):
            for karta in tablicaObiektow:
                karta.draw(window)
                pygame.display.update()
            przegrales()
            if x == 7:
                run = False
            return 7

        if(punkty<21 and len(tablicaObiektow)>=4 and len(tablicaObiektow)<6 and przyciskDoboruBool==True):

            #x=losuj_karte_pocztek(karty2, kolory2)
            przyciskDobierania=Button(600, 200, "D:\karty\dobierz.png", "D:\karty\dobierz1.png")
            przyciskDobierania.draw(window)
            if(przyciskDobierania.tick()):
                if current_time - last_created_time > 1.0:  # utwórz nowy obiekt co 1 sekundę


                    iloscpostaci+=1
                    print(iloscpostaci)
                    h=talia.losuj_karte()
                    karta5 = Karta(h[0], h[1], iloscpostaci*110+200, 400)
                    tablicaObiektow.append(karta5)
                    if (int(h[1]) == 14):
                        punktyZAsemGracza += 10
                        punktyGracza += 1
                    else:
                        punktyZAsemGracza += get_wartosc(int(h[1]))
                        punktyGracza += get_wartosc(int(h[1]))
                    print("Z asem ", punktyZAsemGracza)
                    print(" Bez asa ", punktyGracza)
                    pygame.display.update()
                    last_created_time = current_time


                if(punktyGracza>21):
                    for karta in tablicaObiektow:
                        karta.draw(window)
                        pygame.display.update()

                    x = przegrales(punktyGracza, punktyBrukiera)
                    if x == 7:
                        run = False
                    return 7
if( PrzyciskPasu==True and len(tablicaObiektow)>=4):

            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

            #przycisk passu tworzenie
            przyciskPassu=Button(30,200, "D:\karty\pass.png", "D:\karty\pass1.png")
            przyciskPassu.draw(window)

            if(przyciskPassu.tick()):
                przyciskDoboruBool=False
                PrzyciskPasu=False
                #brukier tworzy 2 swoja karte
                a = talia.losuj_karte()
                if (int(a[1]) == 14):
                    punktyZAsemBrukiera+= 10
                    punktyBrukiera += 1
                else:
                    punktyZAsemBrukiera += get_wartosc(int(a[1]))
                    punktyBrukiera += get_wartosc(int(a[1]))
                print("BBBB Z asem ", punktyZAsemBrukiera)
                print("BBB Bez asa ", punktyBrukiera)
                karta1 = Karta(a[0], a[1], 410, 50)
                tablicaObiektow.append(karta1)
                tablicaObiektowBrukier.append(karta1)
                if(punktyBrukiera>punktyGracza and punktyBrukiera<22):
                    if current_time - last_created_time > 1.0:
                        for karta in tablicaObiektow:
                            karta.draw(window)
                            pygame.display.update()

                        x = przegrales(punktyGracza, punktyBrukiera)
                        if x == 7:
                            run = False
                        return 7

                if(punktyBrukiera==punktyGracza):
                    for karta in tablicaObiektow:
                        karta.draw(window)
                        pygame.display.update()

                    x=remis()
                    if x==1:
                        run=False
                    return 1
                if (punktyBrukiera > 21):
                    for karta in tablicaObiektow:
                        karta.draw(window)
                        pygame.display.update()
                    ilosc_punktow_aktualna = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                     str(punktyGracza), True,
                                                                     (0, 0, 0))
                    ilosc_punktow_aktualna_brukiera = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                              str(punktyBrukiera), True, (0, 0, 0))
                    window.blit(ilosc_punktow_aktualna_brukiera, (0, 0))
                    window.blit(ilosc_punktow_aktualna, (0, 400))
                    x=wygrales()
                    if x==7:
                        run=False
                    return 7
                if(punktyBrukiera>punktyGracza and len(tablicaObiektow)>4 and punktyBrukiera<22):
                    if current_time - last_created_time > 1.0:
                        for karta in tablicaObiektow:
                            karta.draw(window)
                            pygame.display.update()

                        x = przegrales(punktyGracza, punktyBrukiera)
                        if x == 7:
                            run = False
                        return 7
                #brukier do tego momentu stworzyl 2 karte swoja
                if(punktyBrukiera==punktyGracza):
                    if current_time - last_created_time > 1.0:
                        for karta in tablicaObiektow:
                            karta.draw(window)
                            pygame.display.update()

                        x = remis()
                        if x == 1:
                            run = False
                        last_created_time = current_time
                        return 1
                if(punktyBrukiera>punktyGracza and punktyBrukiera<21 and punktyGracza<21):
                    if current_time - last_created_time > 1.0:
                        for karta in tablicaObiektow:
                            karta.draw(window)
                            pygame.display.update()
                        ilosc_punktow_aktualna = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                         str(punktyGracza), True,
                                                                         (0, 0, 0))
                        ilosc_punktow_aktualna_brukiera = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                                  str(punktyBrukiera), True, (0, 0, 0))
                        window.blit(ilosc_punktow_aktualna_brukiera, (0, 0))
                        window.blit(ilosc_punktow_aktualna, (0, 400))
                        x = przegrales(punktyGracza, punktyBrukiera)
                        if x == 7:
                            run = False
                        last_created_time = current_time
                        return 7
                for karta in tablicaObiektow:
                    karta.draw(window)
                    pygame.display.update()
                if (len(tablicaObiektowBrukier) > 1 and punktyBrukiera >= punktyGracza and punktyBrukiera < 22):
                    if current_time - last_created_time > 1.0:
                        for karta in tablicaObiektow:
                            karta.draw(window)
                            pygame.display.update()
                        ilosc_punktow_aktualna = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                         str(punktyGracza), True,
                                                                         (0, 0, 0))
                        ilosc_punktow_aktualna_brukiera = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                                  str(punktyBrukiera), True, (0, 0, 0))
                        window.blit(ilosc_punktow_aktualna_brukiera, (0, 0))
                        window.blit(ilosc_punktow_aktualna, (0, 400))
                        x = przegrales(punktyGracza, punktyBrukiera)
                        if x == 7:
                            run = False
                        return 7
                        last_created_time = current_time
                if(punktyBrukiera<=punktyGracza and len(tablicaObiektowBrukier)>1 and punktyBrukiera<21):
                    #brukier dobiera 3 karte
                    b = talia.losuj_karte()
                    if (int(b[1]) == 14):
                        punktyZAsemBrukiera += 10
                        punktyBrukiera += 1
                    else:
                        punktyZAsemBrukiera += get_wartosc(int(b[1]))
                        punktyBrukiera += get_wartosc(int(b[1]))
                    print("BBBB Z asem ", punktyZAsemBrukiera)
                    print("BBBB  Bez asa ", punktyBrukiera)
                    karta12 = Karta(b[0], b[1], 510, 50)
                    tablicaObiektow.append(karta12)
                    tablicaObiektowBrukier.append(karta12)
                    for karta in tablicaObiektow:
                        karta.draw(window)
                        pygame.display.update()
                    if (punktyBrukiera == punktyGracza):
                        if current_time - last_created_time > 1.0:
                            for karta in tablicaObiektow:
                                karta.draw(window)
                                pygame.display.update()

                            x = remis()
                            if x == 1:
                                run = False

                            return 1
                    if(punktyBrukiera>21):
                        ilosc_punktow_aktualna = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                         str(punktyGracza), True,
                                                                         (0, 0, 0))
                        ilosc_punktow_aktualna_brukiera = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                                  str(punktyBrukiera), True, (0, 0, 0))
                        window.blit(ilosc_punktow_aktualna_brukiera, (0, 0))
                        window.blit(ilosc_punktow_aktualna, (0, 400))
                        x = wygrales()
                        if x == 5:
                            run = False
                        return 5
                    if(punktyBrukiera>punktyGracza and punktyBrukiera<=21):

                        if current_time - last_created_time > 1.0:
                            for karta in tablicaObiektow:
                                karta.draw(window)
                                pygame.display.update()

                            x = przegrales(punktyGracza, punktyBrukiera)
                            if x == 7:
                                run = False
                            last_created_time = current_time
                            return 7
                    if(punktyBrukiera<21 and punktyGracza<21 and punktyBrukiera>punktyGracza):
                        for karta in tablicaObiektow:
                            karta.draw(window)
                            pygame.display.update()

                        x = przegrales(punktyGracza, punktyBrukiera)
                        if x == 7:
                            run = False
                        return 7
                    if(punktyBrukiera>21):
                        if current_time - last_created_time > 1.0:
                            for karta in tablicaObiektow:
                                karta.draw(window)
                                pygame.display.update()

                            x = wygrales()
                            if x == 5:
                                run = False
                            return 5
                     if(punktyBrukiera==punktyGracza):
                        for karta in tablicaObiektow:
                            karta.draw(window)
                            pygame.display.update()

                        x=remis()
                        if x==1:
                            run=False
                        return 1
                    if(punktyBrukiera<21 and punktyBrukiera>punktyGracza):
                        if current_time - last_created_time > 1.0:
                            for karta in tablicaObiektow:
                                karta.draw(window)
                                pygame.display.update()
                            ilosc_punktow_aktualna = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                             str(punktyGracza), True,
                                                                             (0, 0, 0))
                            ilosc_punktow_aktualna_brukiera = pygame.font.Font.render(pygame.font.SysFont("arial", 200),
                                                                                      str(punktyBrukiera), True,
                                                                                      (0, 0, 0))
                            window.blit(ilosc_punktow_aktualna_brukiera, (0, 0))
                            window.blit(ilosc_punktow_aktualna, (0, 400))
                            x = przegrales(punktyGracza, punktyBrukiera)
                            if x == 7:
                                run = False
                            last_created_time = current_time
                            return 7
                    
                    
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
               plik1.write(str(wygrana)+"\n")
               plik1.write(str(przegrana)+"\n")
               plik1.write(str(remis)+"\n")
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
       
