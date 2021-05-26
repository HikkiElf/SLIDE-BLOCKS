import tkinter as tk
from PIL import ImageTk, Image
import random


# class for tiles information
class Tile:

    def __init__(self):
        self.size = None
        self.direction = None
        self.TileCoordX = None
        self.TileCoordY = None
        self.TileIndexX = None
        self.TileIndexY = None
        self.TileStatus = "UNSELECT"
        self.tile = [0] * boardSize
    
    def set_coords(self, TileCoordX, TileCoordY):
        self.TileCoordX = TileCoordX
        self.TileCoordY = TileCoordY
    
    def get_index(self):
        self.TileIndexX = self.TileCoordX // squareSize
        self.TileIndexY = self.TileCoordY // squareSize
    
    def set_direction(self, direction):
        self.direction = direction
    
    def set_size(self, size):
        self.size = size

    def set_status(self, TileStatus):
        self.TileStatus = TileStatus

    def description(self):
        print("size =", self.size, " direction =", self.direction, " TileCoordX =", 
            self.TileCoordX, " TileCoordY =", self.TileCoordY, " TileStatus =", self.TileStatus)


class REDTILE:

    def __init__(self, RedTileCoordX, RedTileCoordY):
        self.RedTileCoordX = RedTileCoordX
        self.RedTileCoordY = RedTileCoordY
        self.RedTileIndexX = RedTileCoordX // squareSize
        self.RedTileIndexY = RedTileCoordY // squareSize
        self.RedTileStatus = "UNSELECT"

    def set_status(self, RedTileStatus):
        self.RedTileStatus = RedTileStatus

    # create window with image "you won"
    def winner(self):
        def on_closing():
            self.winWinner.destroy()

        self.winWinner = tk.Toplevel(root) 
        self.winWinner.protocol("WM_DELETE_WINDOW", on_closing)
        self.winWinner.title('You Win')
        self.winWinner.geometry('400x400+600+300')
        
        self.Mycanvas = tk.Canvas(self.winWinner,width=400,height=400)
        self.Mycanvas.pack()

        self.canvas_id = self.Mycanvas.create_text(180, 20, anchor="nw") 
        self.Mycanvas.itemconfig(self.canvas_id, text="You Win!") 

        self.pilImage = Image.open("unnamed1.jpeg")
        self.image = ImageTk.PhotoImage(self.pilImage)
        self.imagesprite = self.Mycanvas.create_image(200,200,image=self.image)
        self.winWinner.mainloop()
    
    # draw red tile
    def draw(self):
        redTileRect = canvas.create_rectangle(self.RedTileCoordX, self.RedTileCoordY,
                                self.RedTileCoordX + squareSize * 2,
                                self.RedTileCoordY + squareSize,
                                fill="#D42421",
                                outline="#8b5546")
        return redTileRect

    # redtile coordinates
    def description(self):
        print("X redtile =", self.RedTileCoordX, " Y redtile =", self.RedTileCoordY)


# register block selection for next moving
def click(event):

    xCursor, yCursor = event.x, event.y

    xCursor = xCursor // squareSize
    yCursor = yCursor // squareSize

    if (xCursor == RedTileInfo.RedTileIndexX or xCursor - 1 == RedTileInfo.RedTileIndexX) and yCursor == RedTileInfo.RedTileIndexY:
        RedTileInfo.set_status("SELECT")
        print(RedTileInfo.RedTileStatus, " for RedTile")
        for i in range(TilesAmount):
            tileInfo[i].set_status("UNSELECT")
    else:
        RedTileInfo.set_status("UNSELECT")
        print(RedTileInfo.RedTileStatus, " for RedTile")

    for i in range(TilesAmount):
        tileInfo[i].set_status("UNSELECT")
        if xCursor == tileInfo[i].TileIndexX and yCursor == tileInfo[i].TileIndexY:
            RedTileInfo.set_status("UNSELECT")
            tileInfo[i].set_status("SELECT")
            print(tileInfo[i].TileStatus, " for Tile " + str(i))
    for i in range(TilesAmount):
        print(tileInfo[i].TileStatus, " for Tile " + str(i))
        
    

# draw game board
def draw_board():
    global emptySquares, RedTileInfo, tile, redTileRect, tileInfo
    emptySquares = [0] * boardSize
    for i in range(boardSize):
        emptySquares[i] = [0] * boardSize
    for i in range(boardSize):
        for j in range(boardSize):
            if i == 2 and j == 5:
                emptySquares[i][j] = canvas.create_rectangle(j * squareSize, i * squareSize, # white cube
                                                j * squareSize + squareSize,
                                                i * squareSize + squareSize,
                                                fill="#ffffff",
                                                outline="#8b5546")

            else:
                emptySquares[i][j] = canvas.create_rectangle(j * squareSize, i * squareSize, # area blocks
                                        j * squareSize + squareSize,
                                        i * squareSize + squareSize,
                                        fill="#55342b",
                                        outline="#8b5546")
    RedTileInfo = REDTILE(0, 200)
    tile = [0] * TilesAmount
    redTileRect = RedTileInfo.draw()
    RedTileInfo.description()
    print(RedTileInfo.RedTileIndexX, RedTileInfo.RedTileIndexY, " Индексы красного блока")
    for i in range(TilesAmount):
        tileInfo[i] = Tile()
        tileInfo[i].set_coords(i * squareSize, i * squareSize)
        tileInfo[i].description()
        tileInfo[i].get_index()
        print(tileInfo[i].TileIndexX, " ну вот же x индексы")
        print(tileInfo[i].TileIndexY, " а вот эти y индексы")
        tile[i] = canvas.create_rectangle(tileInfo[i].TileIndexX * squareSize, tileInfo[i].TileIndexY * squareSize,
                                            tileInfo[i].TileIndexX * squareSize + squareSize,
                                            tileInfo[i].TileIndexY * squareSize + squareSize,
                                            fill="#FFFF99",
                                            outline="#8b5546")





