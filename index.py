from typing import no_type_check
import pygame
import numpy as np 

pygame.init()


width, heigth = 1000, 1000
screen = pygame .display.set_mode((height, width))

bg = 25, 25, 25
screen . fill(bg)

nxC, nxC = 25, 25

dimCW = width / nxC
dimCH = heigth / nyC 

gameState = np.zeros((nxC, nyC))

while True:
    for y in range(0, nxC):
        for x in range(0, nyC):

            n_neigth = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                       gameState[(x)     % nxC, (y - 1) % nyC] + \
                       gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                       gameState[(x - 1) % nxC, (y)     % nyC] + \
                       gameState[(x + 1) % nxC, (y)     % nyC] + \
                       gameState[(x - 1) % nxC, (y + 1) %] + \
                       gameState[(x)     % nxC, (y + 1)] + \
                       gameState[(x + 1) % nxC, (y + 1)]


                       
            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]
    

            pygamne.draw.polygon(screen, (128, 128, 128), poly, 1)

pygame.display.polygon.flip()

 

            
