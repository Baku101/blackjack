from main import*
from level_one import *


pygame.init() # innicjowanie okna
window = pygame.display.set_mode((800, 600))
import pygame

import random
import time
current_time = time.time()
resolution = (800, 600)
last_created_time = time.time()

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
     self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.button_image.get_width(), self.button_image.get_he
