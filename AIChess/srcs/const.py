import pygame
#GAME BOARD
WIDTH,HEIGHT = 800,600
COLS = 8
ROWS = 8
QSIZE = HEIGHT/8


# RGB COLOR
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
LIGHTGREEN = (234,235,200)
DARKGREEN = (119,154,88)
LIGHTBLUE = (204,255,255)

#font 

class Const:
    def __init__(self) :
        pass
    
    def font(sefl,font,size):
        return pygame.font.SysFont(font,size)

