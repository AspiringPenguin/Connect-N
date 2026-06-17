#from time import perf_counter_ns
from math import floor
from tkinter import Event, Frame, StringVar, Tk, Canvas
from tkinter.ttk import Button, OptionMenu, Style

#import cProfile

from gamestate import Board

class MainWindow(Tk):
    def __init__(self, width:int=7, height:int=6, aim:int=4):
        #Set up window title and geometry
        super().__init__()
        self.title("Game Manager")
        self.geometry(f"{700}x{600}")

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
        self.cellSize = 0
        self.userCanMove = True
        self.setupEventBindings()

        #Other UI elements
        self.ttkStyle = Style()
        self.ttkStyle.configure("LargeText.TButton", font="TkDefaultFont 12")

        self.controlFrame = Frame(self)
        self.controlFrame.pack(anchor="s", fill="x")

        options = ["Human", "Bot 1", "Configure new..."]
        self.player1DropdownVal = StringVar(value="Human")
        self.player1Dropdown = OptionMenu(self.controlFrame, self.player1DropdownVal, "Human", *options)
        self.player1Dropdown.grid(column=1, row=2, padx=5, pady=5)

        self.goButton = Button(self.controlFrame, text="Go", style="LargeText.TButton")
        self.goButton.grid(column=3, row=1, padx=5, pady=5, rowspan=2)

        self.player2DropdownVal = StringVar(value="Human")
        self.player2Dropdown = OptionMenu(self.controlFrame, self.player1DropdownVal, "Human", *options)
        self.player2Dropdown.grid(column=5, row=2, padx=5, pady=5)

        self.controlFrame.columnconfigure(0, weight=2)
        self.controlFrame.columnconfigure(1, weight=1)
        self.controlFrame.columnconfigure(2, weight=2)
        self.controlFrame.columnconfigure(3, weight=1)
        self.controlFrame.columnconfigure(4, weight=2)
        self.controlFrame.columnconfigure(5, weight=1)
        self.controlFrame.columnconfigure(6, weight=2)

    def setupCanvas(self):
        self.slots = list[list[int]]()

        self.canvas = Canvas(self, background="blue")
        self.canvas.pack(expand=True, fill="both", anchor="n")
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
        height, width = self.canvas.winfo_height(), self.canvas.winfo_width()

        self.cellSize = min(height/self.boardHeight, width/self.boardWidth)

        for y in range(self.boardHeight):
            for x in range(self.boardWidth):
                self.canvas.coords(self.slots[y][x], floor(self.cellSize * (0.1 + x)), floor(self.cellSize * (0.1 + y)), floor(self.cellSize * (0.9 + x)), floor(self.cellSize * (0.9 + y)))


    def mouseMove(self, e : Event):
        self.mouseX = e.x
        self.mouseY = e.y
        self.updateBoard()

    def mouseLeave(self, e: Event):
        self.mouseX = -1
        self.mouseY = -1
        self.updateBoard()

    def mouseClick(self, e: Event):
        columnSelected = floor((e.x) / self.cellSize)
        if self.board.moveIsLegal(columnSelected) and self.userCanMove:
            self.board.makeMove(columnSelected)
        self.updateBoard()

    #Highlight a column if needed based on mouse pos and set colors based on gamestate
    def updateBoard(self):
        highlightColumn = self.mouseX // self.cellSize

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
    win = MainWindow(width=13, height=10, aim=8)

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