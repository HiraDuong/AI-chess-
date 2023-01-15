from cmath import pi
from turtle import right
from move import Move
from square import Square
from const import *
from piece import *
import pygame
class Board:
    def __init__(self) :
        #self.square = []
        self.square = [[0,0,0,0,0,0,0,0] for col in range(COLS)] 
        self.last_move = None
        self._create()
        self._add_piece('black')
        self._add_piece('white')

    


    def move ( self,piece,move):
        initial = move.initial
        final = move.final

        #console move update
        self.square[int(initial.row)][int(initial.col)].piece = None
        self.square[int(final.row)][int(final.col)].piece = piece
        # moved
        piece.moved = True
        # clear valid move
        piece.clear_move()
        piece.clear_move_arr()
        #set last move
        self.last_move = move


    def valid_move(self,piece,move):
        return move in piece.moves

    def calc_move(self,piece,row,col):
        '''caculator posible move
            tính nước đi khả dĩ
        '''
        # Cách đi
        #Quân mã
        def Knight_moves():
            #8 posible moves
            
            posible_moves = [
                (row-2,col+1),
                (row+2,col+1),
                (row-2,col-1),
                (row+2,col-1),
                (row-1,col+2),
                (row-1,col-2),
                (row+1,col-2),
                (row+1,col+2),
            ]
            for posible_move in posible_moves:
                posible_move_row,posible_move_col = posible_move
                if Square.in_range(posible_move_row,posible_move_col):
                    if self.square[posible_move_row][posible_move_col].isempty_or_rival(piece.color):
                        #create new Square of new move
                        initial = Square(row,col)
                        final = Square(posible_move_row,posible_move_col)
                        #create new move
                        move = Move(initial,final)
                        #append new valid move
                        if (posible_move_row,posible_move_col)  not in piece.move_arr:  
                            piece.add_moves(move)
                            piece.add_move_arr((posible_move_row,posible_move_col))
                        
            
        # Quân xe       
        def Rook_moves():
            pass

        # Quân Tượng
        def Bishop_moves():
            pass

        #Quân Hậu
        def Queen_moves():
            pass

        # Quân Vua
        def King_moves():
            #8 posible
            
            posible_moves = [
                (row+1,col),
                (row-1,col),
                (row,col+1),
                (row,col-1),
                (row+1,col+1),
                (row+1,col-1),
                (row-1,col-1),
                (row-1,col+1),
                
            ]
            for posible_move in posible_moves:
                posible_move_row,posible_move_col = posible_move
                if Square.in_range(posible_move_row,posible_move_col):
                    if self.square[posible_move_row][posible_move_col].isempty_or_rival(piece.color):
                        #create new Square of new move
                        initial = Square(row,col)
                        final = Square(posible_move_row,posible_move_col)
                        #create new move
                        move = Move(initial,final)
                        
                        
                        #append new valid move
                        if (posible_move_row,posible_move_col) not in piece.move_arr:
                            piece.add_moves(move)
                            piece.add_move_arr((posible_move_row,posible_move_col))
                        #print(posible_move)
            #Nhập thành 
                    #Quân Tốt
        def Pawn_moves():
            
            #steps 
            steps = 1 if piece.moved else 2
            #vertical move : đi thẳng
            start = row+piece.dir
            end = row +(piece.dir*(steps+1))
            for posible_move_row in range(start,end,piece.dir):
                if Square.in_range(posible_move_row):
                    if self.square[posible_move_row][col].isempty():
                        #create inital and final move square
                        initial = Square(row,col)
                        final = Square(posible_move_row,col)
                        move = Move(initial,final)
                        if (posible_move_row,col) not in piece.move_arr:
                            piece.add_moves(move)
                            piece.add_move_arr((posible_move_row,col))
                    else :
                        break
                else :
                    break
            #dialogal move : ăn chéo
            posible_move_row = row + piece.dir
            posible_move_cols = [col-1,col+1]
            for posible_move_col in posible_move_cols:
                if Square.in_range(posible_move_row,posible_move_col):
                    if self.square[posible_move_row][posible_move_col].has_rival_piece(piece.color):
                        #create initial and final move
                        initial = Square(row,col)
                        final = Square(posible_move_row,posible_move_col)
                        # create new move
                        move = Move(initial,final)
                        
                        piece.add_moves(move)
                        piece.add_move_arr((posible_move_row,posible_move_col))

                    # Đi theo đường  
        def straight_line_moves (incrs):
             # Luu nuoc di kha di 
            for incr in incrs  :
                row_incr,col_incr = incr
                posible_move_row = row + row_incr
                posible_move_col = col + col_incr
                while True:
                    if Square.in_range(posible_move_row,posible_move_col) :
                        initial = Square(row,col)
                        final = Square(posible_move_row,posible_move_col)
                        move = Move(initial,final)

                        #empty square
                        if self.square[posible_move_row][posible_move_col].isempty():
                            #create new move
                            if (posible_move_row,posible_move_col) not in piece.move_arr:    
                                piece.add_moves(move)
                                piece.add_move_arr((posible_move_row,posible_move_col))
                        #has rival square
                        if self.square[posible_move_row][posible_move_col].has_rival_piece(piece.color):
                            #create new move
                            if (posible_move_row,posible_move_col) not in piece.move_arr:    
                                piece.add_moves(move)
                                piece.add_move_arr((posible_move_row,posible_move_col))
                            break
                        # Nếu gặp quân cùng màu thì ngắt đường vẽ 
                        if self.square[posible_move_row][posible_move_col].has_team_piece(piece.color):
                            #create new move
                            break
                        
                    else : 
                        break
                    
                    
                    posible_move_row,posible_move_col = posible_move_row+row_incr,posible_move_col+col_incr
            

                

    #check

        if isinstance(piece,Pawn):
            Pawn_moves()

        elif isinstance(piece,Knight):
            Knight_moves()

        elif isinstance(piece,Bishop):
            straight_line_moves([
                (-1,1), #up right
                (1,1), # down right
                (1,-1), # down left
                (-1,-1) # up left
            ])

        elif isinstance(piece,Rook):
            straight_line_moves([
                (1,0), # down
                (-1,0), # up
                (0,-1), # left
                (0,1) #right
            ])

        elif isinstance(piece,Queen):
            straight_line_moves([
                (1,0), # down
                (-1,0), # up
                (0,-1), # left
                (0,1), #right
                (-1,1), #up right
                (1,1), # down right
                (1,-1), # down left
                (-1,-1) # up left
            ])

        elif isinstance(piece,King):
            King_moves()



