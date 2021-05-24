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
    def Winner(self):
        def on_closing(self):
            self.winWinner.destroy()

        self.winWinner = tk.Toplevel(root) 
        self.winWinner.protocol("WM_DELETE_WINDOW", on_closing)
        self.winWinner.title('You Win')
        self.winWinner.geometry('400x400+600+300')
        
        self.Mycanvas = tk.Canvas(winWinner,width=400,height=400)
        self.Mycanvas.pack()

        self.canvas_id = Mycanvas.create_text(180, 20, anchor="nw") 
        self.Mycanvas.itemconfig(canvas_id, text="You Win!") 

        self.pilImage = Image.open("unnamed1.jpeg")
        self.image = ImageTk.PhotoImage(pilImage)
        self.imagesprite = Mycanvas.create_image(200,200,image=image)
        self.winWinner.mainloop()
    
    # draw red tile
    def draw(self):

        self.redTile = canvas.create_rectangle(self.RedTileCoordX, self.RedTileCoordY,
                                self.RedTileCoordX + squareSize * 2,
                                self.RedTileCoordY + squareSize,
                                fill="#D42421",
                                outline="#8b5546")
        return self.redTile

    # redtile coordinates
    def description(self):
        print("X redtile =", self.RedTileCoordX, " Y redtile =", self.RedTileCoordY)


# register block selection for next moving
def click(event):
    global redTileStatus, tile
    redTileStatus = "UNSELECT" # "SELECT"

    xCursor, yCursor = event.x, event.y

    xCursor = xCursor // squareSize
    yCursor = yCursor // squareSize

    print(xCursor, yCursor, "xCursor and yCursor")
    print(redTileX, redTileY, " x and y for RedTile")
    for i in range(TilesAmount):
        print(TileCoordX[i], TileCoordY[i], "x" + str(i) + " and y" + str(i) + " for tile")

    if (xCursor == redTileX or xCursor - 1 == redTileX) and yCursor == redTileY:
        redTileStatus = "SELECT"
        # print(redTileStatus, " for RedTile")
        for i in range(TilesAmount):
            tileInfo[i].TileStatus = "UNSELECT"
    else:
        redTileStatus = "UNSELECT"
        # print(redTileStatus, " for RedTile")

    for i in range(TilesAmount):
        tileInfo[i].TileStatus = "UNSELECT"
        if xCursor == TileCoordX[i] and yCursor == TileCoordY[i]:
            redTileStatus = "UNSELECT"
            tileInfo[i].TileStatus = "SELECT"
            # print(tileInfo[i].TileStatus, " for tile")
            # print(TileCoordX[i], TileCoordY[i], "VERY IMPORTANT")
    # for i in range (TilesAmount):
    #     print(tileInfo[i].TileStatus," for list of tiles")
        
    

# draw game board
def draw_board():
    global emptySquares
    emptySquares = [0] * boardSize
    for i in range(boardSize):
        emptySquares[i] = [0] * boardSize
    canvas.delete("all")
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
    redTile = REDTILE(0, 200)
    tile = [0] * TilesAmount
    redTile.draw()
    redTile.description()
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
        print(tile[i], " Вот индекс сраной плитки")





# moving tiles when 1 of them selected
# def move_tile(event):
#     global redTileX, redTileStatus
#     if redTileStatus == "SELECT":
#         if event.keysym == 'Right' and (not redTileX == 4):
#             for i in range(TilesAmount):
#                 if (redTileX == TileCoordX[i] or redTileX + 1 == TileCoordX[i]) and redTileY == TileCoordY[i]:
#                     canvas.move(redTile, -(squareSize * 2), 0)
#                     redTileX -= 2
#                     print(TileCoordX[i], redTileX, "дада")
#                     break
#                 else:
#                     print(TileCoordX[i], redTileX, "еще немного важной инфы")
#                     canvas.move(redTile, squareSize, 0)
#                     redTileX = redTileX + 1
#                     # print(redTileX, "position x + 1")
#                     canvas.update()
#                     if redTileX == 4:
#                         Winner()
#         if event.keysym == 'Left' and (not redTileX == 0):
#             canvas.move(redTile, -squareSize, 0)
#             redTileX = redTileX - 1
#             # print(redTileX, "position x - 1")
#             canvas.update()
#     for i in range (TilesAmount):
#         if tileInfo[i].TileStatus == "SELECT":
#             if event.keysym == 'Right':
#                 canvas.move(tile[i], squareSize, 0)
#                 TileCoordX[i] += 1
#             if event.keysym == 'Left':
#                 canvas.move(tile[i], -squareSize, 0)
#                 TileCoordX[i] -= 1


# Game settings
root = tk.Tk() # main window
root.title("Slide Blocks") # window name
boardSize = 6
squareSize = 100
squares = boardSize ** 2

canvas = tk.Canvas(root, width=boardSize * squareSize, height=boardSize * squareSize, bg = "#808080")
canvas.focus_set()
canvas.pack()
# canvas.bind('<Button-1>', click)
# canvas.bind('<Right>', move_tile)
# canvas.bind('<Left>', move_tile)
# canvas.bind('<Up>', Print)

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