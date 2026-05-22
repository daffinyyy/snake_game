
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

    def spawn_food(self):
        while True:
            x = random.randrange(
                0,
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
            print(self.score)
            self.spawn_food()

    def update(self):
        self.snake.move()
        self.check_food_collision()

    def draw(self, screen):
        self.snake.draw(screen)
        self.food.draw(screen)