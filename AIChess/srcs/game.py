

import sys
import pygame
from dragger import Dragger
from const import *
from board import *
from square import *
from menu import Menu
class Game:
    def __init__(self) :
        self.board = Board()
        self.dragger = Dragger()
        self.menu = Menu()
    #show method
    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if(row + col) % 2 == 0:
                    color =  LIGHTGREEN
                else:
                    color = DARKGREEN
                rect = (col*QSIZE,row*QSIZE,QSIZE,QSIZE)

                pygame.draw.rect(surface,color,rect)
        
    
    def show_piece(self,surface):
        for row in range(ROWS):
            for col in range(COLS):  
                #check
                if self.board.square[row][col].has_piece():
                    piece = self.board.square[row][col].piece


                    #all piece except dragged piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size = 80)
                        img = pygame.image.load(piece.texture)
                        img_center = col*QSIZE+QSIZE/2,row*QSIZE+QSIZE/2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img,piece.texture_rect)
        #rect = ((8*QSIZE),0,(WIDTH-8*QSIZE),(HEIGHT))
        #pygame.draw.rect(surface,GREEN,rect)

    def show_menu(self,surface,color):
        menu = self.menu
        menu.menu_create(surface,color)
        
    def show_move(self,surface):
        piece = self.dragger.piece
        is_printed = False
        i = 0
        if self.dragger.dragging:
            #lopp all valid moves
            for move in piece.moves:
                #color
                color = '#C86464' if (move.final.row+move.final.col) % 2 == 0 else '#C84646'
                #rect
                rect = (move.final.col * QSIZE,move.final.row*QSIZE,QSIZE,QSIZE)
                #blit
                pygame.draw.rect(surface,color,rect)
            
            
                
            