import pygame
pygame.init()

import random

def get_random_color_rgb():
    ans = random.sample(range(0, 255, 10), 3)
    return ans

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("ცხვენია და იმალება ხოლმე ^_^")

x = 50 + 200
y = 50 + 200
width = 3
height = 3
vel = 5

run = True


while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    key = random.randint(1,5)

    if key == 1:
        # rgb_col = [0, 255, 0]
        x -= vel
    if key == 2:
        # rgb_col = [255, 0, 0]
        x += vel
    if key == 3:
        # rgb_col = [0, 0, 255]
        y -= vel
    if key == 4:
        # rgb_col = [255, 255, 255]
        y += vel


    # win.fill((0,0,0))
    pygame.draw.rect(
                win,
                (0, 255, 0),
                # get_random_color_rgb(),
                # rgb_col,
                (x, y, width, height))
    pygame.display.update()

pygame.quit()
