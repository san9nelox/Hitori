import pygame
from pygame.locals import *

from Field import generate_board, size


def game():
    # размеры поля

    # генерируем поле
    board = generate_board(size)

    # инициализация Pygame
    pygame.init()

    # размеры окна
    WINDOW_SIZE = (50 * size, 50 * size)

    # создаем окно
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # цвета
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)

    # шрифты
    FONT = pygame.font.SysFont("Arial", 30)

    # отображение поля
    cell_size = 50
    for i in range(size):
        for j in range(size):
            cell_value = board[i][j]
            cell_rect = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, cell_rect)
            text_surface = FONT.render(str(cell_value), True, BLACK)
            text_rect = text_surface.get_rect(center=cell_rect.center)
            screen.blit(text_surface, text_rect)

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
                            # если ячейка серая, то перекрашиваем ее в черный
                            if screen.get_at(cell_rect.center) == pygame.Color(GRAY):
                                cell_value = board[i][j]
                                pygame.draw.rect(screen, BLACK, cell_rect)
                                text = FONT.render(str(cell_value), True, WHITE)
                                text_rect = text.get_rect(center=cell_rect.center)
                                screen.blit(text, text_rect)
                            # если ячейка черная, то перекрашиваем ее в белый
                            elif screen.get_at(cell_rect.center) == pygame.Color(BLACK):
                                cell_value = board[i][j]
                                pygame.draw.rect(screen, WHITE, cell_rect)
                                text = FONT.render(str(cell_value), True, BLACK)
                                text_rect = text.get_rect(center=cell_rect.center)
                                screen.blit(text, text_rect)
                            # если ячейка белая, то перекрашиваем ее в серый
                            elif screen.get_at(cell_rect.center) == pygame.Color(WHITE):
                                cell_value = board[i][j]
                                pygame.draw.rect(screen, GRAY, cell_rect)
                                text = FONT.render(str(cell_value), True, BLACK)
                                text_rect = text.get_rect(center=cell_rect.center)
                                screen.blit(text, text_rect)

        # обновление экрана
        pygame.display.flip()

    # завершение Pygame
    pygame.quit()