import pygame
import random

# initialize pygame
pygame.init()

# setup the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE")


# define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# define directions
RIGHT = 'RIGHT'
LEFT = 'LEFT'
UP = 'UP'
DOWN = 'DOWN'

# setup the game clock
clock = pygame.time.Clock()

# setup the snake and food positions
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50], [60, 50], [50, 50], [40, 50], [30, 50]]
food_position = [random.randrange(1, (width // 10)) * 10,
                 random.randrange(1, (height // 10)) * 10]
food_spawned = True

# setup the initial game variables
direction = RIGHT
change_to = direction
score = 0


# setup the game over flag
game_over = False

# function to display the score on the screen
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()

    if choice == 1:
        score_rect.midtop = (width / 10, 15)
    else:
        score_rect.midtop = (width / 2, height / 1.25)

    window.blit(score_surface, score_rect)


# main game loop
while not game_over:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            # arrow key presses
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = UP
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = DOWN
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = LEFT
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = RIGHT
    # making sure the snake cannot move in the opposite direction
    if change_to == UP and direction != DOWN:
        direction = UP
    if change_to == DOWN and direction != UP:
        direction = DOWN
    if change_to == LEFT and direction != RIGHT:
        direction = LEFT
    if change_to == RIGHT and direction != LEFT:
        direction = RIGHT

    # moving the snake
    if direction == UP:
        snake_position[1] -= 10
    if direction == DOWN:
        snake_position[1] += 10
    if direction == LEFT:
        snake_position[0] -= 10
    if direction == RIGHT:
        snake_position[0] += 10

    # snake body growth mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        score += 1
        food_spawned = False
    else:
        snake_body.pop()


    # respawn food when eaten
    if not food_spawned:
        food_position = [random.randrange(1, (width // 10)) * 10,
                         random.randrange(1, (height // 10)) * 10]

    food_spawned = True

    # gfx
    window.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(window, RED, pygame.Rect(food_position[0], food_position[1], 10, 10))
    # game over conditions
    if snake_position[0] < 0 or snake_position[0] > width - 10:
        game_over = True
    if snake_position[1] < 0 or snake_position[1] > height - 10:
        game_over = True
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over = True

    # display score
    show_score(1, WHITE, 'consolas', 20)

    # refresh game screen
    pygame.display.update()

    # fps
    clock.tick(15)

pygame.quit()

