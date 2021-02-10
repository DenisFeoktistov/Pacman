import pygame


class MenuWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        self.screen = self.main_window.screen
        self.time = self.main_window.time
        self.FPS = self.main_window.FPS

    def show(self):
        self.start_cycle()

    def start_cycle(self):
        running = True
        while running:
            self.time.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.main_window.switch_to_game()
                    return 0

            self.set_up_screen()

            self.draw_buttons()

            pygame.display.flip()

    def set_up_screen(self):
        self.screen.fill((0, 0, 0))

        self.draw_buttons()

    def draw_buttons(self):
        pass
