"""
This is a sample game to demonstrate pygame to my students.
It isn't a fun game, but demonstrates some key functions
of pygame library

There are three shapes on the screen with three different motion dynamics
"""
import pygame
from pygame.math import Vector2
from random import randint

# starting positions of triangle, circle and square are randomized
triangle_pos = Vector2(randint(10,400), randint(10,400))
circle_pos = Vector2(randint(10,400), randint(10,400))
square_pos = Vector2(randint(10,400), randint(10,400))

score = 0

triangle_original_surface = pygame.Surface((40,  40), pygame.SRCALPHA)
pygame.draw.polygon(triangle_original_surface, (210, 180, 0), [[0, 40], [20, 0], [40, 40]])
triangle = triangle_original_surface

pygame.init()

font = pygame.font.Font(None, 24)



screen = pygame.display.set_mode((460, 460))
pygame.display.set_caption('Circle Square Triangle')
running = True
clock = pygame.time.Clock()

circle_velocity = Vector2(-2.0, 1.2)
triangle_angle = 1
circle_color = 0

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # square motion
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                square_pos.x -= 10
            elif event.key == pygame.K_RIGHT:
                square_pos.x += 10
            elif event.key == pygame.K_UP:
                square_pos.y -= 10
            elif event.key == pygame.K_DOWN:
                square_pos.y += 10

    # circles motion
    if (circle_pos.x + circle_velocity.x < 0) or (circle_pos.x + circle_velocity.x > 420):
        circle_velocity.x = -circle_velocity.x
    if (circle_pos.y + circle_velocity.y < 0) or (circle_pos.y + circle_velocity.y > 420):
        circle_velocity.y = -circle_velocity.y
    circle_pos = circle_pos + circle_velocity

    screen.fill((0,0,0))

    # square rect and circle rect
    square_rect = pygame.Rect(square_pos.x, square_pos.y, 40, 40)
    circle_rect = pygame.Rect(circle_pos.x, circle_pos.y, 40, 40)

    # if square and circle are touching
    if square_rect.colliderect(circle_rect):
        score = 0
        screen.fill((255,0,0))
        clock.tick(10)  # slow motion death screen

    # rotating triangle 1 degree at a time
    triangle_angle = (triangle_angle + 1) % 360
    triangle = pygame.transform.rotate(triangle_original_surface, triangle_angle)
    triangle_rect = triangle.get_rect()
    triangle_rect.center = triangle_pos

    # if triangle and square are touching
    if triangle_rect.colliderect(square_rect):
        score += 1
        triangle_pos = Vector2(randint(10,400), randint(10,400))

    # keep changing the red shade of the circle
    circle_color = (circle_color + 1) % 255
    pygame.draw.rect(screen, (0, 128, 255), square_rect)
    pygame.draw.ellipse(screen, (circle_color, 128, 128), circle_rect)
    screen.blit(triangle, triangle_rect)

    text = font.render("Score " + str(score), True, (0, 128, 0))
    screen.blit(text,(10,10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()