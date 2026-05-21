
# SNAKE GAME v1.0
# This file defines the interactive game entities and their local behaviors.

import pygame
import config as c


class Snake:

    def __init__(self):
        self.positions = [
            (100, 100),
            (80, 100),
            (60, 100)
        ]

        self.direction = (1, 0)

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction

        new_head = (
            head_x + dir_x * c.GRID_SIZE,
            head_y + dir_y * c.GRID_SIZE
        )

        self.positions.insert(0, new_head)
        self.positions.pop()

    def change_direction(self, new_direction):
        current_x, current_y = self.direction
        new_x, new_y = new_direction

        # impede direção oposta
        if (current_x + new_x, current_y + new_y) == (0, 0):
            return

        self.direction = new_direction

    def draw(self, screen):
        for position in self.positions:
            rect = pygame.Rect(
                position[0],
                position[1],
                c.GRID_SIZE,
                c.GRID_SIZE
            )

            pygame.draw.rect(
                screen,
                c.SNAKE_COLOR,
                rect
            )


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.rect = pygame.Rect(
            self.x,
            self.y,
            c.GRID_SIZE,
            c.GRID_SIZE
        )

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            c.FOOD_COLOR,
            self.rect
        )

    def update_position(self, x, y):
        self.x = x
        self.y = y

        self.rect.topleft = (x, y)