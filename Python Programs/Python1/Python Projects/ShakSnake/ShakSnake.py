import pygame, random, os, sys

pygame.init()
pygame.mixer.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

# Game window
screenWidth = 800
screenHeight = 500
gameWindow = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Shak Snake")

#game specific variables
fps = 60

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 45) #Default system font with 55 font size

def displayText(text, color, posX, posY):
    screenText = font.render(text, True, color)
    gameWindow.blit(screenText, [posX, posY])


def plotSnake(gameWindow, color, snakeList, snakeSize):
    for x,y in snakeList:
        pygame.draw.rect(gameWindow, color, [x, y, snakeSize, snakeSize])


def welcomeScreen():
    exitGame = False
    gameWindow.fill((173, 230, 159))
    displayText("Hello Shak, Welcome To Snake..!", black, 160, screenHeight/2-100)
    displayText("Press Space Bar to play the game..!", black, 140, screenHeight/2)
    displayText('Press "I" to see the instructions of game', black, 120, screenHeight/2+50)
    while not exitGame:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameLoop()
                        
                    if event.key == pygame.K_i:
                        gameInstructions()
                        
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit(0)


def gameInstructions():
    exitGames = False
    gameWindow.fill((173, 230, 159))
    displayText("<- Backspace for main screen", blue, 10, 40)
    displayText("a or up-arrow -> Move Up", blue, 100, 80)
    displayText("d or right-arrow -> Move Right", blue, 100, 120)
    displayText("s or down-arrow -> Move Down", blue, 100, 160)
    displayText("w or left-arrow -> Move Left", blue, 100, 200)
    displayText("c -> Increase Score by 10", blue, 100, 240)
    displayText("x -> Decrease Score by 10", blue, 100, 280)
    displayText("h -> Reset High Score", blue, 100, 320)
    displayText("v -> Increase Snake Velocity", blue, 100, 360)
    displayText("b -> Decrease Snake Velocity", blue, 100, 400)
    displayText("Press Space Bar To Play The Game..!", blue, 20, 440)
    
    while not exitGames:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exitGames = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    welcomeScreen()
                    
                if event.key == pygame.K_SPACE:
                    gameLoop()
                    
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit(0)

def gameLoop():
    pygame.mixer.music.load("naginBackground.mp3")
    pygame.mixer.music.play()
    exitGame = False    
    gameOver = False
    snakeX = 55
    snakeY = 55
    velocity = 4
    velocityX = 0
    velocityY = 0
    snakeSize = 15
    score = 0
    foodX = random.randint(10,screenWidth/2)
    foodY = random.randint(10,screenHeight/2)
    snakeList = []
    snakeLength = 1
    
    if not os.path.exists("HighScore.txt"):
        with open("HighScore.txt", "w") as f:
            f.write("0")
        
    
    with open("HighScore.txt", "r") as f:
        highScore = f.read()

    while not exitGame:
        if gameOver:
            with open("HighScore.txt",'w') as f:
                f.write(str(highScore))
            gameWindow.fill((255, 172, 172))
            displayText("Game Over! Press Space Bar to play again.", red, 80, screenHeight/2-80)
            displayText('Press "I" to see the instructions of game.', red, 80, screenHeight/2-30)
            displayText("Your score was : " + str(score), blue, screenWidth/2-140, screenHeight/2+20)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameLoop()
                        
                    if event.key == pygame.K_i:
                        gameInstructions()
                
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exitGame = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_RIGHT, pygame.K_d]:
                        velocityX = velocity
                        velocityY = 0
                        
                    if event.key in [pygame.K_LEFT, pygame.K_a]:
                        velocityX = -velocity
                        velocityY = 0
                        
                    if event.key in [pygame.K_UP, pygame.K_w]:
                        velocityY = -velocity
                        velocityX = 0
                        
                    if event.key in [pygame.K_DOWN, pygame.K_s]:
                        velocityY = velocity
                        velocityX = 0
                        
                    if event.key == pygame.K_c:
                        score += 10
                    
                    if event.key == pygame.K_x:
                        score -= 10
           
                    if event.key == pygame.K_h:
                        highScore = 0
           
                    if event.key == pygame.K_v:
                        velocity += 0.2
                        
                    if event.key == pygame.K_b:
                        velocity -= 0.2
                        
            snakeX += velocityX   
            snakeY += velocityY
            
            if abs(snakeX - foodX ) < 17 and abs(snakeY - foodY) < 17:
                pygame.mixer.Sound("Beep.mp3").play()
                score += 10
                foodX = random.randint(10,screenWidth/2)
                foodY = random.randint(10,screenHeight/2)
                snakeLength += 5
                if score > int(highScore):
                    highScore = score
                
            gameWindow.fill(white)
            displayText("HighScore : " + str(highScore) + "  Score : " + str(score), blue, 5, 5)
            
            snakeHead = []
            snakeHead.append(snakeX)
            snakeHead.append(snakeY)
            snakeList.append(snakeHead)

            if len(snakeList) > snakeLength:
                del snakeList[0]
                
            if snakeX < 0 or snakeX>screenWidth or snakeY < 0 or snakeY > screenHeight:
                pygame.mixer_music.load("Explosion.mp3")
                pygame.mixer.music.play()
                gameOver = True

            if snakeHead in snakeList[:-1]: #Containing all elements of snakeList except the last one(i.e. head)
                pygame.mixer_music.load("Explosion.mp3")
                pygame.mixer.music.play()
                gameOver = True
                
            # Drawing snake
            plotSnake(gameWindow, black, snakeList, snakeSize)
            # Drawing food
            pygame.draw.rect(gameWindow, green, [foodX, foodY, snakeSize, snakeSize])
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    sys.exit(0)

    
if __name__ == "__main__":
    welcomeScreen()