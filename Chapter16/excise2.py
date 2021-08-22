import pygame
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('./img/wackyball.bmp')
x = 50
y = 50
x_speed = 10
y_speed = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(30)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 90, 90], 0)
    x = x + x_speed
    y = y + y_speed
    if x > screen.get_width() - 30 or x < 0:
        x_speed = - x_speed
    if y > screen.get_height() - 30 or y < 0:
        y_speed = - y_speed
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()
