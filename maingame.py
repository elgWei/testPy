# основа
import pygame
import random
FPS = 30

# создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("elegy")
clock = pygame.time.Clock()

#цвет
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Рендеринг
screen.fill(WHITE)
# после отрисовки всего, переворачиваем экран
pygame.display.flip()
#цикл игры
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

change = True

pygame.quit()
