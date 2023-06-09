# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 20:55:16 2023

@author: clovi
"""


import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1080, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 71, 78)
ORANGE = (233, 138, 30)
BROWN = (255, 210, 160)
DARK_BLUE = (0,0,153)
CYAN = (0, 204, 204)
LIGHT_GRAY = (224, 224, 224)


FONT = pygame.font.SysFont("comicsans", 16)

x = WIDTH/2
y = HEIGHT/2

def createAstro(color, x, y, radius):
    astro = {"color": color, "x": x, "y": y, "radius": radius}
    return astro

sun = createAstro(YELLOW, WIDTH/2, HEIGHT/2, 100)
WIN.fill((0,0,0))
pygame.draw.circle(WIN, sun["color"], (sun["x"], sun["y"]), sun["radius"])


earth = createAstro(BLUE, x, y, 15)
pygame.draw.circle(WIN, earth["color"], (earth["x"], earth["y"]), earth["radius"])
 


pygame.display.flip()



# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()