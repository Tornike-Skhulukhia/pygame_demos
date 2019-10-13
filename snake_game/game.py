'''
    Define OOP method to play 
    simple snake game.
'''
import pygame
import random

# define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Snake:
    def __init__(self,
                 color=BLUE,
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

        # color to make snake parts more visible
        color_2 = [0, 0, 0]
        color_2[color.index(255)] = 255 - 55 # 10 - color difference
        self.color_2 = tuple(color_2)
        # print(self.color_2)

        self.thickness = thickness
        self.speed = speed
        self.coords = [
                    # {"x": 300, "y":200},
                    # {"x": 310, "y": 200},
                    {"x": 320, "y": 200}]  # snake coordinates
        self.delay = delay
        self.direction = direction
        self.food_location = None



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
            self.draw_game()
            # breakpoint()

            # get pressed key
            keys = pygame.key.get_pressed()            
            # we care about direction keys only(yet)
            self._update_snake_coordinates(keys)
            self.handle_food_eating()
            
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

        print(self.coords, self.direction)
        # move from another side wall if needed
        if self.coords[0]['x'] >= 500:
            # self.direction = "left"
            self.coords[0]['x'] = -10
            # print(self.coords, self.direction)
            # breakpoint()

        elif self.coords[0]['x'] <= -10:
            # self.direction = "right"
            self.coords[0]['x'] = 500
        elif self.coords[0]['y'] >= 500:
            # self.direction = "up"
            self.coords[0]['y'] = -10
        elif self.coords[0]['y'] <= -10:
            # self.direction = "down"
            self.coords[0]['y'] = 500
        # breakpoint()

    def draw_game(self):
        # draw all snake points
        for index, point in enumerate(self.coords):
            pygame.draw.rect(
                self.window,
                self.color if index % 2 == 0 else self.color_2,
                (point['x'], point['y'], self.thickness, self.thickness))

        self.draw_food()            


    def _get_random_color(self):
        '''
        get random rgb value tuple        
        '''
        return random.sample(range(0, 255, 10), 3)

    def _get_food_location(self):
        '''
        returns new random food location(excluding snake points)
        '''
        location = {
            "x": random.choice(range(0, 500, self.speed)),
            "y": random.choice(range(0, 500, self.speed)),
        }

        # breakpoint()
        while location['x'] in [p['x'] for p in self.coords]:
            location['x'] = random.choice(range(0, 500, self.speed))

        while location['y'] in [p['y'] for p in self.coords]:
            location['y'] = random.choice(range(0, 500, self.speed))

        return location


    def draw_food(self):
        '''
            draw food in random places(beside our snake body).
            food will have same width & height as snake.
        ''' 
        if self.food_location is None:
            self.food_color = self._get_random_color()
            self.food_location = self._get_food_location()

        # draw food
        pygame.draw.rect(
            self.window,
            self.food_color,
            (self.food_location['x'],
             self.food_location['y'],
             self.thickness,
             self.thickness))

    def handle_food_eating(self):
        '''
        update things if food was eaten
        '''
        # if we are at exact food location
        if (self.food_location['x'] == self.coords[0]['x']
            and self.food_location['y'] == self.coords[0]['y']):
            self.coords.insert(0, self.food_location)
            self.food_location = None

            # test - changes snake color too eaten food color
            # self.color = self.food_color
            self.speed += 10





# test
snake = Snake()
snake.play()