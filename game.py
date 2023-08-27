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

# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_x = width  # Start obstacles off the screen
obstacle_y = height - obstacle_height
obstacle_speed = 10

# Game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_y == height - 300:
                player_velocity = jump_strength

    # Update player
    if not game_over:
        player_velocity += gravity
        player_y += player_velocity

    if player_y >= height - 300:
        player_y = height - 300
        player_velocity = 0

    # Update obstacle
    if not game_over:
        obstacle_x -= obstacle_speed
        if obstacle_x < 0:
            obstacle_x = width
            obstacle_y = height - obstacle_height

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_image.get_width(), player_image.get_height())
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    
    if player_rect.colliderect(obstacle_rect):
        game_over = True

    # Clear the screen
    screen.fill(pink)

    # Draw player
    screen.blit(player_image, (player_x, player_y))

    # Draw obstacle
    pygame.draw.rect(screen, (255, 0, 0), (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Update display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
