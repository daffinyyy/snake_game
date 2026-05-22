import pygame

import config as c

from systems import World


class Game:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(
            (c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
        )

        self.clock = pygame.time.Clock()

        self.world = World()

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.world.snake.change_direction((0, -1))

                elif event.key == pygame.K_DOWN:
                    self.world.snake.change_direction((0, 1))

                elif event.key == pygame.K_LEFT:
                    self.world.snake.change_direction((-1, 0))

                elif event.key == pygame.K_RIGHT:
                    self.world.snake.change_direction((1, 0))

        return True

    def draw(self):

        self.screen.fill(c.BACKGROUND_COLOR)

        self.world.draw(self.screen)

        pygame.display.flip()

    def run(self):

        running = True

        while running:

            running = self.handle_events()

            self.world.update()

            self.draw()

            self.clock.tick(c.FPS)

        pygame.quit()