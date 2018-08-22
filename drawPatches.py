from graphics import *
import math

def drawPatchOne(window, x, y, colour):
    yCordForRect = 0
    for i in range(100, 19, -20):
        whiteSquare = Rectangle(Point(x, y + yCordForRect), Point(x+i, y+100))
        whiteSquare.setOutline("white")
        whiteSquare.setFill("white")
        colourSquare = Rectangle(Point(x, y + yCordForRect+10), Point(x+i-10, y+100))
        colourSquare.setOutline(colour)
        colourSquare.setFill(colour)
        whiteSquare.draw(window)
        colourSquare.draw(window)
        yCordForRect = yCordForRect + 20
        
def drawPatchTwo(window, x, y, colour):
    background = Rectangle(Point(x,y), Point(x+100, y+100))
    background.setFill("white")
    background.setOutline("white")
    background.draw(window)
    
    for yRowOne in range(y, y+100, 20):
        for xRowOne in range(x+25, x+56, 30):
            rect = Rectangle(Point(xRowOne,yRowOne), Point(xRowOne+20, yRowOne+10))
            rect.setFill(colour)
            rect.setOutline("black")
            rect.draw(window)
    for yRowTwo in range(y+10, y+100, 20):
        for xRowTwo in range(x+10, x+100, 30):
            rect = Rectangle(Point(xRowTwo,yRowTwo), Point(xRowTwo+20, yRowTwo+10))
            rect.setFill(colour)
            rect.setOutline("black")
            rect.draw(window)
    for yleftEdgeRect in range(y, y+100, 20):
        rect = Rectangle(Point(x,yleftEdgeRect), Point(x+15,yleftEdgeRect+10))
        rect.setFill(colour)
        rect.setOutline("black")
        rect.draw(window)
    for yRightEdgeRect in range(y, y+100, 20):
        rect = Rectangle(Point(x+85,yRightEdgeRect), Point(x+100,yRightEdgeRect+10))
        rect.setFill(colour)
        rect.setOutline("black")
        rect.draw(window)

def roundDown(x):
    # this function rounds down the given parameter x
    return int(math.floor(x/100)) * 100

def drawPatchwork(patchwork_size, colours):
    win_sizeX, win_sizeY = patchwork_size * 100, patchwork_size * 100
    patchworkWin = GraphWin("Patchwork Sample", win_sizeX, win_sizeY)
    
    coOrds = []
    # a list that takes the coordinates of the top-right point
    # of each patch drawn to the window
    
    coloursUsed = []
    # a list that takes the colours of each patch drawn to the window
    # coloursUsed and coOrds contains the same number of items
    
    i = 0
    for y in range(0, win_sizeY, 100):
        for x in range(0, win_sizeX, 100):
            if i > 3:
                i = 0
            if x == 0 or x == patchwork_size * 100 - 100 or y == win_sizeY//2 - 50:
                drawPatchOne(patchworkWin, x, y, colours[i])
                coOrds.append((x,y))
                coloursUsed.append(colours[i])
            else:
                drawPatchTwo(patchworkWin, x, y, colours[i])
                coOrds.append((x,y))
                coloursUsed.append(colours[i])
            i = i + 1
        
    print(coOrds)
    print(coloursUsed)

    while True:
        mouse_click = patchworkWin.getMouse()
        # x,y are rounded down to the nearest hundread in order to match the co-ordinates in the list coOrds
        x_click = roundDown(mouse_click.getX())
        y_click = roundDown(mouse_click.getY())
        
        # finds the index in the list of co-ordinates for a specific colour
        patch_position_index = coOrds.index((x_click, y_click))

        # in order to display the next colour in the original list of given colours
        newColour = colours.index(coloursUsed[patch_position_index]) + 1
        
        if newColour > 3:
            newColour = 0
            
        if x_click == 0 or x_click == patchwork_size * 100 - 100 or y_click == win_sizeY//2 - 50:
            drawPatchOne(patchworkWin, x_click, y_click, colours[newColour])
        else:
            drawPatchTwo(patchworkWin, x_click, y_click, colours[newColour])
        coloursUsed[patch_position_index] = colours[newColour]
        newColour = newColour + 1
        print(newColour)
        
def takeGrid(x=5):
    num = 0
    for k in range(x):
        grid = [[" " for x in range(x)] for e in range(x)]
        for j in range(x):
            for i in range(5):
                grid[j][i] = num
                num = num + 1
                if num == 4:
                    num = 0
        print(grid)

def getInfo():
    print("this program will show you a large patchwork")
    print('')
    
    valid_patch_sizes = [5,7,9]
    valid_colours = ["red", "green", "blue", "yellow", "magenta", "cyan"]
    colours_to_use = []

    while True:
        patchInput = eval(input("Enter your desired patch size: "))
        print('')
        if patchInput in valid_patch_sizes:
            while patchInput:
                rawColourInput = input("Enter your desired colour: ")
                print('')
                colourInput = rawColourInput.lower()
                if colourInput in valid_colours:
                    colours_to_use.append(colourInput)
                    if len(colours_to_use) == 4:
                        return patchInput, colours_to_use
                        break
                else:
                    print("That colour is not valid, the valid colours are:")
                    print("red, green, blue yellow, magenta, cyan")
                    print('')
        else:
            print("This is not valid patch size, please try again")
            print("the patch size must be 5, 7 or 9")
            print('')
            
def main():
    patchSize, colour = getInfo()
    drawPatchwork(patchSize, colour)

main()