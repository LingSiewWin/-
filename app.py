import pygame
import random

pygame.init()

# Set up the game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake and food settings
snake_block = 20
snake_speed = 15
snake_list = []
snake_head = [width // 2, height // 2]
snake_direction = "RIGHT"
food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

clock = pygame.time.Clock()
game_over = False

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

    # Update snake position
    if snake_direction == "RIGHT":
        snake_head[0] += snake_block
    elif snake_direction == "LEFT":
        snake_head[0] -= snake_block
    elif snake_direction == "UP":
        snake_head[1] -= snake_block
    elif snake_direction == "DOWN":
        snake_head[1] += snake_block

    # Check for collisions with walls
    if snake_head[0] >= width or snake_head[0] < 0 or snake_head[1] >= height or snake_head[1] < 0:
        game_over = True

    # Update snake body
    snake_list.append(list(snake_head))
    if len(snake_list) > 5:  # Snake length
        del snake_list[0]

    # Check for collisions with self
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Draw the snake and food
    window.fill(black)
    pygame.draw.rect(window, red, [food_x, food_y, snake_block, snake_block])
    for segment in snake_list:
        pygame.draw.rect(window, green, [segment[0], segment[1], snake_block, snake_block])

    # Check if snake eats food
    if snake_head[0] == food_x and snake_head[1] == food_y:
        food_x = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        food_y = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
        # Increase snake length by not deleting the tail

    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()