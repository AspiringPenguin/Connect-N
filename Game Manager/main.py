#from time import perf_counter_ns
from math import floor
from tkinter import Event, Tk, Canvas

#import cProfile

from gamestate import Board

class MainWindow(Tk):
    def __init__(self):
        #Set up window title and geometry
        super().__init__()
        self.title("Game Manager")
        self.minsize(700, 600)

        #Add canvas for graphics
        self.setupCanvas()

        #Set up event handling
        self.setupEventBindings()

    def setupCanvas(self):
        self.slots = list[list[int]]()

        self.canvas = Canvas(self, background="blue")
        self.canvas.pack(expand=True, fill="both")
        for y in range(6):
            self.slots.append([])
            for x in range(7):
                self.slots[y].append(self.canvas.create_oval((15 + x*100, 15 + y*100), (85 + x*100, 85 + y*100), fill="gray"))

    def setupEventBindings(self):
        self.canvas.bind("<Button-1>", self.mouseClick)
        self.canvas.bind("<Motion>", self.mouseMove)
        self.canvas.bind("<Leave>", self.clearHighlight)

    def mouseMove(self, e : Event):
        self.highlightColumn(e.x // 100)

    def clearHighlight(self, e:Event):
        self.highlightColumn(-1)

    def highlightColumn(self, column: int):
        for y in range(6):
            for x in range(7):
                if x == column:
                    pass
                else:
                    pass

    def mouseClick(self, e:Event):
        pass

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