import pygame


class MenuWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.screen = self.main_window.screen
        self.time = self.main_window.time
        self.FPS = self.main_window.FPS

        self.set_background()
        self.set_font()
        self.set_buttons()

    def show(self):
        self.start_cycle()

    def start_cycle(self):
        running = True
        while running:
            self.time.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons_click_check(event.pos)

            self.set_up_screen()

            pygame.display.flip()

    def set_buttons(self):
        self.set_play_button()
        self.set_rules_button()

    def buttons_click_check(self, mouse_pos):
        if self.play_button.collidepoint(mouse_pos):
            self.main_window.switch_to_game()
        if self.rules_button.collidepoint(mouse_pos):
            self.main_window.switch_to_rules()

    def set_up_screen(self):
        self.screen.fill((0, 0, 0))
        self.draw_background()
        self.draw_buttons()

    def draw_background(self):
        self.screen.blit(self.background_photo, self.background_rect)

    def set_background(self):
        self.background_photo = pygame.image.load('data/pictures/backgrounds/purple_background1.jpg')
        self.background_photo = pygame.transform.scale(
            self.background_photo, (self.main_window.WIDTH, self.main_window.HEIGHT))
        self.background_rect = self.background_photo.get_rect()

    def draw_buttons(self):
        self.screen.blit(self.text_rules, self.rules_button)
        self.screen.blit(self.text_play, self.play_button)

    def set_play_button(self):
        self.text_play = self.font.render('Играть', False, (255, 255, 255))
        self.play_button = self.text_play.get_rect()
        self.play_button.center = (self.main_window.WIDTH // 2, self.main_window.HEIGHT // 4)

    def set_rules_button(self):
        self.text_rules = self.font.render('Правила', False, (255, 255, 255))
        self.rules_button = self.text_rules.get_rect()
        self.rules_button.center = (self.main_window.WIDTH // 2, self.main_window.HEIGHT // 3)

    def set_font(self):
        self.font = pygame.font.Font('data/fonts/pixel1.ttf', 40)
