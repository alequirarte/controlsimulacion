import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 600,295
screen = pygame.display.set_mode(size)
#pygame.display.set_caption("Joystick Tester")
background_image = pygame.image.load("prueba.png").convert()
frameRect = pygame.Rect((0,0), (width,height))

crosshair = pygame.surface.Surface((10,10))
pygame.draw.circle(crosshair,pygame.Color("Red"), (5,5), 5,0)

crosshairb = pygame.surface.Surface((10,10))
pygame.draw.circle(crosshairb,pygame.Color("blue"), (5,5), 5,0)

crosshairc = pygame.surface.Surface((10,10))
pygame.draw.circle(crosshairc,pygame.Color("green"), (5,5), 5,0)

crosshaird = pygame.surface.Surface((10,10))
pygame.draw.circle(crosshaird,pygame.Color("yellow"), (5,5), 5,0)

while True:
    pygame.event.pump()
    screen.blit(background_image, (0,0))


    Keys = pygame.key.get_pressed()

    if Keys[pygame.K_x]:screen.blit(crosshairb, (461,100))  # x
    
    if Keys[pygame.K_a]:screen.blit(crosshairb, (518,146))  # a

    if Keys[pygame.K_y]:screen.blit(crosshairb, (405,143))  # y

    if Keys[pygame.K_b]:screen.blit(crosshairb, (462,189))  # b

    if Keys[pygame.K_s]:screen.blit(crosshairc, (245,163))  # select

    if Keys[pygame.K_l]:screen.blit(crosshairc, (307,163))  # start

    if Keys[pygame.K_q]:screen.blit(crosshaird, (38,35))  # superior izquierdo

    if Keys[pygame.K_p]:screen.blit(crosshaird, (558,35))  # superior derecho



    x = -1 if Keys[pygame.K_LEFT] else 1 if Keys[pygame.K_RIGHT] else 0

    y = -1 if Keys[pygame.K_UP] else 1 if Keys[pygame.K_DOWN] else 0



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(crosshair,((x*25)+133-5,(y*25)+149-5))
    pygame.display.flip()
    clk.tick(40)


