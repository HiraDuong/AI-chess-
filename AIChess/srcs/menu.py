from tkinter import *
from const import *
import pygame
from dragger import *
from countdown import *


class Menu:
    def __init__(self) :
        self.color = RED
        self.const = Const()
        self.countdown = Countdown()
       # self.menu_create(surface,color)
        '''self.back = os.path.join(
            f"D:/NEWCODE/Game learning/AIChess/assets/images/menu/back.png"
        )
        
        self.new_game = os.path.join(
            f"D:/NEWCODE/Game learning/AIChess/assets/images/menu/new.jpg"
        )'''
    

    def set_button(self,name):
        self.button = os.path.join(
            f"D:/NEWCODE/Game learning/AIChess/assets/images/menu/{name}.png"
        )
    
    #create menu
    def menu_create(self,surface,color):
        rect = ((8*QSIZE),0,(WIDTH-8*QSIZE),(HEIGHT))
        pygame.draw.rect(surface,color,rect)
        pygame.draw.line(surface,BLACK,(600,225),(800,225))
        pygame.draw.line(surface,BLACK,(600,450),(800,450))
        self.countdown.clock_create(surface)
        def option_create ():
            # nút back, back button (620,540,(40,40))
            self.set_button('back')
            back_img = pygame.image.load(self.button)
            back_img = pygame.transform.scale(back_img, (60,60))
            surface.blit(back_img,(620,540))
            # new game button
            self.set_button('new')
            newgame_img = pygame.image.load(self.button)
            newgame_img = pygame.transform.scale(newgame_img, (60,60))
            surface.blit(newgame_img,(620,470))

            # 1 player
            self.set_button('oneplayer')
            oneplayer = pygame.image.load(self.button)
            oneplayer = pygame.transform.scale(oneplayer, (60,60))
            surface.blit(oneplayer,(720,470))

            # 2 player
            self.set_button('twoplayers')
            twoplayer = pygame.image.load(self.button)
            twoplayer = pygame.transform.scale(twoplayer, (60,60))
            surface.blit(twoplayer,(720,540))
            
            # add time
            self.set_button('add')
            add = pygame.image.load(self.button)
            add = pygame.transform.scale(add, (40,40))
            surface.blit(add,(620,315))

            # sub time
            self.set_button('subtract')
            subtract = pygame.image.load(self.button)
            subtract = pygame.transform.scale(subtract, (40,40))
            surface.blit(subtract,(720,315))
        self.countdown.show_clock(surface)
        option_create()
    
    def menu_click(self,mouse_x,mouse_y,surface):
        countdown = self.countdown
        # add time
        if 620<=mouse_x <=660 and 315<=mouse_y<=355:
            countdown.add_time()
            print('+')
        # sub time
        if 720<=mouse_x <=760 and 315<=mouse_y<=355:
            countdown.sub_time()
            print('-')
        # newgame
        if 620 <= mouse_x <=680 and 470 <= mouse_y <= 530:
            #countdown.start = False if True else True
            countdown.start = True
            print('new game')
            #countdown.count_down(surface)
            
        

        # return
        if 620<=mouse_x <=680 and 540<=mouse_y<= 600:
            countdown.start = False
        
        # 1 player
        # 2 players

    

    

