# SNAKE GAME v1.0
# This file storage global constants

import random
import pygame
import config as c
from sprites import Snake, Food


class World:

    def __init__(self):
        self.snake_1 = Snake(
            positions=[
                (100, 140),
                (80, 140),
                (60, 140)
            ],
            direction=(1, 0),
            color=c.GREEN
        )
        self.snake_2 = Snake(
            positions=[
                (700, 460),
                (720, 460),
                (740, 460)
            ],
            direction=(-1, 0),
            color=(0, 180, 255)
        )
        self.foods = []
        self.spawn_foods()
        self.score_1 = 0
        self.score_2 = 0
        self.game_over = False
        self.winner = None


    def is_position_blocked(self, position):

        return position in self.snake_1.positions or position in self.snake_2.positions or any(
            food.x == position[0] and food.y == position[1] for food in self.foods
        )


    def spawn_food(self):

        while True:

            x = random.randrange(
                0,
                c.SCREEN_WIDTH,
                c.GRID_SIZE
            )

            y = random.randrange(
                c.HUD_HEIGHT,
                c.SCREEN_HEIGHT,
                c.GRID_SIZE
            )


            if not self.is_position_blocked((x, y)):

                return Food(x, y)


    def spawn_foods(self):

        self.foods = []

        for _ in range(c.FOOD_COUNT):
            self.foods.append(self.spawn_food())


    def check_food_collision(self):

        eaten_foods = []

        for food in self.foods:
            food_position = (food.x, food.y)

            if self.snake_1.positions[0] == food_position:
                self.snake_1.grow()
                self.score_1 += 1
                eaten_foods.append(food)

            elif self.snake_2.positions[0] == food_position:
                self.snake_2.grow()
                self.score_2 += 1
                eaten_foods.append(food)

        if eaten_foods:
            for food in eaten_foods:
                self.foods.remove(food)

            for _ in range(len(eaten_foods)):
                self.foods.append(self.spawn_food())


    def handle_wall(self, snake):

        head_x, head_y = snake.positions[0]


        if c.WALL_COLLISION:

            return (
                head_x < 0
                or head_x >= c.SCREEN_WIDTH
                or head_y < 0
                or head_y >= c.SCREEN_HEIGHT
            )


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


        snake.positions[0] = (new_x, new_y)

        return False


    def check_self_collision(self, snake):

        if not c.SELF_COLLISION:
            return False


        return snake.positions[0] in snake.positions[1:]


    def check_opponent_collision(self, snake, opponent):

        return snake.positions[0] in opponent.positions


    def resolve_game_over(self, snake_1_dead, snake_2_dead):

        self.game_over = True


        if snake_1_dead and snake_2_dead:
            self.winner = 0
        elif snake_1_dead:
            self.winner = 2
        else:
            self.winner = 1


    def update(self):

        if self.game_over:
            return


        self.snake_1.move()
        self.snake_2.move()

        snake_1_dead = self.handle_wall(self.snake_1)
        snake_2_dead = self.handle_wall(self.snake_2)

        if not snake_1_dead:
            snake_1_dead = self.check_self_collision(self.snake_1)

        if not snake_2_dead:
            snake_2_dead = self.check_self_collision(self.snake_2)

        if not snake_1_dead:
            snake_1_dead = self.check_opponent_collision(self.snake_1, self.snake_2)

        if not snake_2_dead:
            snake_2_dead = self.check_opponent_collision(self.snake_2, self.snake_1)

        if snake_1_dead or snake_2_dead:
            self.resolve_game_over(snake_1_dead, snake_2_dead)
            return

        self.check_food_collision()


    def draw(self, screen):

        grid_color = (42, 42, 42)

        for x in range(0, c.SCREEN_WIDTH, c.GRID_SIZE):
            pygame.draw.line(
                screen,
                grid_color,
                (x, c.HUD_HEIGHT),
                (x, c.SCREEN_HEIGHT)
            )

        for y in range(c.HUD_HEIGHT, c.SCREEN_HEIGHT, c.GRID_SIZE):
            pygame.draw.line(
                screen,
                grid_color,
                (0, y),
                (c.SCREEN_WIDTH, y)
            )

        self.snake_1.draw(screen)
        self.snake_2.draw(screen)

        for food in self.foods:
            food.draw(screen)
