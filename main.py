import pygame
 
import target as t
import score as s
from constants import *

pygame.init()

# OBJECTS
targets = [t.Target(SPEED, TARGET_RADIUS)]
score = s.Score()

# FUNCTIONS

def handle_target_clicks(pos):
    global SPEED
    for target in targets:
        if target.isOver(pos):
            target.pressed = True
            SPEED += ACCELERATION
            targets.append(t.Target(SPEED, TARGET_RADIUS))
            score.increase()

def draw_targets():
    for target in targets:
        target.draw()

def shrink_targets():
    for target in targets:
        if not target.pressed:
            target.shrink(targets)
        else:
            target.radius -= PRESSED_SPEED

def draw_back():
    WIN.fill(BACKGROUND_COLOR)
    draw_targets()
    score.draw()
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        shrink_targets()
        draw_back()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_target_clicks(pygame.mouse.get_pos())


    pygame.quit()

main()
