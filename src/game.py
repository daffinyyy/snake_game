
# SNAKE GAME v1.0
# This file manages the application loop, scenes, input handling, and screen drawing.

import pygame
from sprites import Snake
import config as c


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                up = (0, -1)
                down = (0, 1)
                left = (-1, 0)
                right = (1, 0)

                if event.key == pygame.K_UP:
                    self.snake.change_direction(up)

                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction(down)

                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction(left)

                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction(right)

        return True

    def update(self):
        self.snake.move()

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.snake.draw(self.screen)
        pygame.display.flip()

    def run(self):
        running = True

        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

        pygame.quit()