from tkinter import Event, Tk, Canvas

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

if __name__ == "__main__":
    main()