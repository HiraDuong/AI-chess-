
import pygame
from const import *
from board import *
from square import *
from piece import *

class Dragger:
    def __init__(self) :
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
        self.board = Board()
        self.const = Const()
    # Thay đổi vị trí quân cờ
    def update_blit(self,surface,piece):
        #texture
        #Arialfont = pygame.font.SysFont('arial',30)
        Arialfont_30 = self.const.font('arial',30)

        self.piece.set_texture(size = 128)
        texture = self.piece.texture
        #img
        img = pygame.image.load(texture)
        #rect
        img_center = (self.mouseX,self.mouseY)
        #img = pygame.image.load(piece.texture)
        self.texture_rect = img.get_rect(center = img_center)
        #blit
        surface.blit(img ,self.piece.texture_rect)
        #blit in menu
        surface.blit(img ,(636,36))
        name = Arialfont_30.render(piece.name,True,RED)
        name_rect = name.get_rect(center = (636,164))
        surface.blit(name ,(670,164))

        #board = self.board
        #board.print_move_console(surface,piece)
        #text = Arialfont.render("Text1",True,RED)
        #name_rect = name.get_rect(center = (636,164))
        #surface.blit(text ,(670,200))


    def update_mouse(self,pos) :
        self.mouseX,self.mouseY = pos #(xcor,ycor)
    
    def save_initial (self,pos):
        self.initial_row = pos[1] // QSIZE
        self.initial_col = pos[0] // QSIZE
    
    def drag_piece(self,piece):
        self.piece = piece
        self.dragging = True
    
    def undrag_piece(self,piece):
        self.piece = None
        self.dragging = False
