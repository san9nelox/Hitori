import pygame
from hitori_logic.constant_converter import return_color
from hitori_logic.button import Button
from interface.GUI.menu import make_menu
from settings.diagonal_neighbors import are_horiz_neigh_diff

running = True
black, white, gray = return_color()


class ButtonSettings(Button):
    def draw(self, surface):
        Button.draw(self, surface)

    def handle_event(self, event):
        global running, are_horiz_neigh_diff
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
                    case 'on':
                        are_horiz_neigh_diff = True
                    case 'off':
                        are_horiz_neigh_diff = False

                make_menu()


def make_settings():
    global running
    running = True

    pygame.init()

    screen_info = pygame.display.Info()
    width = int(screen_info.current_w * 0.5)
    height = int(screen_info.current_h * 0.5)

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Настройки")

    button_width = width * 0.3
    button_height = height * 0.1
    button_x = (width - button_width) // 2
    button_y = (height - button_height) // 2

    title_font = pygame.font.Font(None, 48)
    title_text_color = white

    button_on = ButtonSettings(button_x, button_y - 50, button_width, button_height, gray, white, 'Включить',
                               pygame.font.Font(None, 32), 'on')
    button_off = ButtonSettings(button_x, button_y, button_width, button_height, gray, white, 'Выключить',
                                pygame.font.Font(None, 32), 'off')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button_on.handle_event(event)
            button_off.handle_event(event)
        if running:
            window.fill(black)

            title_text = title_font.render(f"Правило диагональных соседей {check_rule()}", True, title_text_color)
            title_text_rect = title_text.get_rect(center=(width // 2, height // 4))
            window.blit(title_text, title_text_rect)

            button_on.draw(window)
            button_off.draw(window)
            pygame.display.flip()


def check_rule():
    if are_horiz_neigh_diff:
        return 'включено'
    return 'выключено'
