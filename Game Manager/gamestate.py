class Board:
    def __init__(self, height : int=6, width : int=7, aim : int=4):
        #Store setup
        self.height = height
        self.width = width
        self.aim = aim

        #Setup board array
        self.board = list[list[int]]() #0=empty,  1=red, -1=yellow
        for y in range(height):
            self.board.append(list[int]())
            for x in range(width):
                self.board[y].append(0)

        #Helper variables
        self.full = [False] * width
        self.heights = [0] * width

        #Game state
        self.toMove = 1 # Red

    def makeMove(self, move : int): #Integer of the column to play in
        self.board[self.heights[move]][move] = self.toMove
        self.heights[move] += 1
        if self.heights[move] == self.height:
            self.full[move] = True

        #Get ready for the next move
        self.toMove *= -1

    def undoMove(self, move : int):
        self.toMove *= -1
        
        self.board[self.heights[move]][move] = 0
        self.heights[move] -= 1
        self.full[move] = False

    def getMoves(self) -> list[int]:
        return [column for column in range(self.width) if not self.full[column]]

    def getMoves(self):
        pass