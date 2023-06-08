import pygame
from pygame.locals import *
from user_solution.user_field import generate_board, return_board, return_user_board_colors
from interface.GUI.size_window import make_size, return_size
from hitori_logic.constant_converter import return_color
from interface.GUI.answer_to_user import check_win

check_button_rect = None
menu_button_rect = None
board = None
board_colors = None
BLACK, WHITE, GRAY = return_color()
FONT = None
cell_size = 0
width = 0
height = 0
size = 0


def start():
    global board, board_colors, size, FONT
    make_size()
    size = return_size()
    generate_board(size)
    board = return_board()
    board_colors = return_user_board_colors()
    pygame.init()
    FONT = pygame.font.SysFont("Arial", 30)
    pygame.display.set_caption("Хитори")
    game()


def change_color(color_background, color_number, screen, row, column):
    cell_value = board[row][column]
    cell_rect = pygame.Rect(column * cell_size, row * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, color_background, cell_rect)
    text = FONT.render(str(cell_value), True, color_number)
    text_rect = text.get_rect(center=cell_rect.center)
    screen.blit(text, text_rect)


def draw_buttons(screen):
    global check_button_rect, menu_button_rect
    button_font = pygame.font.SysFont("Arial", 20)

    check_button_rect = pygame.Rect(cell_size * size + width * 0.1, height * 0.5, width * 0.3, height * 0.2)
    pygame.draw.rect(screen, WHITE, check_button_rect)
    pygame.draw.rect(screen, BLACK, check_button_rect, 2)
    check_text = button_font.render("Проверить", True, BLACK)
    check_text_rect = check_text.get_rect(center=check_button_rect.center)
    screen.blit(check_text, check_text_rect)

    menu_button_rect = pygame.Rect(cell_size * size + width * 0.1, height * 0.9, width * 0.3, height * 0.2)
    pygame.draw.rect(screen, WHITE, menu_button_rect)
    pygame.draw.rect(screen, BLACK, menu_button_rect, 2)
    exit_text = button_font.render("Выйти в меню", True, BLACK)
    exit_text_rect = exit_text.get_rect(center=menu_button_rect.center)
    screen.blit(exit_text, exit_text_rect)


def game():
    global width, height, cell_size
    screen_info = pygame.display.Info()
    width = int(screen_info.current_w * 0.5)
    height = int(screen_info.current_h * 0.5)
    cell_size = max(width, height) // size
    window_size = (cell_size * size + width * 0.5, cell_size * size)

    screen = pygame.display.set_mode(window_size)

    for i in range(size):
        for j in range(size):
            change_color(GRAY, BLACK, screen, i, j)

    pygame.display.flip()

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
                                board_colors[i][j] = 'b'
                            # если ячейка черная, то перекрашиваем ее в белый
                            elif pixel_color == BLACK:
                                change_color(WHITE, BLACK, screen, i, j)
                                board_colors[i][j] = 'w'
                            # если ячейка белая, то перекрашиваем ее в серый
                            elif pixel_color == WHITE:
                                change_color(GRAY, BLACK, screen, i, j)
                                board_colors[i][j] = 'g'

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if check_button_rect.collidepoint(mouse_pos):
                    pygame.display.flip()
                    title_font = pygame.font.Font(None, 30)
                    title_text_color = WHITE
                    title_text = title_font.render(f"{check_win(board_colors)}", True, title_text_color)
                    title_text_rect = title_text.get_rect(center=(width * 1.25, height * 1.25))
                    screen.blit(title_text, title_text_rect)


                elif menu_button_rect.collidepoint(mouse_pos):
                    from interface.GUI.menu import make_menu
                    running = False
                    pygame.quit()
                    make_menu()

        draw_buttons(screen)

        pygame.display.flip()
