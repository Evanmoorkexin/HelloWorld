# First Project for My Language Learning
# Create a simple game like snake for "Hello World" in Python

import pygame
import random

pygame.init()

# Define Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# Define Screen Size
display_width = 800
display_height = 600

# Define Size of Snake
block_size = 10

# Define Speed of Snake
FPS = 30

# Define Font
font = pygame.font.SysFont(None, 25)

# Define Game Display
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Hello World')

# Define Clock
clock = pygame.time.Clock()

# Define Snake
def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

# Define Message to Screen
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

# Define Game Loop
def gameLoop():
    gameExit = False
    gameOver = False

    # Define Starting Position of Snake
    lead_x = display_width / 2
    lead_y = display_height / 2

    # Define Change of Position of Snake
    lead_x_change = 0
    lead_y_change = 0

    # Define Snake List
    snakeList = []
    snakeLength = 1

    # Define Random Position of Apple
    randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    # Define Game Loop
    while not gameExit:

        # Define Game Over Loop
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over, press C to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_c:
                        gameLoop()
            gameLoop()

        # Define Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        # Define Boundaries
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        # Define Change of Position of Snake
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Define Display
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        # Define Snake
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(block_size, snakeList)

        pygame.display.update()

        # Define Apple
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            randAppleY = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            snakeLength += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()







