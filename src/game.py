
# SNAKE GAME v1.0
# This file manages the application loop, scenes, input handling, and screen drawing.

import pygame
from systems import World
import config as c


class Game:

    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont(None, 48)
        self.screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.world = World()
        self.scene = "game_over"

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if self.scene == "play":
                    up = (0, -1)
                    down = (0, 1)
                    left = (-1, 0)
                    right = (1, 0)

                    if event.key == pygame.K_UP:
                        self.world.snake.change_direction(up)
                        print("cima")   #DEBUG

                    elif event.key == pygame.K_DOWN:
                        self.world.snake.change_direction(down)
                        print("baixo")   #DEBUG

                    elif event.key == pygame.K_LEFT:
                        self.world.snake.change_direction(left)
                        print("esquerda")   #DEBUG

                    elif event.key == pygame.K_RIGHT:
                        self.world.snake.change_direction(right)
                        print("direita")   #DEBUG

                elif self.scene == "game_over":
                    if event.key == pygame.K_r:
                        self.restart()
                    elif event.key == pygame.K_ESCAPE:
                        return False

        return True

    def update(self):
        if self.scene == "play":
            self.world.update()

            if self.world.game_over:
                self.scene = "game_over"

    def restart(self):
        self.world = World()
        self.scene = "play"

    def draw(self):
        self.screen.fill(c.BACKGROUND_COLOR)

        if self.scene == "play":
            self.draw_game()
        elif self.scene == "game_over":
            self.draw_game_over()

        pygame.display.flip()

    def draw_game(self):
        self.world.draw(self.screen)

    def draw_game_over(self):
        #textos
        game_over_text = self.font.render("GAME OVER", True, c.WHITE)
        restart_text = self.font.render("Pressione R para reiniciar", True, c.WHITE)
        quit_text = self.font.render("ESC para sair", True, c.WHITE)

        #posicionando
        self.screen.blit(game_over_text, (295, 240))
        self.screen.blit(restart_text, (190, 280))
        self.screen.blit(quit_text,(290, 320))

    def run(self):
        running = True

        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

        pygame.quit()