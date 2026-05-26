
# SNAKE GAME v1.0
# This file coordinates world state, spawning, collisions, scoring, and progression

import random
import config as c
from sprites import Snake, Food


class World:

    def __init__(self):
        self.snake = Snake()
        self.food = Food(0, 0)
        self.spawn_food()
        self.score = 0
        self.game_over = False

    def spawn_food(self):
        while True:
            x = random.randrange(
                c.GRID_SIZE * 2,
                c.SCREEN_WIDTH,
                c.GRID_SIZE
            )

            y = random.randrange(
                0,
                c.SCREEN_HEIGHT,
                c.GRID_SIZE
            )

            if (x, y) not in self.snake.positions:
                self.food.update_position(x, y)
                break

    def check_food_collision(self):
        snake_head = self.snake.positions[0]
        food_position = (
            self.food.x,
            self.food.y
        )

        if snake_head == food_position:
            self.snake.grow()
            self.score += 1
            print(self.score)  #DEBUG
            self.spawn_food()

    def check_wall_collision(self):
        head_x, head_y = self.snake.positions[0]

        #colisao habilitada
        if c.WALL_COLLISION:
            if (
                head_x < 0
                or head_x >= c.SCREEN_WIDTH
                or head_y < 0
                or head_y >= c.SCREEN_HEIGHT
            ):
                self.game_over = True
                print("wall collision")  #DEBUG
                print("GAME OVER!")

        #colisao desabilitada/modo pacman
        else:
            new_x = head_x
            new_y = head_y

            if head_x < 0:
                new_x = c.SCREEN_WIDTH - c.GRID_SIZE
            elif head_x >= c.SCREEN_WIDTH:
                new_x = 0
            if head_y < 0:
                new_y = c.SCREEN_HEIGHT - c.GRID_SIZE
            elif head_y >= c.SCREEN_HEIGHT:
                new_y = 0

            self.snake.positions[0] = (new_x, new_y)

    def check_self_collision(self):
        if not c.SELF_COLLISION:
            return

        head = self.snake.positions[0]
        body = self.snake.positions[1:]
        if head in body:
            self.game_over = True
            print("self collision")  #DEBUG
            print("GAME OVER!")  #DEBUG

    def update(self):
        if self.game_over:
            return
        
        self.snake.move()
        self.check_food_collision()
        self.check_wall_collision()
        self.check_self_collision()

    def draw(self, screen):
        self.snake.draw(screen)
        self.food.draw(screen)
