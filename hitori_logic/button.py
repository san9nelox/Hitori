import pygame
from hitori_logic.constant_converter import return_color

black, white, gray = return_color()


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


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
