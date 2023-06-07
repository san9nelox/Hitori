import pygame
from hitori_logic.constant_converter import return_color

running = True
size = 0

# Инициализация Pygame
pygame.init()

# Размеры окна
screen_info = pygame.display.Info()
width = int(screen_info.current_w * 0.5)
height = int(screen_info.current_h * 0.5)

black, white, gray = return_color()

# Создание окна
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Выбор размера поля")


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
        global running, size
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = self.hover_color
            else:
                self.color = gray
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                running = False
                size = self.value
                pygame.quit()


def make_size():
    global running, window  # Добавляем window в глобальные переменные
    button_width = width * 0.3
    button_height = height * 0.1
    button_x = (width - button_width) // 2
    button_y = (height - button_height) // 2

    # Создание кнопок
    button1 = Button(button_x, button_y - 100, button_width, button_height, gray, white, "6",
                     pygame.font.Font(None, 32), 6)
    button2 = Button(button_x, button_y - 50, button_width, button_height, gray, white, "7",
                     pygame.font.Font(None, 32), 7)
    button3 = Button(button_x, button_y, button_width, button_height, gray, white, "8",
                     pygame.font.Font(None, 32), 8)
    button4 = Button(button_x, button_y + 50, button_width, button_height, gray, white, "9",
                     pygame.font.Font(None, 32), 9)
    button5 = Button(button_x, button_y + 100, button_width, button_height, gray, white, "10",
                     pygame.font.Font(None, 32), 10)

    # Основной цикл программы
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            button1.handle_event(event)
            button2.handle_event(event)
            button3.handle_event(event)
            button4.handle_event(event)
            button5.handle_event(event)
        if running:
            window.fill(black)
            button1.draw(window)
            button2.draw(window)
            button3.draw(window)
            button4.draw(window)
            button5.draw(window)
            pygame.display.flip()


def return_size():
    global size
    return size
