# -*- coding: utf-8 -*-
"""
Created on Mon May  2 00:05:11 2022

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
DARK_GRAY = (80, 71, 78)
ORANGE = (233, 138, 30)
BROWN = (255, 210, 160)
DARK_BLUE = (0,0,153)
CYAN = (0, 204, 204)
LIGHT_GRAY = (224, 224, 224)

FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    AU = 149597870700  # astronomical unit in meters
    G = 6.67428e-11
    SCALE = 100 / AU # 1AU = 100 pixels
    TIMESTEP = 3600*24 # 1 day
    PROPORTION = 1.0001

    
    
    def __init__(self, x, y, radius, color, mass, name):
        self.x = x
        self.y = y
        self.radius = radius * self.PROPORTION
        self.color = color
        self.mass = mass
        
        self.keep_proportion = False
        
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
         
        self.x_vel = 0
        self.y_vel = 0
        self.max_length = False
        self.name = name
        
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        
        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                    
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x,y))
            
        
            pygame.draw.lines(win, self.color, False, updated_points)
            
            # Erasing the orbit lines after a certain length
            '''
            if len(self.orbit) > ((self.x**2)**0.5)*10*self.SCALE:
                 self.max_length = True
                
            if self.max_length == True:
                self.orbit.pop(0) # remove the line orbit as the moviment flows
            '''

        name_text = FONT.render(f"{self.name}", 1, WHITE)   
        win.blit(name_text, (x - name_text.get_width()/2, y - 35))

        pygame.draw.circle(win, self.color, (x,y), self.radius)
        
        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/10**9, 2)} * 10^6 km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))
        
        

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x**2 + distance_y**2)
        
        if other.sun:
            self.distance_to_sun = distance
        
        force  = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
            
        self.x_vel += total_fx / self.mass * self.TIMESTEP 
        self.y_vel += total_fy / self.mass * self.TIMESTEP 
        
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        
        self.orbit.append((self.x, self.y))
    
    


def main():
    scale = Planet.SCALE * Planet.AU
    run = True
    clock = pygame.time.Clock()
    
    # (x, y, radius, color, mass)
    
    sun = Planet(0, 0, 35, YELLOW, 1.98892 * 10**30, "Sun")
    sun.sun = True
    
    mercury = Planet(0.387 * Planet.AU, 0, 3, DARK_GRAY, 0.330 * 10**24, "Mercury")
    mercury.y_vel = -48.92 * 1000 # m/s
    
    venus = Planet(0.723 * Planet.AU, 0, 13, WHITE, 4868.5 * 10**21, "Venus")
    venus.y_vel = -35.02 * 1000 # m/s
    
    earth = Planet(-1 * Planet.AU, 0, 15, BLUE, 5973.6 * 10**21, "Earth")
    earth.y_vel = 29.783 * 1000 # m/s
    
    mars = Planet(-1.524 * Planet.AU, 0, 10, RED, 641.85 * 10**21, "Mars")
    mars.y_vel = 24.077 * 1000 # m/s
    
    jupiter  = Planet(-5.203 * Planet.AU, 0, 23, ORANGE, 1898.6 * 10**21, "Jupiter")
    jupiter.y_vel = 13.05 * 1000 # m/s
    
    saturn = Planet(-9.537 * Planet.AU, 0, 21, BROWN, 568460 * 10**21, "Saturn")
    saturn.y_vel = 9.64 * 1000 # m/s
    
    uranus = Planet(-19.23 * Planet.AU, 0, 17, CYAN, 86832 * 10**21, "Uranus")
    uranus.y_vel = 6.81 * 1000 # m/s
    
    neptune = Planet(-30.10 * Planet.AU, 0, 17, DARK_BLUE, 102430 * 10**21, "Neptune")
    neptune.y_vel = 5.43 * 1000 # m/s
    
    pluto = Planet(-39.3 * Planet.AU, 0, 3, LIGHT_GRAY, 13.105 * 10**21, "Pluto")
    pluto.y_vel = 4.72 * 1000 # m/s
    
    sedna = Planet( -960 * Planet.AU, 0, 1000, CYAN, 1 * 10**21, "Sedna")
    sedna.y_vel = 1.04 * 1000 # m/s
    
    
    planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto, sedna]
    
    # glTranslatef(0.0, 0.0, -5.0)
    moving = True
    while run:
        clock.tick(60)
        WIN.fill((0,0,0))
        print(moving)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: # wheel rolled up
                Planet.SCALE += Planet.SCALE/2 
                for planet in planets:
                    planet.radius+=planet.radius/2
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: # wheel rolled down
                Planet.SCALE -= Planet.SCALE/2 
                for planet in planets:
                    planet.radius-=planet.radius/2
                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                moving = False
                while not moving:
                    WIN.fill((0,0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            moving = True
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4: # wheel rolled up
                            Planet.SCALE += Planet.SCALE/2 
                            for planet in planets:
                                planet.radius+=planet.radius/2
                        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: # wheel rolled down
                            Planet.SCALE -= Planet.SCALE/2 
                            for planet in planets:
                                planet.radius-=planet.radius/2
                        
                    for planet in planets:
                        planet.draw(WIN)
                    pygame.display.update()
                            
                   
            elif event.type == pygame.MOUSEBUTTONUP:
                moving = False
                      
        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
    
        
        pygame.display.update()
    
    pygame.quit()
    

main()
