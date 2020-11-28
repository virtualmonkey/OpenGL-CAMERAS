import pygame
from pygame.locals import *
import glm
from gl import Renderer, Model
import shaders

deltaTime = 0.0

camX = 0
camY = 0
camZ = 0

rollAngle = 0
pitchAngle = 0
yawAngle = 0

pygame.init()
clock = pygame.time.Clock()
screenSize = (960, 540)
screen = pygame.display.set_mode(screenSize, OPENGLBLIT | DOUBLEBUF | OPENGL)

pygame.mixer.music.load('background_music.mp3')
pygame.mixer.music.play(0)

r = Renderer(screen)
r.setShaders(shaders.vertex_shader, shaders.fragment_shader)

# cargar los modelos

fox= Model('models/ironman.obj', 'textures/ironman.tga')
fox.position = glm.vec3(0, -1, -8)
fox.rotation = glm.vec3(0, 0, 0)

nave = Model('models/coke.obj', 'textures/coke.png')
nave.position = glm.vec3(0,0,-4)
nave.rotation = glm.vec3(0, 0, 0)
nave.scale = glm.vec3(0.1, 0.1, 0.1)

r2 = Model('models/r2.obj','textures/R2.bmp')
r2.position = glm.vec3(0, 2, -15)
r2.rotation = glm.vec3(0, 0, 0)

spider = Model('models/spider.obj','textures/spider.jpg')
spider.position = glm.vec3(2, -1 , -17)
spider.rotation = glm.vec3(0, 90, 0)
spider.scale = glm.vec3(0.1, 0.1, 0.1)

# Añadir los objetos al render
r.models.append(fox)
r.models.append(r2)
r.models.append(nave)
r.models.append(spider)

isPlaying = True
crystal_shader_active = False;
while isPlaying:

    keys = pygame.key.get_pressed()

    # Cambiar pitch y jaw
    if keys[pygame.K_LEFT]:
        yawAngle += 20 * deltaTime
    if keys[pygame.K_RIGHT]:
        yawAngle -= 20 * deltaTime
    if keys[pygame.K_DOWN]:
        pitchAngle -= 20 * deltaTime
    if keys[pygame.K_UP]:
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

    # intercambiar shaders
    if keys[K_1]:
        r.setShaders(shaders.vertex_shader, shaders.fragment_shader)
        crystal_shader_active = False;
        r.ratio = 0
    if keys[K_2]:
        r.setShaders(shaders.vertex_shader, shaders.all_colors_shader)
        crystal_shader_active = False;
        r.ratio = 0
    if keys[K_3]:
        r.setShaders(shaders.vertex_shader, shaders.termic_vision)
        crystal_shader_active = False;
        r.ratio = 0
    if keys[K_4]:
        r.setShaders(shaders.expand_shader, shaders.all_colors_shader)
        crystal_shader_active = True;
    if keys[K_e]:
        if (crystal_shader_active == True):
            r.ratio+=10
    if keys[K_q]:
        if (crystal_shader_active == True):
            r.ratio-=10

    # Manejo del flujo del programa
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            isPlaying = False
        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                isPlaying = False
            elif ev.key == pygame.K_TAB:
                r.currentModel = (r.currentModel+1) % len( r.models )

        # acercar y alejar la cámara
        if ev.type == pygame.MOUSEBUTTONDOWN or ev.type == pygame.MOUSEBUTTONUP:
            if ev.button == 4:
                if r.camPosition.z>=-50:
                    r.camPosition.z -= 50 * deltaTime
            if ev.button == 5:
                if r.camPosition.z<=50:
                    r.camPosition.z += 50 * deltaTime

    r.camPosition.x = camX
    r.camPosition.y = camY
    r.rotateCamera(pitchAngle, yawAngle, rollAngle)
    r.render()

    pygame.display.flip()
    clock.tick(60)
    deltaTime = clock.get_time() / 1000
    r.timer=r.timer+1
    
pygame.quit()
