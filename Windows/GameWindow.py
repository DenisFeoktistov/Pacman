import pygame


class GameWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600

    def __init__(self, main_interface_class):
        self.main_interface_class = main_interface_class

    def set_responder(self, responder):
        self.responder = responder

    def show(self):
        screen = pygame.display.set_mode(GameWindow.SIZE)

        self.set_up_screen(screen)

        self.start_main_cycle(screen)

    def start_main_cycle(self, screen):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()

    def set_up_screen(self, screen):
        screen.fill((0, 0, 0))

    def close(self):
        pass
