import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Shot Game")

# Set up colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Set up the player
player_radius = 20
player_pos = [WIDTH // 2, HEIGHT - 2 * player_radius]

# Set up the bullets
bullet_radius = 5
bullet_pos = []
bullet_speed = 10
bullet_list = []

# Set up the bubbles
bubble_radius = 30
bubble_speed = 5
bubble_list = []

# Set up game variables
score = 0
clock = pygame.time.Clock()
game_over = False

# Set up fonts
font = pygame.font.Font(None, 36)

# Function to create bubbles
def create_bubbles():
    x = random.randint(bubble_radius, WIDTH - bubble_radius)
    y = random.randint(bubble_radius, HEIGHT // 2)
    bubble_list.append([x, y])

# Function to draw the player
def draw_player():
    pygame.draw.circle(window, BLUE, player_pos, player_radius)

# Function to draw the bullets
def draw_bullets():
    for bullet in bullet_list:
        pygame.draw.circle(window, RED, bullet, bullet_radius)

# Function to draw the bubbles
def draw_bubbles():
    for bubble in bubble_list:
        pygame.draw.circle(window, RED, bubble, bubble_radius)

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            bullet_pos = player_pos[:]
            bullet_list.append(bullet_pos)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5

    # Update bullet positions
    for bullet in bullet_list:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:
            bullet_list.remove(bullet)

    # Update bubble positions
    for bubble in bubble_list:
        bubble[1] += bubble_speed

        # Check for collision with bullets
        for bullet in bullet_list:
            if bubble_radius > abs(bubble[0] - bullet[0]) > 0 and bubble[1] - bullet[1] <= bubble_radius:
                bubble_list.remove(bubble)
                bullet_list.remove(bullet)
                score += 1

        # Check for collision with player
        if bubble_radius > abs(bubble[0] - player_pos[0]) > 0 and bubble[1] - player_pos[1] <= bubble_radius:
            game_over = True

        # Check if bubble reaches the bottom
        if bubble[1] > HEIGHT:
            game_over = True

    # Create new bubbles
    if len(bubble_list) < 10:
        create_bubbles()

    # Draw on the window
    window.fill(WHITE)

    # Draw the player
    draw_player()

    # Draw the bullets
    draw_bullets()

    # Draw the bubbles
    draw_bubbles()

    # Draw the score
    score_text = font.render("Score: " + str(score), True, BLUE)
    window.blit(score_text, [10, 10])

    # Update the display
    pygame.display.update()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
