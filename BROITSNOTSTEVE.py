from pickle import TRUE
import pygame
pygame.init
screen=pygame.display.set_mode((500,500))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,125,125),pygame.Rect(200,200,200,200))
    pygame.display.flip()