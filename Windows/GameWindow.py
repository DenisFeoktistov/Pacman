import pygame

from GameFiles.Game import Game
from Responders.GameWindowResponder import GameWindowResponder


class GameWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    def __init__(self):
        self.responder = GameWindowResponder(self)

        self.screen = pygame.display.set_mode(GameWindow.SIZE)
        self.game = Game(self.screen)

        self.set_font()

    def show(self):
        self.start_main_cycle()

    def start_main_cycle(self):
        time = pygame.time.Clock()

        running = True
        while running:
            time.tick(self.FPS)

            for event in pygame.event.get():
                self.game.handle(event)

                if event.type == pygame.QUIT:
                    running = False

            self.set_up_screen()

            self.game.update()
            self.game.draw(self.screen)

            pygame.display.flip()

    def set_up_screen(self):
        self.screen.fill((0, 0, 0))

        self.set_up_texts()

    def close(self):
        pygame.display.quit()

    def set_up_texts(self):
        self.set_score_text()
        self.set_time_text()
        self.set_record_text()

        self.screen.blit(self.score_text, (17, 0))
        self.screen.blit(self.time_text, (737, 0))
        self.screen.blit(self.record_time_text, (807, 60))

    def set_score_text(self):
        score = self.responder.get_score()
        self.score_text = self.font.render(f'POINTS LEFT: {score}', True, (230, 230, 250))

    def set_time_text(self):
        minutes = self.responder.get_minutes()
        seconds = self.responder.get_seconds()
        self.time_text = self.font.render(f'TIME: {str(minutes).rjust(2, "0")}:{str(seconds).rjust(2, "0")}', True,
                                          (230, 230, 250))

    def set_record_text(self):
        minutes = self.responder.get_record_minutes()
        seconds = self.responder.get_record_seconds()

        font = pygame.font.Font('data/fonts/pixel1.ttf', 20)

        self.record_time_text = font.render(
            f'RECORD TIME: {str(minutes).rjust(2, "0")}:{str(seconds).rjust(2, "0")}', True,
            (230, 230, 250))

    def set_font(self):
        self.font = pygame.font.Font('data/fonts/pixel1.ttf', 50)
