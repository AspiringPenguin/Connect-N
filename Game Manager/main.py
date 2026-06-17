#from time import perf_counter_ns
from math import floor
from random import choice
from tkinter import Event, Tk, Canvas

#import cProfile

from gamestate import Board

class MainWindow(Tk):
    def __init__(self, width:int=7, height:int=6, aim:int=4):
        #Set up window title and geometry
        super().__init__()
        self.title("Game Manager")
        self.geometry(f"{width*100}x{height*100}")

        #Gamestate
        self.board = Board(width=width, height=height, aim=aim)
        self.boardWidth = width
        self.boardHeight = height
        self.aim = aim

        #Add canvas for graphics
        self.setupCanvas()

        #Set up event handling
        self.mouseX = -1
        self.mouseY = -1
        self.setupEventBindings()

    def setupCanvas(self):
        self.slots = list[list[int]]()

        self.canvas = Canvas(self, background="blue")
        self.canvas.pack(expand=True, fill="both")
        for y in range(self.boardHeight):
            self.slots.append([])
            for x in range(self.boardWidth):
                self.slots[y].append(self.canvas.create_oval((0, 0), (0, 0), fill="gray"))

    def setupEventBindings(self):
        self.canvas.bind("<Button-1>", self.mouseClick)
        self.canvas.bind("<Motion>", self.mouseMove)
        self.canvas.bind("<Leave>", self.mouseLeave)
        self.canvas.bind("<Configure>", self.configureBoardView)

    def configureBoardView(self, e : Event):
        height, width = self.winfo_height(), self.winfo_width()

        cellSize = min(height/self.boardHeight, width/self.boardWidth)

        for y in range(self.boardHeight):
            for x in range(self.boardWidth):
                self.canvas.coords(self.slots[y][x], floor(cellSize * (0.1 + x)), floor(cellSize * (0.1 + y)), floor(cellSize * (0.9 + x)), floor(cellSize * (0.9 + y)))

    def mouseMove(self, e : Event):
        self.mouseX = e.x
        self.mouseY = e.y
        self.updateBoard()

    def mouseLeave(self, e: Event):
        self.mouseX = -1
        self.mouseY = -1
        self.updateBoard()

    def mouseClick(self, e:Event):
        self.board.makeMove(choice(self.board.getMoves()))
        self.updateBoard()

    #Highlight a column if needed based on mouse pos and set colors based on gamestate
    def updateBoard(self):
        highlightColumn = self.mouseX // 100

        for y in range(self.boardHeight):
            for x in range(self.boardWidth):
                #Determine fill color
                color = "gray"
                status = self.board.board[(self.boardHeight-1) - y][x]
                if status == 1:
                    color = "red"
                elif status == -1:
                    color = "yellow"
                elif x == highlightColumn:
                    color = "white"

                self.canvas.itemconfigure(self.slots[y][x], fill=color)

def main():
    win = MainWindow()

    win.mainloop()

# def perft(board : Board, depth : int) -> int:
#     if depth == 0 or board.isWon() != 0 or board.isDraw():
#         return 1

#     total = 0
#     for move in board.getMoves():
#         board.makeMove(move)
#         total += perft(board, depth-1)
#         board.undoMove(move)
#     return total

if __name__ == "__main__":
    main()

    # board = Board(width=7, height=6, aim=4)
    
    # with cProfile.Profile() as pr:
    #     for i in range(9):
    #         start = perf_counter_ns()
    #         res = perft(board, i)
    #         end = perf_counter_ns()
    #         secs = (end - start)/1_000_000_000
    #         print(i, res, f"{secs}s {res/secs:.0f}nps")
    #     pr.print_stats(sort="tottime")