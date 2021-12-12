# 2D Shooter [Alien Invaders](https://github.com/CHAMPION316)

Taking inspiration from the classic 1978 [Space Invaders](https://en.wikipedia.org/wiki/Space_Invaders). This is a 2D shooter created in [python](https://www.python.org/) using [pygame](https://www.pygame.org/news). 

## Table of contents

- [Description](#description)
- [Gameplay](#gameplay)

## 1. Description

The game is a very standard old school style 2D [fixed shooter](https://en.wikipedia.org/wiki/Shoot_%27em_up#Fixed_shooters) game in which the player uses directional inputs in order to manuever the space ship. 

### 1.1 Objective

The objective is to make it through as many levels as possible without dying but successfully eliminating your enemies. This will be accomplished by firing a laser that you will have at your disposal.

### 1.2 [**Main Menu**](readme-files/main-menu.jpg)

Upon loading the game you will be presented with a very simplistic main menu. You will be instructed to [click](readme-files/start-game.jpg) the mouse button in order to begin playing.

### 1.3 User Goal

#### *STYLE*
The background is presented with the same image that you see in the main menu of the game which is the background of where the game takes place. I decided to 

## 2 Gameplay

Gameplay requires the use of the [**WASD**](readme-files/move-input.jpg) keys to move horizontally and vertically. Using the [**spacebar key**](readme-files/space-shoot.jpg) fires the player's laser.

In the top left and right corners of the screen the player will be presented with the lives and level numbers that corresponds to them.
- [Game-Bar](readme-files/game-bar.jpg)

### 2.1 Lives

[**Lives-Level**](readme-files/lives-level.jpg)

Player begins game with 5 lives but can _lose_ them if:

- _If the player allows the enemey to reach the bottom of the screen._

- _However the player begins with **5 lives** at the start of the game._

### 2.2 Health Bar

The player maintains a health bar of 100% that decreases by 10% by either: and losing all his health bar doesn't account for the lost of lives but instead losing the game entirely. 

1. _Suffer a laser hit from the enemy -10%_
2. _Collide with the enemy resulting in the enemies death and a -10% deduction to players health._

When the player loses all of his health he will lose the game even if he has a single life remaining.

- _Lives only count toward letting the enemy reach bottom screen not wiping out player's health bar._

### 2.3 Lasers

Lasers in this game have a [__cooldown__](readme-files/cooldown-shot.jpg) of 1 second before they can be fired again for both the player and the enemy.

- _Laser [**speed**](readme-files/laser-speed.jpg) is set to 5 for both player and enemy_

I required a lot of help and guidance for this project due to the fact that I had to take a leave of absense at a job in a cruise ship until just about two weeks ago. There is more I would of liked to have done with this project but unfortunately time was not on my side. I struggled remembering a lot of the information I had learned since there was no way for me to spend the necessary time learning the material. I had to fast track and use a lot of resources to gain some kind of grasp of what I was doing. 

- Background and ships are P**NG images designed by me using [Adobe Photoshop](https://www.adobe.com/products/photoshop.html)

    * [Laser_Image](readme-files/laser_green_0.jpg)
    * [Space_Ship](readme-files/space_ship_creation.jpg)
- (The other colors were only saved as **PNG** format since all I had to do was change the color in the **PSD** format which is what photoshop uses for images.)


