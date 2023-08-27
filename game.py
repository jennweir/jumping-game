import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jumping Game")

# Colors
pink = (247, 185, 215)

# Player attributes
player_x = 50
player_y = height - 100
player_velocity = -10
jump_strength = -10
gravity = 0.5

# Player image
player_image = pygame.image.load('barbie.png')
# Get original dimensions
original_width, original_height = player_image.get_size()
desired_width = 150
aspect_ratio = original_width / original_height
desired_height = int(desired_width / aspect_ratio)
player_image = pygame.transform.scale(player_image, (desired_width, desired_height))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y == height - 300:
                player_velocity = jump_strength

    # Update player
    player_velocity += gravity
    player_y += player_velocity

    if player_y >= height - 300:
        player_y = height - 300
        player_velocity = 0

    # Clear the screen
    screen.fill(pink)

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Update display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
