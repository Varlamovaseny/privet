import pygame
import sys

W, H = 400, 400
collide = False
n = 0
# квадрат
rect_size = w, h = 70, 70
rect_pos = ((W - w) // 2, (H - h) // 2)
# круг
circle_radius = 35
circle_pos = (0, 0)
# цвет
RED = (200, 0, 180)
BLUE = (0, 0, 180)
YELLOW = (250, 250, 180)
BG = (128, 128, 128)

pygame.init()
pygame.display.set_caption('DRAW and COLLIDE')
screen = pygame.display.set_mode((W, H))
font = pygame.font.Font(None, 32)



# на созданой поверхности рисуем круг желтого цвета
surface = pygame.Surface((circle_radius * 2, circle_radius * 2), pygame.SRCALPHA)
pygame.draw.circle(surface, YELLOW, (circle_radius, circle_radius), circle_radius)
# находим рект у поверхности
rect1 = surface.get_rect()

ball = pygame.image.load('ball.png')
ball_rect = ball.get_rect() 

# создаем поверхность размеров в 2-а раза больше радиуса круга и вкл. альфа-канал
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
        elif e.type == pygame.MOUSEMOTION:
            # circle_pos = e.pos
            rect1.center = e.pos

    screen.fill(BG)

    COLOR = RED if collide else BLUE
    # rect1 = pygame.draw.circle(screen, YELLOW, circle_pos, circle_radius)
    rect2 = pygame.draw.rect(screen, RED if collide else BLUE, (rect_pos, rect_size))
    screen.blit(surface, rect1)

    if rect1.colliderect(rect2):  # столкновение
        collide = True
        if COLOR == BLUE:
            n += 1
    else:
        collide = False

    screen.blit(font.render(str(n), 1, RED), (10, 10))
    pygame.display.update()