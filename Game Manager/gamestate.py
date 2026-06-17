ray = list[tuple[int, int]]

def getAsChar(i : int) -> str:
    if i == 0:
        return "."
    elif i == 1:
        return "x"
    return "o"

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

        self.rays = self.generateRays()

        #Game state
        self.toMove = 1 # Red

    def generateRays(self) -> list[ray]:
        rays = list[ray]()

        rayLen = self.aim - 1

        for direction in [(1, 0), (1, 1), (0, 1), (-1, 1)]:
            for y in range(self.height):
                for x in range(self.width):
                    if 0 <= (y + direction[1]*rayLen) < self.height:
                        if 0 <= (x + direction[0]*rayLen) < self.width:
                            thisRay = ray()
                            for i in range(0, self.aim):
                                thisRay.append((x + direction[0]*i, y + direction[1]*i))
                            rays.append(thisRay)

        return rays


    def makeMove(self, move : int): #Integer of the column to play in
        #Apply the move
        self.board[self.heights[move]][move] = self.toMove
        self.heights[move] += 1
        if self.heights[move] == self.height:
            self.full[move] = True

        #Get ready for the next move
        self.toMove *= -1

    def undoMove(self, move : int):
        #Undo preparations for the next move
        self.toMove *= -1
        
        #Undo the last move
        self.full[move] = False
        self.heights[move] -= 1
        self.board[self.heights[move]][move] = 0

    def getMoves(self) -> list[int]:
        return [column for column in range(self.width) if not self.full[column]]

    def moveIsLegal(self, move: int) -> bool:
        return not self.full[move]

    def isWon(self) -> int: #0 for no, 1 for red, -1 for yellow
        for ray in self.rays:
            broken = False
            piece = self.board[ray[0][1]][ray[0][0]]
            if piece == 0:
                continue
            for (x2, y2) in ray[1:]:
                if self.board[y2][x2] != piece:
                    broken = True
                    break
            if not broken:
                return piece
        
        return 0

    def isDraw(self) -> bool: #Given that no-one has won, check for a draw
        return all(self.full)

    def __str__(self) -> str:
        rows = map(lambda x: "".join(map(getAsChar, x)), self.board[::-1])
        return "\n".join(rows)