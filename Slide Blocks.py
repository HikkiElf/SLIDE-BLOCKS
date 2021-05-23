import tkinter as tk
from PIL import ImageTk, Image
import random


# class for tiles information
class Tile:

    def __init__(self, size, direction, TileCoordX, TileCoordY, TileStatus):
        self.size = size
        self.direction = direction
        self.TileCoordX = TileCoordX
        self.TileCoordY = TileCoordY
        self.TileStatus = TileStatus
        
    def description(self):
        print("size =", self.size, " direction =", self.direction, " TileCoordX =", 
            self.TileCoordX, " TileCoordY =", self.TileCoordY, " TileStatus =", self.TileStatus)


# draw red tile
def red_tile():
    global redTile
    for i in range(len(emptySquares)):
        for j in range(len(emptySquares[i])):
            if emptySquares[i][j] == 13:
                redTile = canvas.create_rectangle(j * squareSize, i * squareSize,
                                        j * squareSize + squareSize + 100,
                                        i * squareSize + squareSize,
                                        fill="#D42421",
                                        outline="#8b5546")


# register block selection for next moving
def click(event):
    global redTileStatus, tile
    redTileStatus = "UNSELECT" # "SELECT"

    xCursor, yCursor = event.x, event.y

    xCursor = xCursor // squareSize
    yCursor = yCursor // squareSize

    print(xCursor, yCursor, "xCursor and yCursor")
    print(redTileX, redTileY, " x and y for RedTile")
    for i in range(tilesAmount):
        print(TileCoordX[i], TileCoordY[i], "x" + str(i) + " and y" + str(i) + " for tile")

    if (xCursor == redTileX or xCursor - 1 == redTileX) and yCursor == redTileY:
        redTileStatus = "SELECT"
        for i in range(1):
            print(redTileStatus, " for RedTile")
    else:
        redTileStatus = "UNSELECT"
        print(redTileStatus, " for RedTile")

    for i in range(tilesAmount):
        tileInfo[i].TileStatus = "UNSELECT"
        if xCursor == TileCoordX[i] and yCursor == TileCoordY[i]:
            tileInfo[i].TileStatus = "SELECT"
            print(tileInfo[i].TileStatus, " for tile")
            print(TileCoordX[i], TileCoordY[i], "VERY IMPORTANT")
    for i in range (tilesAmount):
        print(tileInfo[i].TileStatus," for list of tiles")
        
    
    
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


# draw tiles
def draw_tile():
    global tile
    tile = [0] * boardSize
    for i in range(tilesAmount):
        TileCoordX[i] = TileCoordX[i] // squareSize
        TileCoordY[i] = TileCoordY[i] // squareSize
    for i in range(tilesAmount):
        tile[i] = canvas.create_rectangle(TileCoordX[i] * squareSize, TileCoordY[i] * squareSize,
                                        TileCoordX[i] * squareSize + squareSize,
                                        TileCoordY[i] * squareSize + squareSize,
                                        fill="#FFFF99",
                                        outline="#8b5546")
        print(tile[i], "= плитка")


# moving tiles when 1 of them selected
def move_tile(event):
    global redTileX, redTileStatus
    if redTileStatus == "SELECT":
        if event.keysym == 'Right' and (not redTileX == 4):
            for i in range(tilesAmount):
                if redTileX == TileCoordX[i]:
                    print(TileCoordX[i], redTileX, "дада")
                    break
                else:
                    print(TileCoordX[i], redTileX, "еще немного важной инфы")
                    canvas.move(redTile, squareSize, 0)
                    redTileX = redTileX + 1
                    print(redTileX, "position x + 1")
                    canvas.update()
                    if redTileX == 4:
                        Winner()
        if event.keysym == 'Left' and (not redTileX == 0):
            canvas.move(redTile, -squareSize, 0)
            redTileX = redTileX - 1
            print(redTileX, "position x - 1")
            canvas.update()
    for i in range (tilesAmount):
        if tileInfo[i].TileStatus == "SELECT":
            if event.keysym == 'Right':
                canvas.move(tile[i], squareSize, 0)
                TileCoordX[i] += 1
            if event.keysym == 'Left':
                canvas.move(tile[i], -squareSize, 0)
                TileCoordX[i] -= 1


# create window with image "you won"
def Winner():
    def on_closing():
        winWinner.destroy()

    winWinner = tk.Toplevel(root) 
    winWinner.protocol("WM_DELETE_WINDOW", on_closing)
    winWinner.title('You Win')
    winWinner.geometry('400x400+600+300')
    
    Mycanvas = tk.Canvas(winWinner,width=400,height=400)
    Mycanvas.pack()

    canvas_id = Mycanvas.create_text(180, 20, anchor="nw") 
    Mycanvas.itemconfig(canvas_id, text="You Win!") 

    pilImage = Image.open("unnamed1.jpeg")
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = Mycanvas.create_image(200,200,image=image)
    winWinner.mainloop()


# Game settings
root = tk.Tk() # main window
root.title("Slide Blocks") # window name
boardSize = 6
squareSize = 100
squares = boardSize ** 2

redTileX = 0
redTileY = 2

canvas = tk.Canvas(root, width=boardSize * squareSize, height=boardSize * squareSize, bg = "#808080")
canvas.focus_set()
canvas.pack()
canvas.bind('<Button-1>', click)
canvas.bind('<Right>', move_tile)
canvas.bind('<Left>', move_tile)
# canvas.bind('<Up>', Print)

board = list(range(1, squares + 1))
print(board)
tileInfo = [0] * 10

# Settings for module that i'm gonna create from menu on pygame
size = [0] * 10
TileCoordX = [0] * 10
TileCoordY = [0] * 10
tilesAmount = 6

for i in range(tilesAmount):
    size[i] = random.randint(2, 3)
    TileCoordX[i] = i * squareSize
    TileCoordY[i] = i * squareSize
    tileInfo[i] = Tile(size[i], "horizontal", TileCoordX[i], TileCoordY[i], "UNSELECT")
    tileInfo[i].description()

for i in range (1):
    draw_board()
    draw_tile()
    red_tile()   
root.mainloop()