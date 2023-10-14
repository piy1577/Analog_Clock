import pygame
import numpy as np
import datetime
from Numbers import print_numbers
from Line import line
from Circle import circle

pygame.init()

screen_width, screen_height = 1920, 1080
center = (screen_width // 2, screen_height // 2)
radius = 400

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 255, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Analog Clock")

def getCoordinate(current, angle,radius):
    angle = np.deg2rad((current * angle)-90)
    return (int(center[0]+ radius*np.cos(angle)),int(center[1] + radius* np.sin(angle)))

running = True
while running:
    screen.fill(black)
    print_numbers(screen, center, radius, white) 
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            running = False
    circle(screen, center[0], center[1], radius, white)


    current_time = datetime.datetime.now()
    second = current_time.second
    minute = current_time.minute
    hour = current_time.hour
        
    hour_coordinate = getCoordinate(hour + minute/60 + second/3600, 30, 250)
    minute_coordinate = getCoordinate(minute, 6, 300)
    second_coordinate = getCoordinate(second, 6, 350)

    line(screen, center[0], center[1], hour_coordinate[0], hour_coordinate[1] ,white)
    line(screen, center[0], center[1], second_coordinate[0], second_coordinate[1] ,red)
    line(screen, center[0], center[1], minute_coordinate[0], minute_coordinate[1] ,blue)

    pygame.display.update()

pygame.quit()