# moving tiles when 1 of them selected
def move_tile(event):
    if RedTileInfo.RedTileStatus == "SELECT":

        if event.keysym == 'Right' and (not RedTileInfo.RedTileIndexX == 4):
            for i in range(TilesAmount):
                if RedTileInfo.RedTileIndexY == tileInfo[i].TileIndexY:
                    if not (RedTileInfo.RedTileIndexX == tileInfo[i].TileIndexX or RedTileInfo.RedTileIndexX + 2 == tileInfo[i].TileIndexX):
                        canvas.move(redTileRect, squareSize, 0)
                        RedTileInfo.RedTileIndexX = RedTileInfo.RedTileIndexX + 1
                        if RedTileInfo.RedTileIndexX == 400:
                            RedTileInfo.winner()
                    else:
                        break
                # if not RedTileInfo.RedTileIndexY == tileInfo[i].TileIndexY:
                #     canvas.move(redTileRect, squareSize, 0)
                #     RedTileInfo.RedTileIndexX = RedTileInfo.RedTileIndexX + 1
                #     if RedTileInfo.RedTileIndexX == 400:
                #         RedTileInfo.winner()

        if event.keysym == 'Left' and (not RedTileInfo.RedTileIndexX == 0):
            for i in range(TilesAmount):
                if RedTileInfo.RedTileIndexY == tileInfo[i].TileIndexY:
                    if not (RedTileInfo.RedTileIndexX - 1 == tileInfo[i].TileIndexX):
                        canvas.move(redTileRect, -squareSize, 0)
                        RedTileInfo.RedTileIndexX = RedTileInfo.RedTileIndexX - 1
                    else:
                        break


    for i in range (TilesAmount):
        if tileInfo[i].TileStatus == "SELECT":

            if event.keysym == 'Right' and (not tileInfo[i].TileIndexX == 5):
                if not RedTileInfo.RedTileIndexY == tileInfo[i].TileIndexY:
                    canvas.move(tile[i], squareSize, 0)
                    tileInfo[i].TileIndexX += 1
                else:
                    if not (RedTileInfo.RedTileIndexX == tileInfo[i].TileIndexX or RedTileInfo.RedTileIndexX + 1 == tileInfo[i].TileIndexX):
                        canvas.move(tile[i], squareSize, 0)
                        tileInfo[i].TileIndexX += 1

            if event.keysym == 'Left' and (not tileInfo[i].TileIndexX == 0):
                if not RedTileInfo.RedTileIndexY == tileInfo[i].TileIndexY:
                    canvas.move(tile[i], -squareSize, 0)
                    tileInfo[i].TileIndexX -= 1
                else:
                    if not (RedTileInfo.RedTileIndexX + 2 == tileInfo[i].TileIndexX):
                        canvas.move(tile[i], -squareSize, 0)
                        tileInfo[i].TileIndexX -= 1

            if event.keysym == 'Up' and (not tileInfo[i].TileIndexY == 0):
                if not RedTileInfo.RedTileIndexX == tileInfo[i].TileIndexX:
                    canvas.move(tile[i], 0, -squareSize)
                    tileInfo[i].TileIndexY -= 1
                else:
                    if not (RedTileInfo.RedTileIndexY + 1 == tileInfo[i].TileIndexY):
                        canvas.move(tile[i], 0, -squareSize)
                        tileInfo[i].TileIndexY -= 1

            if event.keysym == 'Down' and (not tileInfo[i].TileIndexY == 5):
                if not RedTileInfo.RedTileIndexX == tileInfo[i].TileIndexX:
                    canvas.move(tile[i], 0, squareSize)
                    tileInfo[i].TileIndexY += 1
                else:
                    if not (RedTileInfo.RedTileIndexY - 1 == tileInfo[i].TileIndexY):
                        canvas.move(tile[i], 0, squareSize)
                        tileInfo[i].TileIndexY += 1
            


# Game settings
root = tk.Tk() # main window
root.title("Slide Blocks") # window name
boardSize = 6
squareSize = 100
squares = boardSize ** 2

canvas = tk.Canvas(root, width=boardSize * squareSize, height=boardSize * squareSize, bg = "#808080")
canvas.focus_set()
canvas.pack()
canvas.bind('<Button-1>', click)
canvas.bind('<Right>', move_tile)
canvas.bind('<Left>', move_tile)
canvas.bind('<Up>', move_tile)
canvas.bind('<Down>', move_tile)

board = list(range(1, squares + 1))
# print(board)

# Settings for module that i'm gonna create from menu on pygame
# size = [0] * 10
# TileCoordX = [0] * 10
# TileCoordY = [0] * 10
TilesAmount = 6
tileInfo = [0] * TilesAmount


for i in range (1):
    draw_board()
    # draw_tile()
    # red_tile()   
root.mainloop()