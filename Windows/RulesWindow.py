import pygame


class RulesWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.screen = self.main_window.screen
        self.time = self.main_window.time
        self.FPS = self.main_window.FPS

        self.set_background()
        self.set_font()
        self.set_back_button()
        self.set_text()

        self.running = False

    def set_text(self):
        self.strings = list()
        text = "Приветсвуем Вас в игре 'Pacman'! Вы играете за\n " \
               "пакмена, Ваша цель - собрать все звезды за наименьшее\n" \
               " количество времени. Но попасть в таблицу лидеров Вам\n" \
               "будут мешать приведения, которых мы старательно \n" \
               "настраивали :) Как видите, все достаточно просто.\n Удачи!"
        for i, string in enumerate(text.split("\n")):
            string_text = self.font.render(string, False, (255, 255, 255))
            string_rect = string_text.get_rect()
            string_rect.center = (self.main_window.WIDTH // 2, self.main_window.HEIGHT - 200 - 50 * (5 - i))
            self.strings.append((string_text, string_rect))

    def draw_text(self):
        for string in self.strings:
            self.screen.blit(string[0], string[1])

    def show(self):
        self.start_cycle()

    def start_cycle(self):
        self.running = True
        while self.running:
            self.time.tick(self.FPS)

            self.set_up_screen()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.buttons_click_check(event.pos)

    def buttons_click_check(self, mouse_pos):
        if self.back_button.collidepoint(mouse_pos):
            self.running = False
            self.main_window.switch_to_menu()

    def set_up_screen(self):
        self.screen.fill((0, 0, 0))

        self.draw_background()
        self.draw_back_button()
        self.draw_text()

    def draw_background(self):
        self.screen.blit(self.background_photo, self.background_rect)

    def set_background(self):
        self.background_photo = pygame.image.load('data/pictures/backgrounds/purple_background1.jpg')
        self.background_photo = pygame.transform.scale(
            self.background_photo, (self.main_window.WIDTH, self.main_window.HEIGHT))
        self.background_rect = self.background_photo.get_rect()

    def draw_back_button(self):
        self.screen.blit(self.text_back, self.back_button)

    def set_font(self):
        self.font = pygame.font.Font('data/fonts/pixel1.ttf', 30)

    def set_back_button(self):
        font = pygame.font.Font('data/fonts/pixel1.ttf', 40)
        self.text_back = font.render('Вернуться', False, (255, 255, 255))
        self.back_button = self.text_back.get_rect()
        self.back_button.center = (self.main_window.WIDTH // 2, self.main_window.HEIGHT - 50)
