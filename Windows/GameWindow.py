import pygame


from GameFiles.Game import Game


class GameWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    def __init__(self, main_interface_class):
        self.main_interface_class = main_interface_class

        self.create_pause_button()

        self.paused = False

    def set_responder(self, responder):
        self.responder = responder

    def show(self):
        screen = pygame.display.set_mode(GameWindow.SIZE)
        game = Game(screen)

        self.set_up_screen(screen)

        self.start_main_cycle(screen, game)

    def start_main_cycle(self, screen, game):
        time = pygame.time.Clock()
        running = True
        while running:
            if not self.paused:
                time.tick(self.FPS)
                for event in pygame.event.get():
                    game.handle(event)
                    if event.type == pygame.QUIT:
                        running = False
                    if self.pause_check(event):
                        self.paused = True
                        self.responder.pause()
                self.set_up_screen(screen)
                game.update()
                game.draw(screen)
                pygame.display.flip()
            else:
                return 0

    def set_up_screen(self, screen):
        screen.fill((0, 0, 0))

        self.show_pause(screen)

    def show_pause(self, screen):
        screen.blit(self.pause_surface, self.pause_rect)

    def create_pause_button(self):
        self.pause_surface = pygame.image.load('data/pictures/pause/pause4.png')
        self.pause_surface = pygame.transform.scale(self.pause_surface, (160, 45))
        self.pause_rect = self.pause_surface.get_rect()

        self.pause_rect.x = 825
        self.pause_rect.y = 27

    def pause_check(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            return self.pause_rect.collidepoint(mouse_pos)

    def close(self):
        pygame.display.quit()
