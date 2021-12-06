import pygame
import os
import time
import random
pygame.font.init()

#.............................Initialize a window or screen for display 
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")  

#..............................Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets","pixel_ship_blue_small.png"))

#.............................Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#Laser images
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#...................................Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Ship: 
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0
    
#............................Function that draws size of ship on the window    
    
    def draw(self, window):
        pygame.draw.rect(window, (255, 255, 51), (self.x, self.y, 30, 30))

#............................Function that runs game while window remains open
#............................Fucntion that determines player lives and levels

def main():
    run = True
    FPS = 60
    level = 1
    lives = 6
    main_font = pygame.font.SysFont("cambriamath", 60)
    
    player_speed = 7
    
#.............................calling the class ship, inputs for ships location on the window    
    ship = Ship(350, 700)
    
    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        #Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (128, 255, 0))
        level_label = main_font.render(f"Level: {level}", 1, (128, 255, 0))
        
        WIN.blit(lives_label, (20, 20))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 20, 20))
        
#...........................Draw window for the appearance of the ship     
        ship.draw(WIN)
        
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #..................................Key input for user movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: #.........................Left
            ship.x -= player_speed
        if keys[pygame.K_d]: #.........................Right
            ship.x += player_speed
        if keys[pygame.K_s]: #.........................Down
            ship.y += player_speed
        if keys[pygame.K_w]: #.........................Up
            ship.y -= player_speed             
main()