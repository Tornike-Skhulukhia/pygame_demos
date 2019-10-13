'''
    Define OOP method to play 
    simple snake game.
'''
import pygame
import random


class Snake:
    def __init__(self,
                 color=(255, 0, 0),
                 color_2=(200, 0, 0),
                 thickness=10,
                 speed=10,
                 delay=50,
                 direction="right"):
        '''
        Initialize object with given parameters:
            1. color - color(rgb tuple) for snake(default=(255, 0, 0) - red)
            2. color_2 - second color(rgb tuple) for snake
                            (default=(200, 0, 0) - less red)
            3. thickness - how thick it will be (default=3)
            4. speed - how fast will it move (default=5)
            5. delay - pygame delay (default=50)
            6. direction to move towards initially)(default="right")
        '''
        self.color = color
        self.color_2 = color_2
        self.thickness = thickness
        self.speed = speed
        self.coords = [
                    {"x": 220, "y":200},
                    {"x": 210, "y":200},
                    {"x": 200, "y":200},
                    {"x": 190, "y": 200},
                    {"x": 180, "y": 200}]  # snake coordinates
        self.delay = delay
        self.direction = direction



    def play(self):
        '''
        Start game
        '''
        pygame.init()
        self.window = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Let's play the game ^_^")
        run = True

        while run:
            pygame.time.delay(self.delay)

            # if X was pressed
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False


            # clear the screen
            self.window.fill((0,0,0))
            # draw the snake
            self.draw_snake()
            # breakpoint()

            # get pressed key
            keys = pygame.key.get_pressed()            
            # we care about direction keys only(yet)
            self._update_snake_coordinates(keys)

            
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
        if keys[pygame.K_RIGHT]:
            self.direction = "right"
        if keys[pygame.K_UP]:
            self.direction = "up"
        if keys[pygame.K_DOWN]:
            self.direction = "down"

        # move
        '''
            {"x": 200, "y": 200},
            {"x": 190, "y": 200},
            {"x": 180, "y": 200}]
        '''
        # do not increase each ones location separately
        # use fact that all, after first one
        # moves in its preceding points place
        # but first one moves in direction
        # that we told it to move towards

        # move from second to end points one forward
        for index in range(len(self.coords) - 1):
            self.coords[-1-index] = {**self.coords[-2-index]}
        # move head in correct direction

        if self.direction == "right":
            self.coords[0]['x'] += self.speed
        elif self.direction == "left":
            self.coords[0]['x'] -= self.speed
        elif self.direction == "up":
            self.coords[0]['y'] -= self.speed
        elif self.direction == "down":
            self.coords[0]['y'] += self.speed
        print(self.coords)
        # print(self.coords, self.direction)
        # # change direction if wall was there
        # if self.x >= 500:
        #     self.direction = "left"
        # elif self.x <= 0:
        #     # print("x < 0")
        #     self.direction = "right"
        #     # breakpoint()
        # elif self.y >= 500:
        #     # print("y >  500")
        #     self.direction = "up"
        # elif self.y <= 0:
        #     # print("y <  0")
        #     self.direction = "down"

    def draw_snake(self):
        # draw all snake points
        for index, point in enumerate(self.coords):
            pygame.draw.rect(
                self.window,
                self.color if index % 2 == 0 else self.color_2,
                (point['x'], point['y'], self.thickness, self.thickness))

    def draw_food():
        '''
            
        ''' 
        pass


# test
snake = Snake()
snake.play()