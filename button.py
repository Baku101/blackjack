import pygame_widgets
import pygame
import os
from pygame_widgets.slider import Slider
from pygame_widgets.button import Button

pygame.init()
#rozmiar okna
win = pygame.display.set_mode((300, 170))

# Ustawienie tytułu okna
pygame.display.set_caption("Blackjack")

#rozmiar przycisku i suwaka
slider = Slider(win, 75, 50, 150, 20, min=1, max=8, step=1)
output = Button(win, 110, 100, 80, 30,text="", fontSize=8,onClick=lambda: print(slider.getValue()))

#liczba talii
liczba_talii = slider.getValue()

#ustawienie zdjęcia jako tła
current_dir = os.path.dirname(__file__)
background_path = os.path.join(current_dir, "bg.jpg")
background_image = pygame.image.load(background_path)
background_image = pygame.transform.scale(background_image, (300, 170))

#wyswietlanie zdjecia jako tlo na ekranie
    win.blit(background_image, (0, 0))
