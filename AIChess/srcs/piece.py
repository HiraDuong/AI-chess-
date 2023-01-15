# Mỗi quân cờ  ( object ) sẽ có các thuộc tính (elements) là tên , giá trị (điểm trên bàn cờ), cách di chuyển  
# - 1 = white, 1 = black


import os

class Piece:
    def __init__(self,name,color,value,texture=None,texture_rect= None):
        self.name = name
        self.color = color 
        value_sign = 1 if color == 'white' else -1
        self.value = value
        self.moves = []
        self.move_arr=[]
        self.moved = False # check đã di chuyển hay chưa (check the piece moved or not)
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    # Lấy ảnh quân cờ ra

    def set_texture(self,size = 80):
        self.texture = os.path.join(
            f'D:/NEWCODE/Game learning/AIChess/assets/images/imgs-{size}px/{self.color}_{self.name}.png') 
    # Di chuyển

    def add_moves(self,move):
        self.moves.append(move)
    
    def clear_move_arr(self):
        self.move_arr=[]

    def add_move_arr(self,move_arr):
        self.move_arr.append(move_arr)

    def clear_move(self):
        self.moves = []   
# Quân tốt 
class Pawn(Piece):

    def __init__(self,color) :
        self.dir = -1 if color == 'white' else 1
        super().__init__('pawn',color,1.0)
# Quân mã
class Knight(Piece):

    def __init__(self,color) :
        super().__init__('knight',color,3.0)
# Quân tượng
class Bishop(Piece):

    def __init__(self,color) :
        super().__init__('bishop',color,3.01)
# Quân xe
class Rook(Piece):

    def __init__(self,color) :
        super().__init__('rook',color,5.0)
        
# Quân hậu
class Queen(Piece):

    def __init__(self,color) :
        super().__init__('queen',color,9.0)
#Quân vua
class King(Piece):

    def __init__(self,color) :
        # Vua quan trọng nhất nên phải cho nó cực hạn 
        super().__init__('king',color,10000.0)