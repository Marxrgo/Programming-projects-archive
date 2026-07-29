import pygame
from pygame.locals import *
import random

pygame.init()

# Variables:
gameSpeed = 20  # controls fps and game speed
shouldGrow = False
cell_size = 10
direction = 1  # 1 up, 2 right , 3 down, 4 left
screen_width = 600  # Width
screen_height = 600  # Height

# Colors
body_inner = (45, 159, 22)
body_outer = (100, 100, 200)
red = (255, 0, 0)

# Game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

# Backgorund
bg = pygame.Surface((screen_width, screen_height))
bg.fill((0, 0, 0))
for i in range(0, screen_height, cell_size):
    if (i / cell_size) % 2 == 0:
        for y in range(0, screen_width, cell_size):
            if (y / cell_size) % 2 == 0:
                pygame.draw.rect(
                    bg,
                    color=(0, 230, 0),
                    rect=(y, i, cell_size, cell_size),
                    border_radius=1,
                )
            else:
                pygame.draw.rect(
                    bg,
                    color=(0, 200, 0),
                    rect=(y, i, cell_size, cell_size),
                    border_radius=1,
                )
    else:
        for y in range(0, screen_width, cell_size):
            if (y / cell_size) % 2 == 1:
                pygame.draw.rect(
                    bg,
                    color=(0, 230, 0),
                    rect=(y, i, cell_size, cell_size),
                    border_radius=1,
                )
            else:
                pygame.draw.rect(
                    bg,
                    color=(0, 200, 0),
                    rect=(y, i, cell_size, cell_size),
                    border_radius=1,
                )


# Create snake
def create_snake():
    snake_pos = [[int(screen_width / 2), int(screen_height / 2)]]  # X , Y
    snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size])
    snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 2])
    snake_pos.append([int(screen_width / 2), int(screen_height / 2) + cell_size * 3])
    return snake_pos

snake_pos = create_snake()


# Fruit
def randomfunc():
    x = int(random.randint(0, int((screen_width/cell_size))-1)) * cell_size
    y = int(random.randint(0, int((screen_width/cell_size))-1)) * cell_size
    return [x, y]

fruit_pos = randomfunc()

# Setup loop
run = True
clock = pygame.time.Clock()
while run:
    screen.blit(bg, (0, 0))
    clock.tick(gameSpeed)

    # Iterate through events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4

    # Update snake position
    update_snake = 0
    if shouldGrow == False:
        snake_pos = [[snake_pos[0][0], snake_pos[0][1]]] + snake_pos[:-1]
    else:
        snake_pos = [[snake_pos[0][0], snake_pos[0][1]]] + snake_pos
        shouldGrow = False

    if direction == 1:  # moving UP
        snake_pos[0][1] -= cell_size
    if direction == 3:  # moving DOWN
        snake_pos[0][1] += cell_size
    if direction == 2:  # moving RIGHT
        snake_pos[0][0] += cell_size
    if direction == 4:  # moving LEFT
        snake_pos[0][0] -= cell_size

    if not (0 <= snake_pos[0][0] <= 599 and 0 <= snake_pos[0][1] <= 599):
        snake_pos = create_snake()
        direction = 1

    # Draw snake
    head = 1
    for x in snake_pos:
        if head == 0:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(
                screen, body_inner, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2)
            )
        if head == 1:
            pygame.draw.rect(screen, body_outer, (x[0], x[1], cell_size, cell_size))
            pygame.draw.rect(
                screen, red, (x[0] + 1, x[1] + 1, cell_size - 2, cell_size - 2)
            )
            head = 0

    pygame.draw.rect(screen, red, (fruit_pos[0], fruit_pos[1], cell_size, cell_size))

    if snake_pos[0] == fruit_pos:
        shouldGrow = True
        fruit_pos = randomfunc()

    # Update the display
    pygame.display.update()

# end pygame
pygame.quit()
