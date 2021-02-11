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

        self.running = False

    def show(self):
        self.restart()
        self.start_cycle()

    def start_cycle(self):
        self.running = True
        while self.running:
            self.time.tick(self.FPS)
            self.set_up_screen()

            self.draw_buttons()
            self.game.update()
            self.game.draw(self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                self.game.handle(event)

                if event.type == pygame.QUIT:
                    self.running = False
                    self.main_window.switch_to_menu()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons_click_check(event.pos)
                if self.game.win:
                    self.responder.game_ended()

    def draw_buttons(self):
        self.screen.blit(self.restart_button_pic, self.restart_button_rect)
        self.screen.blit(self.home_button_pic, self.home_button_rect)

    def restart(self):
        self.game.restart()

    def buttons_click_check(self, mouse_pos):
        if self.restart_button_rect.collidepoint(mouse_pos):
            self.restart()
        if self.home_button_rect.collidepoint(mouse_pos):
            self.running = False
            self.main_window.switch_to_menu()

    def set_up_screen(self):
        self.screen.fill((0, 0, 0))

        self.set_up_texts()
        self.set_up_buttons()

    def close(self):
        pygame.display.quit()

    def set_up_buttons(self):
        self.set_up_restart_button()
        self.set_up_home_button()

    def set_up_home_button(self):
        self.home_button_pic = pygame.image.load("data/pictures/buttons/menu1.png")
        self.home_button_pic = pygame.transform.scale(self.home_button_pic, (40, 37))
        self.home_button_rect = self.home_button_pic.get_rect()

        self.home_button_rect.x = 67
        self.home_button_rect.y = 55

    def set_up_restart_button(self):
        self.restart_button_pic = pygame.image.load("data/pictures/buttons/restart3.png")
        self.restart_button_pic = pygame.transform.scale(self.restart_button_pic, (40, 37))
        self.restart_button_rect = self.restart_button_pic.get_rect()

        self.restart_button_rect.x = 17
        self.restart_button_rect.y = 55

    def set_up_texts(self):
        self.set_score_text()
        self.set_time_text()
        self.set_record_text()
        if self.game.win:
            self.set_win_text()
            self.screen.blit(self.win_text, (440, 0))

            if self.responder.is_record():
                self.set_new_record_text()
                self.screen.blit(self.new_record_text, (450, 50))

        self.screen.blit(self.score_text, (17, 0))
        self.screen.blit(self.time_text, (737, 0))
        self.screen.blit(self.record_time_text, (807, 60))

    def set_new_record_text(self):
        font = pygame.font.Font('data/fonts/pixel1.ttf', 30)
        self.new_record_text = font.render(f'New record!', True, (230, 230, 250))

    def set_win_text(self):
        self.win_text = self.font.render(f'You win!', True, (230, 230, 250))

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
