'''
    Define OOP method to play 
    simple snake game.
'''
import pygame
import random


class Snake:
    def __init__(self,
                 color=(255, 0, 0),
                 thickness=10,
                 speed=10,
                 delay=50,
                 direction="right"):
        '''
        Initialize object with given parameters:
            1. color - color(rgb tuple) for snake(default=(255, 0, 0) - red)
            2. thickness - how thick it will be (default=3)
            3. speed - how fast will it move (default=5)
            4. delay - pygame delay (default=50)
            5. direction to move towards initially)(default="right")
        '''
        self.color = color
        self.thickness = thickness
        self.speed = speed
        self.x = 200  # starting position X coordinate
        self.y = 200  # starting position Y coordinate
        self.delay = delay
        self.direction = direction



    def play(self):
        '''
        Start game
        '''
        pygame.init()
        window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Let's play the game ^_^")
        run = True

        while run:
            pygame.time.delay(self.delay)

            # if X was pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # get pressed key
            keys = pygame.key.get_pressed()
            # print(keys)


            # we care about direction keys only(yet)
            self._update_snake_coordinates(keys)

            # print(self.x, self.y)
            # draw the snake
            window.fill((0,0,0))
            pygame.draw.rect(
                window,
                self.color,
                (self.x, self.y, self.thickness, self.thickness))
            pygame.display.update()
        pygame.quit()


    def _update_snake_coordinates(self, keys):
        '''
        get keys and update
        snake coordinates accordingly
        '''
        # change direction
        if keys[pygame.K_LEFT]:
            self.direction = "left"
            # self.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.direction = "right"
            # self.x += self.speed

        if keys[pygame.K_UP]:
            self.direction = "up"
            # self.y -= self.speed

        if keys[pygame.K_DOWN]:
            self.direction = "down"
            # self.y += self.speed

        # move
        if self.direction == "right":
            self.x += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed

        print(self.x, self.y, self.direction)
        # change direction if wall was there
        if self.x >= 500:
            self.direction = "left"
        elif self.x <= 0:
            # print("x < 0")
            self.direction = "right"
            # breakpoint()
        elif self.y >= 500:
            # print("y >  500")
            self.direction = "up"
        elif self.y <= 0:
            # print("y <  0")
            self.direction = "down"
    # def _draw_snake():


# test
snake = Snake()
snake.play()