import pygame
from hitori_logic.constant_converter import return_color
from hitori_logic.button import Button

running = True
black, white, gray = return_color()


class ButtonMenu(Button):
    def draw(self, surface):
        Button.draw(self, surface)

    def handle_event(self, event):
        global running
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
            else:
                self.color = gray
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                running = False
                pygame.quit()
                match self.value:
                    case "play":
                        play_func()
                    case "settings":
                        settings_func()
                    case "exit":
                        exit_func()


def make_menu():
    global running
    running = True

    pygame.init()

    screen_info = pygame.display.Info()
    width = int(screen_info.current_w * 0.5)
    height = int(screen_info.current_h * 0.5)

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Меню")

    button_width = width * 0.3
    button_height = height * 0.1
    button_x = (width - button_width) // 2
    button_y = (height - button_height) // 2

    button_play = ButtonMenu(button_x, button_y - 100, button_width, button_height, gray, white, 'Играть',
                             pygame.font.Font(None, 32), 'play')
    button_settings = ButtonMenu(button_x, button_y - 50, button_width, button_height, gray, white, 'Настройки',
                                 pygame.font.Font(None, 32), 'settings')
    button_exit = ButtonMenu(button_x, button_y, button_width, button_height, gray, white, 'Выход',
                             pygame.font.Font(None, 32), 'exit')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_play.handle_event(event)
            button_settings.handle_event(event)
            button_exit.handle_event(event)
        if running:
            window.fill(black)
            button_play.draw(window)
            button_settings.draw(window)
            button_exit.draw(window)
            pygame.display.flip()


def play_func():
    from interface.GUI.game import start
    start()


def settings_func():
    from interface.GUI.settings import make_settings
    make_settings()


def exit_func():
    exit()
