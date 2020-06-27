import random
import time
import pygame

pygame.init()



WIDTH  = 1200
HEIGHT = 600

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SNAKE MANIA")

SCREEN_COLOR = (0, 255, 0)
FONT_COLOR   = (0,   0, 0)
FOOD_COLOR   = (255, 0, 0)
SNAKE_COLORS = [(51, 25, 0), (153, 76, 0), (102, 51, 0), (204, 102, 0), (255, 128, 0),\
                (255, 153, 51), (255, 178, 102), (51, 51, 0), (102, 102, 0), (153, 153, 0),\
                (204, 204, 0), (255, 255, 0), (255, 255, 51), (255, 255, 102), (0, 153, 153),\
                (0, 204, 204), (0, 255, 255), (51, 255, 255), (102, 255, 255), (0, 51, 102), \
                (0, 76, 153), (0, 102, 204), (0, 128, 255), (51, 153, 255), (102, 178, 255), \
                (0, 0, 153), (102, 0, 102), (153, 0, 153), (153, 0, 76), (204, 0, 204),\
                (204, 0, 102), (255, 0, 255), (255, 0, 127), (255, 51, 153), (255, 51, 255)]

def drawSquare(x: float, y: float, side: int, color: (int)):
    pygame.draw.rect(SCREEN, color, [x, y, side, side])
   
def printMessage(message: str, x: int, y: int, color: (int)):
    font = pygame.font.SysFont("arialblack", 40)
    display_text = font.render(message, True, color)
    SCREEN.blit(display_text, [x, y])

def makeSnake(size: int, position: [int]):
    for block in position:
        color = random.choice(SNAKE_COLORS)
        drawSquare(block[0], block[1], size, color)

def makeFood(size: int) -> (float, float):
    x = random.randrange(0, WIDTH  - size)
    y = random.randrange(0, HEIGHT - size)
    return x, y

def closeScreen(score: int):

    inclose = True
    while inclose:
        SCREEN.fill(SCREEN_COLOR)
        printMessage(    "GAME OVER"            , WIDTH // 4,  HEIGHT // 6       , FONT_COLOR)
        printMessage(    "PRESS P TO PLAY AGAIN", WIDTH // 4,  HEIGHT // 6 +  100, FONT_COLOR)
        printMessage(    "PRESS Q TO QUIT GAME ", WIDTH // 4,  HEIGHT // 6 +  200, FONT_COLOR)
        printMessage("YOUR SCORE: " + str(score), WIDTH // 4, HEIGHT  // 6 +  300, FONT_COLOR)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    snakemania()
                if event.key == pygame.K_q:
                    inclose = False

    pygame.quit
    quit()

        
def snakemania():

    snake = 1
    size  = 10
    speed = 10
    score = 0
    positions = []
    clock = pygame.time.Clock()

    x1, y1 = WIDTH  / 2, HEIGHT / 2
    x2, y2 = 0, 0
    x, y = makeFood(size)
    
    

    playing     =  True

    while playing:

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                playing = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x2 = -size
                    y2 = 0

                elif event.key == pygame.K_RIGHT:
                    x2 = size
                    y2 = 0
                    
                elif event.key == pygame.K_UP:
                    x2 = 0
                    y2 = -size
                    
                    
                elif event.key == pygame.K_DOWN:
                    x2 = 0
                    y2 = size

            if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
                closeScreen(score)

            x1 += x2
            y1 += y2

            SCREEN.fill(SCREEN_COLOR)
            drawSquare(x, y, size, FOOD_COLOR)
            blocks = [x1, y1]
            positions.append(blocks)
            if len(positions) > snake:
                del positions[0]

            for block in positions[: -1]:
                if block == blocks:
                    closeScreen(score)

            makeSnake(size, positions)
            printMessage(str(score), 1120, 550, FONT_COLOR)

            pygame.display.update()

            if x == x1 and y == y1:
                x, y = makeFood(size)
                snake = snake + 1
                score = score + 1
                
            
            clock.tick(speed)

    pygame.quit()
    quit()


snakemania()


            

            
            

        
            

        








    
    


