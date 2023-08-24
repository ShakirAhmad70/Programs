import pygame
import random

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 800))

# Load the background image
background = pygame.image.load("background.jpg")

# Create the bubble class
class Bubble(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += 0.3

# Create the bubbles
bubbles = []
for i in range(10):
    color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    x = random.randint(0, 400)
    y = 0
    bubble = Bubble(color, x, y)
    bubbles.append(bubble)

# The game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the bubbles
    for bubble in bubbles:
        bubble.update()

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the bubbles
    for bubble in bubbles:
        screen.blit(bubble.image, bubble.rect)

    # Update the display
    pygame.display.flip()

# Close Pygame
pygame.quit()
