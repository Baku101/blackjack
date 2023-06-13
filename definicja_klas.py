from main import*

pygame.init() # innicjowanie okna
window = pygame.display.set_mode((800, 600))
import pygame

import random
import time
current_time = time.time()
resolution = (800, 600)
last_created_time = time.time()

def get_wartosc(number):
    slownik = {
        1:1,
        2:2,
        3:3,
        4:4,
        5:5,
        6:6,
        7:7,
        8:8,
        9:9,
        10:10,
        11:10,
        12:10,
        13:10,
        14:1
    }
    if number in slownik:
        return slownik[number]
    else:
        print("cos cie swedzi")

def odswiez(punktyGracza, punktyBrukiera, window):
    ilosc_punktow_aktualna = pygame.font.Font.render(pygame.font.SysFont("arial", 200), str(punktyGracza), True,
                                                     (0, 0, 0))
    ilosc_punktow_aktualna_brukiera = pygame.font.Font.render(pygame.font.SysFont("arial", 200), str(punktyBrukiera),
                                                              True, (0, 0, 0))
    window.blit(ilosc_punktow_aktualna_brukiera, (0, 0))
    window.blit(ilosc_punktow_aktualna, (0, 400))
    
class Button:
    def __init__(self, x_cord, y_cord, zdj, zdj1):
       self.x_cord = x_cord
       self.y_cord = y_cord
       self.button_image = pygame.image.load(zdj)
       self.hovered_button_image = pygame.image.load(zdj1)
       self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_image.get_width(), self.button_image.get_height())
    
    def tick(self):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
    def draw(self, window):
        if self.hitbox.collidepoint(pygame.mouse.get_pos()):
            window.blit(self.hovered_button_image, (self.x_cord, self.y_cord))
        else:
            window.blit(self.button_image, (self.x_cord, self.y_cord))

class Talia:
    def __init__(self, ilosc_talii=1):
        self.ilosc_talii = ilosc_talii
        self.karty = []
        for _ in range(ilosc_talii):
            for kolor in ['k', 'p', 't', 'k']:
                for wartosc in range(2, 14):
                    print(wartosc)
                    self.karty.append((kolor, wartosc))
    def losuj_karte(self):
        karta = random.choice(self.karty)
        self.karty.remove(karta)
        return (karta[0], karta[1])            

class Karta:
    def __init__(self, kolor, figura, x=700, y=500):
        self.x_cord = x
        self.y_cord = y
        self.kolor = kolor
        self.figura = figura
        self.image = pygame.image.load(f"zdjecia\{figura}{kolor}.png")
    
    def draw(self, window):
        window.blit(self.image, (self.x_cord, self.y_cord))

def wygrales():

    time.sleep(2.5)
    wygrana=pygame.image.load("zdjecia\ptlowybranej.png")
    window.blit(wygrana, (-100, 0))
    koniec = pygame.font.Font.render(pygame.font.SysFont("arial", 170), "WYGRALES", True, (0, 0, 0))
    window.blit(koniec, (0, 400))
    pygame.display.update()
    time.sleep(5)

def remis():
    time.sleep(2.5)
    remis = pygame.image.load("zdjecia\wremis.jpg")
    window.blit(remis, (0, 0))
    koniec = pygame.font.Font.render(pygame.font.SysFont("arial", 170), "remis", True, (0, 0, 0))
    window.blit(koniec, (0, 0))
    pygame.display.update()
    time.sleep(5)

def przegrales(punktyGracza, punktyBrukiera):
    time.sleep(2)
    tlo_gra = pygame.image.load("zdjecia\Beznazwy.png")
    window.blit(tlo_gra, (0, 0))
    matrix = pygame.image.load("zdjecia\poop.png")
    window.blit(matrix, (-250, 0))
    if(punktyGracza>21):

        koniec = pygame.font.Font.render(pygame.font.SysFont("arial", 170), "przegrales", True,
                                     (0, 0, 0))

        koniecPunktyGracza = pygame.font.Font.render(pygame.font.SysFont("arial", 70), "twoje punkty: "+str(punktyGracza), True, (100, 0, 0))
        window.blit(koniecPunktyGracza, (300, 300))
    else:
        koniec = pygame.font.Font.render(pygame.font.SysFont("arial", 170), "przegrales", True,
                                         (0, 0, 0))

        koniecPunktyGracza = pygame.font.Font.render(pygame.font.SysFont("arial", 70),
                                                     "twoje punkty: " + str(punktyGracza), True, (100, 0, 0))
        window.blit(koniecPunktyGracza, (300, 300))
        koniecPunktyBrukiera=pygame.font.Font.render(pygame.font.SysFont("arial", 70), "punkty Brukiera: "+str(punktyBrukiera), True, (100, 0, 0))
        window.blit(koniecPunktyBrukiera, (300, 400))


    print("przegrales")
    window.blit(koniec, (0, 400))
    pygame.display.update()
    time.sleep(5)
def wkzdj(kolor, liczba):

    nazwa_pliku = f"zdjecia\{liczba}{kolor}.png"

    return nazwa_pliku
