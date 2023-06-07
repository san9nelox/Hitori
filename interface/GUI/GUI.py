import pygame
from pygame.locals import *
from user_solution.user_field import generate_board, return_board
from interface.GUI.size_window import make_size, return_size, width, height
from hitori_logic.constant_converter import return_color

make_size()
size = return_size()
generate_board(size)
board = return_board()

BLACK, WHITE, GRAY = return_color()

# инициализация Pygame
pygame.init()

# шрифты
FONT = pygame.font.SysFont("Arial", 30)
# отображение поля
cell_size = max(width, height) // size
pygame.display.set_caption("Хитори")


def change_color(color_background, color_number, screen, row, column):
    cell_value = board[row][column]
    cell_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, color_background, cell_rect)
    text = FONT.render(str(cell_value), True, color_number)
    text_rect = text.get_rect(center=cell_rect.center)
    screen.blit(text, text_rect)


def game():
    # размеры окна
    window_size = (cell_size * size + width * 0.5, cell_size * size)

    # создаем окно
    screen = pygame.display.set_mode(window_size)

    for i in range(size):
        for j in range(size):
            change_color(GRAY, BLACK, screen, i, j)

    # обновление экрана
    pygame.display.flip()

    # игровой цикл
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN:
                # получаем координаты клика
                mouse_pos = pygame.mouse.get_pos()
                # проверяем, на какую ячейку был сделан клик
                for i in range(size):
                    for j in range(size):
                        cell_rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                        if cell_rect.collidepoint(mouse_pos):
                            # получаем цвет пикселя в левом верхнем углу ячейки
                            pixel_color = screen.get_at((j * cell_size, i * cell_size))
                            # если ячейка серая, то перекрашиваем ее в черный
                            if pixel_color == GRAY:
                                change_color(BLACK, WHITE, screen, i, j)
                            # если ячейка черная, то перекрашиваем ее в белый
                            elif pixel_color == BLACK:
                                change_color(WHITE, BLACK, screen, i, j)
                            # если ячейка белая, то перекрашиваем ее в серый
                            elif pixel_color == WHITE:
                                change_color(GRAY, BLACK, screen, i, j)

        pygame.display.flip()

    pygame.quit()
