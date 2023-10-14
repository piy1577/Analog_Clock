import pygame
import numpy as np

def print_numbers(screen, center, radius, color):
    font = pygame.font.SysFont("Arial", 80, True, False)
    for i in range (1, 13):
        text = font.render(str(i), True, color)
        angle = np.deg2rad((i * 30)- 90) 
        text_rect = text.get_rect(center = (int(center[0] + (radius- 40)*np.cos(angle)), int(center[1] + (radius- 40)*np.sin(angle))))
        screen.blit(text, text_rect)
