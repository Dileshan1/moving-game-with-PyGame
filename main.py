import pygame

# Create window for game
window = pygame.display.set_mode((500, 500))
x=50
y=50
width=40
height=40

v=5     # size of moving

jump = False
cjump = 10

flag = True

while flag:

    # end of game(quit button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

    # time delay
    pygame.time.delay(100)

    # access keys in the keyboard
    keys = pygame.key.get_pressed()
                     # keyd[pygame.K_ ....]

    if keys[pygame.K_LEFT] and x>v:
        x-=v

    if keys[pygame.K_RIGHT] and x<500-width-v:
        x+=v

    if not jump:
        if keys[pygame.K_UP] and y>v:
            y-=v

        if keys[pygame.K_DOWN] and y<500-height-v:
            y+=v

        if keys[pygame.K_SPACE]:
            jump = True
    else:
        if cjump>-15:
            y-=cjump
            cjump-=1
        else:
            jump=False
            cjump = 10

    # new window for every loop
    window.fill((0,0,0))

    # create object
    pygame.draw.rect(window, (230, 23, 89), (x, y, width, height))          # ((RGB color), (position, size))
    pygame.display.update()

pygame.quit()