import pygame
import time
import random

pygame.init()

# Set up the display
width, height = 800, 600
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake parameters
snake_block = 10
snake_speed = 10

# Create the snake
snake = [(width // 2, height // 2)]
snake_direction = 'RIGHT'
change_to = snake_direction

# Initialize the game clock
clock = pygame.time.Clock()

# Load music files
pygame.mixer.music.load("C:\\Users\krish\OneDrive\Desktop\movement.mp3")
crash_sound = pygame.mixer.Sound("C:\\Users\krish\OneDrive\Desktop\game_over.wav")
game_over_sound = pygame.mixer.Sound("C:\\Users\krish\OneDrive\Desktop\game_over.wav")

# Function to play background music
def play_background_music():
    pygame.mixer.music.play(-1)

# Function to play crash sound
def play_crash_sound():
    crash_sound.play()

# Function to play game over sound
def play_game_over_sound():
    game_over_sound.play()

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(dis, green, [block[0], block[1], snake_block, snake_block])

# Function to display the score
def Your_score(score):
    font = pygame.font.SysFont(None, 35)
    value = font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Function to display the game over message and score
def game_over_msg(score):
    font = pygame.font.SysFont(None, 50)
    over_msg = font.render("Game Over! Your Score: " + str(score), True, white)
    dis.blit(over_msg, [width // 4, height // 2])
    pygame.display.update()
    time.sleep(2)

# Main game loop
game_over = False
game_close = False

foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

play_background_music()

score = 0

while not game_over:

    while game_close == True:
        dis.fill(blue)
        Your_score(score)
        game_over_msg(score)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    # Reset game variables
                    snake = [(width // 2, height // 2)]
                    snake_direction = 'RIGHT'
                    change_to = snake_direction
                    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                    game_close = False
                    score = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not snake_direction == 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and not snake_direction == 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_UP and not snake_direction == 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and not snake_direction == 'UP':
                change_to = 'DOWN'

    # Update snake direction
    if change_to == 'LEFT':
        snake_direction = 'LEFT'
    elif change_to == 'RIGHT':
        snake_direction = 'RIGHT'
    elif change_to == 'UP':
        snake_direction = 'UP'
    elif change_to == 'DOWN':
        snake_direction = 'DOWN'

    # Move the snake
    if snake_direction == 'LEFT':
        snake[0] = (snake[0][0] - snake_block, snake[0][1])
    elif snake_direction == 'RIGHT':
        snake[0] = (snake[0][0] + snake_block, snake[0][1])
    elif snake_direction == 'UP':
        snake[0] = (snake[0][0], snake[0][1] - snake_block)
    elif snake_direction == 'DOWN':
        snake[0] = (snake[0][0], snake[0][1] + snake_block)

    # Check if snake hits the boundaries
    if (
        snake[0][0] >= width
        or snake[0][0] < 0
        or snake[0][1] >= height
        or snake[0][1] < 0
    ):
        game_close = True
        play_crash_sound()

    # Check if snake collides with itself
    for segment in snake[1:]:
        if snake[0] == segment:
            game_close = True
            play_crash_sound()

    # Generate new food if eaten
    if snake[0][0] == foodx and snake[0][1] == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake.append((1, 1))
        score += 1
    

    # Update the display
    dis.fill(blue)
    pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
    our_snake(snake_block, snake)
    pygame.display.update()

    # Set the speed of the game
    clock.tick(snake_speed)

# Play game over sound and quit the game
play_game_over_sound()
pygame.quit()