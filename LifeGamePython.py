import pygame
import numpy as np
import random as ran
import time

pygame.init()

width, height = 600, 600

screen = pygame.display.set_mode((width, height))
time.sleep(0.1)
bg = 25, 25, 25

screen.fill(bg)

nxC, nyC = 100, 100

dimCW = int(width / nxC)
dimCH = int(height / nyC)

gameState = np.zeros((nxC, nyC))

pauseExact = False

print(dimCH, dimCW)


def fillRandom(newGameState):
    for y in range(0, nyC):
        for x in range(0, nxC):
            newGameState[x, y] = ran.randint(0, 1)


while True:

    newGameState = np.copy(gameState)
    screen.fill(bg)
    # time.sleep(0.1)
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pauseExact = not pauseExact
                print("p pressed")
            if event.key == pygame.K_r:
                fillRandom(newGameState)
                print("r pressed")
            if event.key == pygame.K_e:
                pygame.quit()
                print("e pressed")
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            print(int(x / 6),int(y / 6))
            newGameState[int(x / 6),int(y / 6)] = 1
            print("mouse clicked")

    for y in range(0, nyC):
        for x in range(0, nxC):
            if not pauseExact:
                n_vecinos = \
                    gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                    gameState[(x) % nxC,     (y - 1) % nyC] + \
                    gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                    gameState[(x - 1) % nxC, (y) % nyC] + \
                    gameState[(x + 1) % nxC, (y) % nyC] + \
                    gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                    gameState[(x) % nxC,     (y + 1) % nyC] + \
                    gameState[(x + 1) % nxC, (y + 1) % nyC]

                if gameState[x, y] == 0 and n_vecinos == 3:
                    newGameState[x, y] = 1
                elif gameState[x, y] == 1 and (n_vecinos < 2 or n_vecinos > 3):
                    newGameState[x, y] = 0

            poly = [(x * dimCW, y * dimCH),
                    ((x + 1) * dimCW, y * dimCH),
                    ((x + 1) * dimCW, (y + 1) * dimCH),
                    ((x * dimCW), (y + 1) * dimCH)]

            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    gameState = np.copy(newGameState)

    pygame.display.flip()
