import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define player and enemy rectangles
player_rect = pygame.Rect(300, 300, 50, 50)  # x, y, width, height
enemy_rect = pygame.Rect(400, 400, 50, 50)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player rectangle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    # Check for collision
    if player_rect.colliderect(enemy_rect):
        print("Collision detected!")

    # Clear the screen
    screen.fill(WHITE)

    # Draw the rectangles
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, RED, enemy_rect)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
