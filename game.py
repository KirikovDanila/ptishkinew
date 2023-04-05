#Импортирование модулей
import pygame
import sys
from pygame.locals import QUIT

#Инициализирование модулей pugame
pygame.init()

#Определение основных свойств игры
SPEED = 30
Frames = pygame.time.Clock()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

BACKGROUND_COLOR = (25, 25, 150)

#Инициализация графического интерфейса
pygame.display.set_caption('Flappy bird')

screen_surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#Сущности игры
class Bird:
    def __init__(self) -> None:
        # Тут описываем все свойства для птички
        self.image = pygame.image.load('birdik.png')
        self.rect = self.image.get_rect()
#Движок игры
while True:
    #1)выйти из движка 2)повторяюмые операции
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Блок обновления данных


    #Блок отрисовки
    screen_surface.fill(BACKGROUND_COLOR)
    pygame.display.update()
    Frames.tick(SPEED)