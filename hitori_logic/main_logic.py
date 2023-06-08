import pygame
from hitori_logic.constant_converter import return_color
from hitori_logic.button import Button

running = True
# Инициализация Pygame
pygame.init()

# Размеры окна
screen_info = pygame.display.Info()
width = screen_info.current_w * 0.5
height = screen_info.current_h * 0.5

black, white, gray = return_color()

# Создание окна
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Выбор режима")


# Функция для отображения текста на кнопке
# def draw_text(text, font, color, surface, x, y):
#     text_obj = font.render(text, True, color)
#     text_rect = text_obj.get_rect()
#     text_rect.center = (x, y)
#     surface.blit(text_obj, text_rect)


# Класс кнопки
class ButtonMainLogic(Button):

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
                    case "CLI":
                        cli()
                    case "GUI":
                        gui()


def main():
    global running
    button_width = width * 0.3
    button_height = height * 0.2
    button_x = (width - button_width) // 2
    button_y = (height - button_height) // 2

    # Создание кнопок
    button1 = ButtonMainLogic(button_x, button_y - 100, button_width, button_height, gray, white, "Разработка",
                              pygame.font.Font(None, 32), "CLI")
    button2 = ButtonMainLogic(button_x, button_y + 100, button_width, button_height, gray, white, "Игра",
                              pygame.font.Font(None, 32), "GUI")

    # Основной цикл программы
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button1.handle_event(event)
            button2.handle_event(event)
        if running:
            window.fill(black)
            button1.draw(window)
            button2.draw(window)
            pygame.display.flip()


def gui():
    from interface.GUI.menu import make_menu
    make_menu()


def cli():
    from interface.CLI import all_func
    all_func()
