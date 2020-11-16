import pygame
from pygame.locals import *

from gl import Renderer
import shaders

deltaTime = 0.0

pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

r = Renderer(screen)
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)
r.createObjects()

# cubeX = 0
# cubeY = 0
# cubeZ = 0

camX = 0
camY = 0
camZ = 3

pitchAngle = 0
yawAngle = 0
rollAngle = 0

isPlaying = True
while isPlaying:

    # Using arrows to change the rotation of the camera
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        yawAngle += 20 * deltaTime
        # cubeX -= 2 * deltaTime
    if keys[pygame.K_RIGHT]:
        yawAngle -= 20 * deltaTime
        # cubeX += 2 * deltaTime
    if keys[pygame.K_DOWN]:
        # cubeY -= 2 * deltaTime
        pitchAngle -= 20 * deltaTime
    if keys[pygame.K_UP]:
        # cubeY += 2 * deltaTime
        pitchAngle += 20 * deltaTime

    # Mover hacia la izquierda la cámara
    if keys[pygame.K_a]:
        camX -= 2 * deltaTime

    # Mover hacia la derecha la cámara
    if keys[pygame.K_d]:
        camX += 2 * deltaTime

    # Mover hacia abajo la cámara
    if keys[pygame.K_s]:
        camY -= 2 * deltaTime

    # Mover hacia enfrente la cámara
    if keys[pygame.K_w]:
        camY += 2 * deltaTime

    # Mover hacia adelante la cámara
    if keys[pygame.K_q]:
        camZ -= 2 * deltaTime

    # mover hacia atrás la cámara
    if keys[pygame.K_e]:
        camZ += 2 * deltaTime


    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_1:
                r.filledMode()
            elif ev.key == pygame.K_2:
                r.wireframeMode()
            elif ev.key == pygame.K_ESCAPE:
                isPlaying = False
        # Scroll to change the rollAngle of the camera
        if ev.type == pygame.MOUSEBUTTONDOWN or ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 4:
               rollAngle -= 20 * deltaTime
            if ev.button == 5:
               rollAngle += 20 * deltaTime

    # r.translateCube(cubeX, cubeY, cubeZ)
    r.translateCamera(camX, camY, camZ)
    r.rotateCamera(pitchAngle, yawAngle, rollAngle)

    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000

pygame.quit()
