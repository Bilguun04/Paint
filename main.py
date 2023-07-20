import pygame
from pygame.locals import *
from color import *

pygame.init()
size = width, height = 720, 720
screen = pygame.display.set_mode(size)
screen.fill(white)
running = True
drawing = False
color = black
brush_size = 3

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            drawing = True
            start_pos = pygame.mouse.get_pos()
        elif event.type == MOUSEBUTTONUP:
            drawing = False

        if drawing == True:
            end_pos = pygame.mouse.get_pos()
            pygame.draw.line(screen, color, start_pos, end_pos, brush_size)
            start_pos = pygame.mouse.get_pos()

    pygame.display.update()

pygame.quit()