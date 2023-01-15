class Move:
    # ô đầu và cuôi
    def __init__(self,initial,final) :
        self.initial = initial
        self.final = final
        self.history = []
    def __str__(self) :
        s = ''
        s+= f'({self.initial_col},{self.initial_row})'
        s+= f'->({self.initial_col},{self.initial_row})'
        return s
    def __eq__(self, other):
        return self.initial==other.initial and self.final ==other.final
    

