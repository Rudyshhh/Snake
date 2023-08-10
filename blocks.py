import pygame
from sys import exit
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('whatevs')
clock=pygame.time.Clock()
test_surface=pygame.Surface((400,500))
test_surface.fill((200,215,5))
test_rect=pygame.Rect(200,200,100,100)
test_rect2=test_surface.get_rect(center=(300,300))
# x_pos=10
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.QUIT
            exit()
    screen.fill("red")
    # x_pos+=1
    # screen.blit(test_surface,(50,50))
    screen.blit(test_surface,test_rect2)
    pygame.draw.rect(screen,'blue',test_rect)
    test_rect2.left-=2
    test_rect2.right+=1
    # pygame.draw.rect(screen,'aqua',test_rect2)
    pygame.display.update()
    clock.tick(60)
        