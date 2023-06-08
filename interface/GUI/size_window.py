import pygame
from hitori_logic.constant_converter import return_color
from hitori_logic.button import Button

running = True
size = 0
width = 0
height = 0
black, white, gray = return_color()


class ButtonSizeWindow(Button):
    def draw(self, surface):
        Button.draw(self, surface)

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
    global running, width, height
    running = True

    pygame.init()

    screen_info = pygame.display.Info()
    width = int(screen_info.current_w * 0.5)
    height = int(screen_info.current_h * 0.5)

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Выбор размера поля")

    button_width = width * 0.3
    button_height = height * 0.1
    button_x = (width - button_width) // 2
    button_y = (height - button_height) // 2

    button1 = ButtonSizeWindow(button_x, button_y - 100, button_width, button_height, gray, white, "6",
                               pygame.font.Font(None, 32), 6)
    button2 = ButtonSizeWindow(button_x, button_y - 50, button_width, button_height, gray, white, "7",
                               pygame.font.Font(None, 32), 7)
    button3 = ButtonSizeWindow(button_x, button_y, button_width, button_height, gray, white, "8",
                               pygame.font.Font(None, 32), 8)
    button4 = ButtonSizeWindow(button_x, button_y + 50, button_width, button_height, gray, white, "9",
                               pygame.font.Font(None, 32), 9)
    button5 = ButtonSizeWindow(button_x, button_y + 100, button_width, button_height, gray, white, "10",
                               pygame.font.Font(None, 32), 10)

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
