# SNAKE GAME v1.0
# This file storage global constants

import pygame
import time
from systems import World
import config as c


class Game:

    def __init__(self):
        pygame.init()

        self.difficulty = "normal"
        self.apply_difficulty()

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


    def apply_difficulty(self):
        difficulty_food_count = {
            "easy": 2,
            "normal": 3,
            "hard": 5,
        }

        c.FOOD_COUNT = difficulty_food_count[self.difficulty]


    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:

                # ======================
                # MENU
                # ======================
                if self.scene == "menu":

                    if event.key == pygame.K_1:
                        self.difficulty = "easy"
                        self.apply_difficulty()

                    elif event.key == pygame.K_2:
                        self.difficulty = "normal"
                        self.apply_difficulty()

                    elif event.key == pygame.K_3:
                        self.difficulty = "hard"
                        self.apply_difficulty()

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
                        self.world.snake_1.change_direction(up)

                    elif event.key == pygame.K_DOWN:
                        self.world.snake_1.change_direction(down)

                    elif event.key == pygame.K_LEFT:
                        self.world.snake_1.change_direction(left)

                    elif event.key == pygame.K_RIGHT:
                        self.world.snake_1.change_direction(right)


                    # PLAYER 2 (WASD)

                    elif event.key == pygame.K_w:
                        self.world.snake_2.change_direction(up)

                    elif event.key == pygame.K_s:
                        self.world.snake_2.change_direction(down)

                    elif event.key == pygame.K_a:
                        self.world.snake_2.change_direction(left)

                    elif event.key == pygame.K_d:
                        self.world.snake_2.change_direction(right)



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

        self.apply_difficulty()
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

        difficulty_text = self.small_font.render(
            f"Dificuldade: {self.difficulty.title()}",
            True,
            c.WHITE
        )

        difficulty_help = self.small_font.render(
            "1 Fácil | 2 Normal | 3 Difícil",
            True,
            c.WHITE
        )

        self.screen.blit(title, title.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 - 120)))
        self.screen.blit(subtitle, subtitle.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 - 40)))

        self.screen.blit(play_text, play_text.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 + 40)))

        self.screen.blit(difficulty_text, difficulty_text.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 + 120)))
        self.screen.blit(difficulty_help, difficulty_help.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 + 160)))

        self.screen.blit(controls, controls.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 + 220)))
        self.screen.blit(controls2, controls2.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 + 260)))


    # ===================================
    # HUD
    # ===================================

    def draw_hud(self):

        pygame.draw.rect(
            self.screen,
            (50,50,50),
            (0,0,c.SCREEN_WIDTH,c.HUD_HEIGHT)
        )

        score_text = self.small_font.render(
            f"Jogador 1: {self.world.score_1}",
            True,
            c.WHITE
        )

        score2_text = self.small_font.render(
            f"Jogador 2: {self.world.score_2}",
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
        self.screen.blit(score2_text,(210,8))
        self.screen.blit(timer_text, timer_text.get_rect(topright=(c.SCREEN_WIDTH - 10, 8)))


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

        if self.world.winner == 1:
            result_message = "Jogador 1 venceu"
        elif self.world.winner == 2:
            result_message = "Jogador 2 venceu"
        else:
            result_message = "Empate"

        result_text = self.font.render(
            result_message,
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


        self.screen.blit(game_over_text, game_over_text.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 - 40)))

        self.screen.blit(result_text, result_text.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 + 10)))

        self.screen.blit(restart_text, restart_text.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 + 60)))

        self.screen.blit(quit_text, quit_text.get_rect(center=(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2 + 110)))


    def run(self):

        running = True

        while running:

            running = self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(c.FPS)

        pygame.quit()
