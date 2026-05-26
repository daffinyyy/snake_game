# SNAKE GAME v1.0
# This file storage global constants

import pygame
import time
from systems import World
import config as c


class Game:

    def __init__(self):
        pygame.init()

        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 30)
        self.title_font = pygame.font.SysFont(None, 72)

        self.screen = pygame.display.set_mode(
            (c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
        )

        self.clock = pygame.time.Clock()
        self.world = World()

        self.scene = "menu"

        self.start_time = 0


    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                # ======================
                # MENU
                # ======================
                if self.scene == "menu":

                    if event.key == pygame.K_RETURN:
                        self.restart()


                # ======================
                # GAME
                # ======================
                elif self.scene == "play":

                    up = (0, -1)
                    down = (0, 1)
                    left = (-1, 0)
                    right = (1, 0)

                    # PLAYER 1 (setas)

                    if event.key == pygame.K_UP:
                        self.world.snake.change_direction(up)

                    elif event.key == pygame.K_DOWN:
                        self.world.snake.change_direction(down)

                    elif event.key == pygame.K_LEFT:
                        self.world.snake.change_direction(left)

                    elif event.key == pygame.K_RIGHT:
                        self.world.snake.change_direction(right)


                    # PLAYER 2 (WASD)

                    elif event.key == pygame.K_w:
                        self.world.snake.change_direction(up)

                    elif event.key == pygame.K_s:
                        self.world.snake.change_direction(down)

                    elif event.key == pygame.K_a:
                        self.world.snake.change_direction(left)

                    elif event.key == pygame.K_d:
                        self.world.snake.change_direction(right)



                # ======================
                # GAME OVER
                # ======================

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

        self.start_time = time.time()


    def draw(self):

        self.screen.fill(c.BACKGROUND_COLOR)

        if self.scene == "menu":
            self.draw_menu()

        elif self.scene == "play":
            self.draw_game()

        elif self.scene == "game_over":
            self.draw_game_over()

        pygame.display.flip()


    # ===================================
    # MENU
    # ===================================

    def draw_menu(self):

        title = self.title_font.render(
            "SNAKE GAME",
            True,
            c.GREEN
        )

        subtitle = self.font.render(
            "MULTIPLAYER",
            True,
            c.WHITE
        )

        play_text = self.small_font.render(
            "Pressione ENTER para jogar",
            True,
            c.WHITE
        )

        controls = self.small_font.render(
            "Player 1: SETAS",
            True,
            c.WHITE
        )

        controls2 = self.small_font.render(
            "Player 2: W A S D",
            True,
            c.WHITE
        )


        self.screen.blit(title, (220,120))
        self.screen.blit(subtitle,(280,200))

        self.screen.blit(play_text,(260,300))

        self.screen.blit(controls,(280,420))
        self.screen.blit(controls2,(290,460))


    # ===================================
    # HUD
    # ===================================

    def draw_hud(self):

        pygame.draw.rect(
            self.screen,
            (50,50,50),
            (0,0,c.SCREEN_WIDTH,40)
        )

        score_text = self.small_font.render(
            f"Score: {self.world.score}",
            True,
            c.WHITE
        )


        elapsed = int(time.time() - self.start_time)

        minutes = elapsed // 60
        seconds = elapsed % 60


        timer_text = self.small_font.render(
            f"Tempo: {minutes:02}:{seconds:02}",
            True,
            c.WHITE
        )


        self.screen.blit(score_text,(10,8))
        self.screen.blit(timer_text,(650,8))


    # ===================================
    # GAME
    # ===================================

    def draw_game(self):

        self.world.draw(self.screen)

        self.draw_hud()



    # ===================================
    # GAME OVER
    # ===================================

    def draw_game_over(self):

        game_over_text = self.font.render(
            "GAME OVER",
            True,
            c.WHITE
        )

        restart_text = self.font.render(
            "Pressione R para reiniciar",
            True,
            c.WHITE
        )

        quit_text = self.font.render(
            "ESC para sair",
            True,
            c.WHITE
        )


        self.screen.blit(
            game_over_text,
            (295,240)
        )

        self.screen.blit(
            restart_text,
            (190,280)
        )

        self.screen.blit(
            quit_text,
            (290,320)
        )


    def run(self):

        running = True

        while running:

            running = self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(c.FPS)

        pygame.quit()
