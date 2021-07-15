import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Cubes Game")

x = 50
y = 435
widht = 40
height = 60
speed = 5

isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - widht - 5:
        x += speed
    if not(isJump):
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        if keys[pygame.K_DOWN] and y < 500 - height - 5:
            y += speed
        if keys[pygame.K_SPACE]:
            isJump = True

    win.fill((26, 0, 13))
    pygame.draw.rect(win, (170, 128, 255), (x, y, widht, height))
    pygame.display.update()

pygame.quit()