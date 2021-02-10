import pygame

from GameFiles.Game import Game
from Responders.GameWindowResponder import GameWindowResponder


class GameWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.screen = self.main_window.screen
        self.time = self.main_window.time
        self.FPS = self.main_window.FPS

        self.responder = GameWindowResponder(self)

        self.game = Game(self.screen)

        self.set_font()

    def show(self):
        self.restart()
        self.start_cycle()

    def start_cycle(self):
        running = True
        while running:
            self.time.tick(self.FPS)

            for event in pygame.event.get():
                self.game.handle(event)

                if event.type == pygame.QUIT:
                    running = False
                    self.main_window.switch_to_menu()
                    return 0
                if self.restart_button_clicked(event):
                    self.restart()
                if self.game.win:
                    self.responder.game_ended()

            self.set_up_screen()

            self.draw_buttons()
            self.game.update()
            self.game.draw(self.screen)

            pygame.display.flip()

    def draw_buttons(self):
        self.screen.blit(self.restart_button_pic, self.restart_button_rect)

    def restart(self):
        self.game.restart()

    def restart_button_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.restart_button_rect.collidepoint(event.pos)

    def set_up_screen(self):
        self.screen.fill((0, 0, 0))

        self.set_up_texts()
        self.set_up_buttons()

    def close(self):
        pygame.display.quit()

    def set_up_buttons(self):
        self.set_up_restart_button()

    def set_up_restart_button(self):
        self.restart_button_pic = pygame.image.load("data/pictures/buttons/restart2.png")
        self.restart_button_pic = pygame.transform.scale(self.restart_button_pic, (50, 50))
        self.restart_button_rect = self.restart_button_pic.get_rect()

        self.restart_button_rect.x = 630
        self.restart_button_rect.y = 10

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
