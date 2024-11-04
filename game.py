import pygame
import sys

pygame.init()

size = width, height = 300, 300
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BOARDSTATE = [["-","-","-"],["-","-","-"],["-","-","-"]]
TURNOFX = True

def drawO(square):
    x = (square[0] + square[1]) / 2
    y = (square[2] + square[3]) / 2
    pygame.draw.circle(screen, BLACK, (x, y), height // 7)
    pygame.draw.circle(screen, WHITE, (x, y), height // 8)
    

def drawX(square):
    pygame.draw.line(screen, BLACK, (square[0], square[2]), (square[1], square[3]), 6)
    pygame.draw.line(screen, BLACK, (square[1], square[2]), (square[0], square[3]), 6)

def drawBoard():
    pygame.draw.line(screen, BLACK, (0, height // 3), (width, height // 3), 3)
    pygame.draw.line(screen, BLACK, (0, 2 * height // 3), (width, 2 * height // 3), 3)
    pygame.draw.line(screen, BLACK, (width // 3, 0), (width // 3, height), 3)
    pygame.draw.line(screen, BLACK, (2 * width // 3, 0), (2 * width // 3, height),3)

def getPosi(mousePointer):
    x = mousePointer[0]
    y = mousePointer[1]

    square = [0,0,0,0]

    state = [0,0]

    if x < width // 3: 
        square[0] = 0
        square[1] = width // 3
        state[0] = 0
    elif x < 2 * width // 3: 
        square[0] = width // 3
        square[1] = 2 * width // 3
        state[0] = 1
    else: 
        square[0] = 2 * width // 3
        square[1] = width
        state[0] = 2
    
    if y < height // 3: 
        square[2] = 0
        square[3] = height // 3
        state[1] = 0
    elif y < 2 * height // 3: 
        square[2] = height // 3
        square[3] = 2 * height // 3
        state[1] = 1
    else: 
        square[2] = 2 * height // 3
        square[3] = height
        state[1] = 2

    return square,state

def winstate():
    for i in range(3):
        if BOARDSTATE[i][0] == BOARDSTATE[i][1] == BOARDSTATE[i][2] != "-":
            return BOARDSTATE[i][0]
        if BOARDSTATE[0][i] == BOARDSTATE[1][i] == BOARDSTATE[2][i] != "-":
            return BOARDSTATE[0][i]

    if BOARDSTATE[0][0] == BOARDSTATE[1][1] == BOARDSTATE[2][2] != "-":
        return BOARDSTATE[0][0] 
    if BOARDSTATE[0][2] == BOARDSTATE[1][1] == BOARDSTATE[2][0] != "-":
        return BOARDSTATE[0][2]

    return None


def printBoard():
    for i in range(3):
        for j in range(3):
            print('[' + BOARDSTATE[j][i] + ']',end=" ")
        print()
    print()

running = True
screen.fill(WHITE)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            square,state = getPosi(mousePointer=pygame.mouse.get_pos())
            if BOARDSTATE[state[0]][state[1]] == "-":
                if TURNOFX:
                    drawX(square=square)
                    BOARDSTATE[state[0]][state[1]] = "X"
                    TURNOFX = not TURNOFX
                else:
                    drawO(square=square)
                    BOARDSTATE[state[0]][state[1]] = "O"
                    TURNOFX = not TURNOFX

                printBoard()
                if winstate() != None:
                    print("AND THE WINNER IS : ",winstate())
                    running = False

    drawBoard()
    pygame.display.flip()

pygame.quit()
sys.exit()