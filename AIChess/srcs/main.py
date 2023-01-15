
import sys

import pygame

from const import *
from dragger import *
from game import *
from move import *
from square import *


class Main:
 
    def __init__(self) :
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("AI chess")
        self.game = Game()
        #self.history = Move(intinal,final)
        self.all_history = []
        self.RAM_history = []
        #Lượt 
        self.turn = False
        self.menu = Menu()

    def mainloop(self):
        click = False
        screen = self.screen
        game = self.game
        dragger = self.game.dragger
        board = self.game.board
        menu = self.menu
        turn = self.turn
        #all_history = self.all_history
        while True:
            #show methods
            game.show_bg(screen)
            game.show_move(screen)
            game.show_piece(screen)
            game.show_menu(screen,LIGHTBLUE)
            if dragger.dragging:
                dragger.update_blit(screen,piece)
            # get event 
            for event in pygame.event.get():
               
                #click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    clicked_row = int (dragger.mouseY // QSIZE)
                    clicked_col = int (dragger.mouseX // QSIZE)
                    if click == False :
                        #dragger.update_mouse(event.pos)
                        #print(event.pos)
                        # Chuyển tọa độ click -> tọa độ hàng và cột 
                        
                        #print(clicked_row,clicked_col) 
                        #nếu có quân cờ trong ô
                        if 600<=dragger.mouseX<=800 and 0<=dragger.mouseY<=600:
                            print("menu")
                            menu.menu_click(dragger.mouseX,dragger.mouseY,screen)
                        elif board.square[clicked_row][clicked_col].has_piece():
                            #print(dragger.mouseY,clicked_row)
                            #print(dragger.mouseX,clicked_col)
                            piece = board.square[clicked_row][clicked_col].piece
                            board.calc_move(piece,clicked_row,clicked_col)
                            #board.print_move_console(screen,piece)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            #show method
                            game.show_bg(screen)
                            game.show_move(screen)
                            game.show_piece(screen)
                            start_row=clicked_row
                            start_col=clicked_col
                            click = True
                        else:
                            pass
                    else:
                        if dragger.dragging:
                            #dragger.update_mouse(event.pos)
                            #print(event.pos)
                #show methods

                            '''game.show_bg(screen)
                            game.show_move(screen)
                            game.show_piece(screen)
                            dragger.update_blit(screen)'''
                            
                            if piece.color == 'white':
                                turn = True
                            else:
                                turn = False

                            release_row = int(dragger.mouseY // QSIZE)
                            release_col =int (dragger.mouseX // QSIZE)

                            #create posible move
                            initial = Square(dragger.initial_row,dragger.initial_col)
                            final = Square(release_row,release_col)
                            move = Move(initial,final)
                            
                            #Move(initial,final).add_history(piece,initial,final)
                            #Move(initial,final).show_history()
                        #HISTORY OF THE GAME
                            if (start_row,start_col) != (release_row,release_col):
                                self.RAM_history.append((piece.color+" "+piece.name,(start_row,start_col),(release_row,release_col)))
                                self.all_history.append((piece.color+" "+piece.name,(start_row,start_col),(release_row,release_col)))

                                print(self.RAM_history)
                            self.RAM_history = []
                            print (turn)

                            if board.valid_move(dragger.piece,move):
                                board.move(dragger.piece,move)
                                game.show_bg(screen)
                                game.show_piece(screen)
                            dragger.undrag_piece(piece)
                            
                            click = False
                    
                            
                        

                #mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        #print(event.pos)
                    #show methods
                        game.show_bg(screen)
                        game.show_move(screen)
                        game.show_piece(screen)
                        dragger.update_blit(screen,piece)
                        

    
                


                #click release
                '''elif event.type == pygame.MOUSEBUTTONUP:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        release_row = int(dragger.mouseY // QSIZE)
                        release_col =int (dragger.mouseX // QSIZE)

                        #create posible move
                        intinal = Square(dragger.initial_row,dragger.initial_col)
                        final = Square(release_row,release_col)
                        move = Move(intinal,final)
                        if board.valid_move(dragger.piece,move):
                            board.move(dragger.piece,move)
                            game.show_bg(screen)
                            game.show_piece(screen)
                    '''
                    
                    #dragger.undrag_piece(piece)



                 #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

main = Main()
main.mainloop()