# CREATE BOARD AND PIECES

    def _create(self): 
        for row in range(ROWS):
            for col in range(COLS):   
                self.square[row][col] = Square(row,col)
    
    def _add_piece(self,color): 
            row_pawn,row_others = (6,7) if color == 'white' else (1,0)
            # because the rows and cols start from 0 (Vì các hàng và cột tính từ số 0)


            # khởi tạo hàng tốt
            for col in range (COLS):
                self.square[row_pawn][col] = Square(row_pawn,col,Pawn(color))

     

            # Create Knight khởi tạo quân mã
            self.square[row_others][1] = Square(row_others,1,Knight(color))
            self.square[row_others][6] = Square(row_others,6,Knight(color))

            # Create Bishop
            self.square[row_others][2] = Square(row_others,2,Bishop(color))
            self.square[row_others][5] = Square(row_others,5,Bishop(color))
            #self.square[3][4] = Square(3,4,Bishop(color))

            #Create Rook
            self.square[row_others][0] = Square(row_others,0,Rook(color))
            self.square[row_others][7] = Square(row_others,7,Rook(color))
            # Create Queen
            self.square[row_others][3] = Square(row_others,3,Queen(color))

            # Create King 
            self.square[row_others][4] = Square(row_others,4,King(color))

    def print_move_console(self,surface,piece):
        print(piece.name)
        print (piece.move_arr)   
        Arialfont = pygame.font.SysFont('arial',30)
        #text_menu1 =  Arialfont.render("text 1",True,BLUE)
        #pygame.blit(surface,"text_menu1",(700,700))
        
