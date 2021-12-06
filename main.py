import pygame
import os
import time
import random
pygame.font.init()

#Initialize a window or screen for display 
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")  

#Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))

#Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#Laser images
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

#Function that runs game while window remains open
#Fucntion that determines player lives and levels

def main():
    run = True
    FPS = 60
    level = 1
    lives = 6
    main_font = pygame.font.SysFont("cambriamath", 60)
    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        #Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (128, 255, 0))
        level_label = main_font.render(f"Level: {level}", 1, (128, 255, 0))
        
        WIN.blit(lives_label, (20, 20))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 20, 20))
        
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
main()