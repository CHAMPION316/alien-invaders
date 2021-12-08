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

#.............................The user's character image (player)
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

#Laser images
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

#...................................Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

#....................................Class player's character and it's attributes
class Ship: 
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.player_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0
        
    #............................Function that draws size of player on the window (temporary design *rectangle*)
    def draw(self, window):
        #pygame.draw.rect(window, (255, 255, 51), (self.x, self.y, 30, 30))
        window.blit(self.ship_img, (self.x, self.y,))
        
    def get_width(self):
        return self.ship_img.get_width()
    
    def get_height(self):
        return self.ship_img.get_height()
        
#.........................................Takes inheritance from class Ship for use in player
class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

#........................................Enemy ship class and their colors         
class BadShips(Ship):
    EMEMY_COLORS = {
                   "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
                   "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                   "red": (RED_SPACE_SHIP, RED_LASER)
                    } #.......................................Dictionary for colors of enemy ships 
     
    def __init__(self, x, y, color, health = 100):
        super().__init__(x, y, health)  
        self.ship_img, self.laser_img = self.EMENY_COLORS[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
     
    #..................................................................Enemy movement     
    def movement(self, velocity):
        self.y += vel
       
#............................Function that runs game while window remains open
#............................Fucntion that determines player lives and levels

def main():
    run = True
    FPS = 60
    level = 1
    lives = 6
    main_font = pygame.font.SysFont("cambriamath", 60)
    
    player_speed = 7
    
#.............................calling the class player, inputs for players location on the window    
    player = Player(350, 620)
    
    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        #Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (128, 255, 0))
        level_label = main_font.render(f"Level: {level}", 1, (128, 255, 0))
        
        WIN.blit(lives_label, (20, 20))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 20, 20))
        
#...........................Draw window for the appearance of the player     
        player.draw(WIN)
        
        pygame.display.update()
    
    while run:
        clock.tick(FPS)
        redraw_window()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        #..................................Key input for user movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_speed > -10: #.........................Left
            player.x -= player_speed
        if keys[pygame.K_d] and player.x + player_speed + player.get_width() -10 < WIDTH: #.........................Right
            player.x += player_speed
        if keys[pygame.K_s] and player.y + player_speed + player.get_height() < HEIGHT: #.........................Down
            player.y += player_speed
        if keys[pygame.K_w] and player.y - player_speed > 0: #.........................Up
            player.y -= player_speed             
main()