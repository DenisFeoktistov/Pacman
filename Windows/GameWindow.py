import pygame


from GameFiles.Game import Game


class GameWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    def __init__(self, main_interface):
        self.main_interface = main_interface
        
        self.create_menu_button()

    def set_responder(self, responder):
        self.responder = responder

    def show(self):
        screen = pygame.display.set_mode(GameWindow.SIZE)
        game = Game(screen)

        self.set_up_screen(screen)

        self.start_main_cycle(screen, game)

    def start_main_cycle(self, screen, game):
        print(1)
        time = pygame.time.Clock()
        running = True
        while running:
            time.tick(self.FPS)
            for event in pygame.event.get():
                game.handle(event)
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.button_clicked_check(event)
            self.set_up_screen(screen)
            game.update()
            game.draw(screen)
            pygame.display.flip()

    def button_clicked_check(self, event):
        mouse_pos = event.pos
        if self.menu_rect.collidepoint(mouse_pos):
            self.main_interface.from_game_to_menu()

    def set_up_screen(self, screen):
        screen.fill((0, 0, 0))

        self.show_menu_button(screen)

    def show_menu_button(self, screen):
        screen.blit(self.menu_surface, self.menu_rect)

    def create_menu_button(self):
        self.menu_surface = pygame.image.load('data/pictures/menu_button/menu4.png')
        self.menu_surface = pygame.transform.scale(self.menu_surface, (160, 45))
        self.menu_rect = self.menu_surface.get_rect()

        self.menu_rect.x = 825
        self.menu_rect.y = 27

    def close(self):
        pygame.display.quit()
