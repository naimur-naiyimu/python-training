import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake attributes
snake_block = 20
snake_speed = 10

# Fonts
font_style = pygame.font.SysFont(None, 50)

# Function to draw the snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Function to display message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])

# Main game function
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1 = screen_width / 2
    y1 = screen_height / 2

    # Initial movement
    x1_change = 0
    y1_change = 0

    # Initial snake length
    snake_list = []
    length_of_snake = 1

    # Initial food position
    foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
    clock = pygame.time.Clock()
    while not game_over:
        while game_close == True:
            screen.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Event handling for game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling for movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        # Update snake's position
        x1 += x1_change
        y1 += y1_change

        # Boundary conditions
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True

        screen.fill(white)
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)

        pygame.display.update()

        # Snake eats food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, screen_height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        pygame.display.update()

        # Set game speed
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()
