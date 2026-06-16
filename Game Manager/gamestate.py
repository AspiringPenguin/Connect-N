import typing

class Board:
    def __init__(self, height : int=6, width : int=7, aim : int=4):
        #Store setup
        self.height = height
        self.width = width
        self.aim = aim

        #Setup board array
        board = list[list[int]]() #0 = empty. 1=red, -1=yellow
        for y in range(height):
            board.append(list[int]())
            for x in range(width):
                board[y].append(0)

        #Helper variables
        self.full = [False] * width
        self.height = [0] * width

        #Game state
        self.toMove = 1 # Red

    def makeMove(self, move : typing.Any):
        pass

    def undoMove(self):
        pass

    def getMoves(self):
        pass