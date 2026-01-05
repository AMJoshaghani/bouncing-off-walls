import pygame, sys
from pygame.locals import *

pygame.init()
# constants
DISPLAY = pygame.display.set_mode((800, 600))
BLACK = pygame.Color(0, 0, 0)
YELLOW = pygame.Color(255, 255, 0)
RED = pygame.Color(255, 0, 0)

# ball
ball_speed = (2.5, 2.5)
ball_position = (385, 285)

# FPS
FPS = pygame.time.Clock()

# loop
while True:
    # quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # objects
    #   surface
    DISPLAY.fill(BLACK)
    #   wall
    pygame.draw.rect(DISPLAY, RED, (0, 0, 800, 600), 3)

    #   ball
    pygame.draw.circle(DISPLAY, YELLOW, ball_position, 30)
    ball_position = (ball_position[0] + ball_speed[0], ball_position[1] + ball_speed[1])

    #       velocity on impact
    if ball_position[0] + 30 >= 800 or ball_position[0] - 30 <= 0:
        ball_speed = (-ball_speed[0], ball_speed[1])

    if ball_position[1] + 30 >= 600 or ball_position[1] - 30 <= 0:
        ball_speed = (ball_speed[0], -ball_speed[1])

    # Update position
    ball_position = (ball_position[0] + ball_speed[0], ball_position[1] + ball_speed[1])

    # screen
    FPS.tick(60)
    pygame.display.set_caption("Wall Collision")
    pygame.display.flip()
