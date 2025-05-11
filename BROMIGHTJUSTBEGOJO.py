import pygame
pygame.init
screen=pygame.display.set_mode((500,500))
white=(255,255,255)
blue=(0,0,255)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(white)
    pygame.draw.circle(screen,blue,(250,250),100)
    pygame.display.flip()