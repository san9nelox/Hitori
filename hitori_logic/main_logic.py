import pygame

running = True
# Инициализация Pygame
pygame.init()

# Размеры окна
screen_info = pygame.display.Info()
width = screen_info.current_w * 0.5
height = screen_info.current_h * 0.5

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

# Создание окна
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Выбор режима")


# Функция для отображения текста на кнопке
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


# Класс кнопки
class Button:
    def __init__(self, x, y, w, h, color, hover_color, text, font, value):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.font = font
        self.value = value

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(self.text, self.font, black, surface, self.rect.centerx, self.rect.centery)

    def handle_event(self, event):
        global running
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
            else:
                self.color = gray
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                match self.value:
                    case "CLI":
                        running = False
                        pygame.quit()
                        cli()
                    case "GUI":
                        running = False
                        pygame.quit()
                        gui()


def main():
    global running
    button_width = width * 0.3
    button_height = height * 0.2
    button_x = (width - button_width) // 2
    button_y = (height - button_height) // 2

    # Создание кнопок
    button1 = Button(button_x, button_y - 100, button_width, button_height, gray, white, "Разработка",
                     pygame.font.Font(None, 32), "CLI")
    button2 = Button(button_x, button_y + 100, button_width, button_height, gray, white, "Игра",
                     pygame.font.Font(None, 32), "GUI")

    # Основной цикл программы
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button1.handle_event(event)
            button2.handle_event(event)

        window.fill(black)
        button1.draw(window)
        button2.draw(window)
        pygame.display.flip()


def gui():
    print('Doesn\'t work')
    # from interface.GUI import game
    # game()


def cli():
    from interface.CLI import all_func
    all_func()
