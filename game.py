import pygame

pygame.init()

size = (winWidht, winHeight) = (900, 420) 
win = pygame.display.set_mode(size)

pygame.display.set_caption("Cubes Game")

walkRight = [pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_1.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_2.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_3.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_4.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_5.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_6.png')]
walkLeft = [pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_Left_1.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_Left_2.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_Left_3.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_Left_4.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_Left_5.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Walk_Left_6.png')]

# jumpRight = [pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_1.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_2.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_3.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_4.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_5.png'), pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_6.png')]
# jumpLeft = [pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_Left_1.png'), pygame.image.load(r'C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_Left_2.png'), pygame.image.load(r'C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_Left_3.png'), pygame.image.load(r'C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_Left_4.png'), pygame.image.load(r'C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_Left_5.png'), pygame.image.load(r'C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Jump_Left_6.png').convert()]

playerStand = pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/paku_Idle.png')

background = pygame.image.load('C:/Users/ann/Documents/Python/webdev/khishchenko/my_first_game/space.jpg')

clock = pygame.time.Clock()

x = 50
y = 315
widht = 100
height = 100
speed = 5

isJump = False
jumpCount = 10
# gravity = 0.35

left = False
right = False
animCount = 0

platform_WIDTH = 32
platform_HEIGHT = 32
platform_COLOR = (102, 0, 102)

# level = [
#        "-------------------------",
#        "-                       -",
#        "-                       -",
#        "-                       -",
#        "-            --         -",
#        "-                       -",
#        "--                      -",
#        "-                       -",
#        "-                   --- -",
#        "-                       -",
#        "-                       -",
#        "-      ---              -",
#        "-                       -",
#        "-   -----------        -",
#        "-                       -",
#        "-                -      -",
#        "-                   --  -",
#        "-                       -",
#        "-                       -",
#        "-------------------------"]

def drawWindow():
    global animCount
    win.blit(background, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    # elif isJump:
    #     win.blit(jumpRight[animCount // 5], (x, y))
    #     animCount += 1
    else:
        win.blit(playerStand, (x, y))
        

    pygame.display.update()

run = True

while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > speed:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < winWidht - widht - speed:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    if not(isJump):
        # if keys[pygame.K_UP] and y > 5:
        #     y -= speed
        # if keys[pygame.K_DOWN] and y < 500 - height - 5:
        #     y += speed
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # i=z=0 # координаты
    # for row in level: # вся строка
    #     for col in row: # каждый символ
    #         if col == "-":
    #             #создаем блок, заливаем его цветом и рисеум его
    #             pf = pygame.display.set_mode((platform_WIDTH, platform_HEIGHT))
    #             pf.fill(platform_COLOR)
    #             win.blit(pf,(i,z))
                    
        #     i += platform_WIDTH #блоки платформы ставятся на ширине блоков
        # z += platform_HEIGHT    #то же самое и с высотой
        # i = 0                
    
    drawWindow()

pygame.quit()