import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jumping Game")

# Colors
white = (255, 255, 255)

# Player attributes
player_x = 50
player_y = height - 100
player_velocity = 0
jump_strength = -10
gravity = 0.5

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y == height - 100:
                player_velocity = jump_strength

    # Update player
    player_velocity += gravity
    player_y += player_velocity

    if player_y >= height - 100:
        player_y = height - 100
        player_velocity = 0

    # Clear the screen
    screen.fill(white)

    # Draw player
    pygame.draw.circle(screen, (0, 0, 255), (player_x, int(player_y)), 20)

    # Update display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
