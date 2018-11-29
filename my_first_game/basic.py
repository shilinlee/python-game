import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Slither")

pygame.display.update()

gameExit = False

while not gameExit:
    for even in pygame.event.get():
        print(even)

pygame.quit()

quit()

