import pygame
import numpy as np


# constantes physiques
g = 9.81
L = 2
mu = 0.1 # frottements

THETA_0 = np.pi / 2 # 90°
THETA_DOT_0 = 0 # pas de vitesse initiale
DELTA_T = 0.01

# constante d'affichage
OFFSET_X = 300
OFFSET_Y = 150
LENGTH = 100


def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g/L) * np.sin(theta)


def theta_to_pos(theta):
    #cos(π/2 - θ) = x / L <=> x = cos(π/2 - θ) * L
    x = np.cos(np.pi/2 - theta) * L

    # cos(θ) = y / L <=> y = cos(θ) * L
    y = np.cos(theta) * L
    
    return x*LENGTH + OFFSET_X, y*LENGTH + OFFSET_Y 


pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True

theta = THETA_0
theta_dot = THETA_DOT_0 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = (event.pos[0] - OFFSET_X) / LENGTH
            if x > L: x = L
            elif x < -L: x = -L
            theta = np.arcsin(x/L)
            theta_dot = THETA_DOT_0 # commente cette ligne pour accumuler de la vitesse 

    screen.fill("black")

    theta_double_dot = get_theta_double_dot(theta, theta_dot)
    theta += theta_dot * DELTA_T
    theta_dot += theta_double_dot * DELTA_T

    pos = theta_to_pos(theta)
    pygame.draw.line(screen, "white", (OFFSET_X, OFFSET_Y), pos)
    pygame.draw.circle(screen, "red", pos, 30)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
