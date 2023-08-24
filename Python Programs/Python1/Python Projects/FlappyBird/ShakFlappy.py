import pygame 

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating game window
screenWidth =330
screenHeight = 600
gameWindow = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Shak Flappy Bird")
pygame.display.update()

# Game specific variables
exitGame = False
gameOver = False
snakeX = 55
snakeY = 55
snakeSize = 10


# Creating game loop
while not exitGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitGame = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed right key")
                
    
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snakeX, snakeY, snakeSize, snakeSize])
    pygame.display.update()
            

pygame.quit() #quit pygame
quit() #quit python
