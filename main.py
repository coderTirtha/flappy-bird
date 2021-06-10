import pygame
from random import randint
pygame.init()
display = pygame.display.set_mode((320, 568))
text = pygame.font.Font(None, 50)
bg = pygame.image.load('bg.png')
bird = pygame.image.load('bird.png')
pole_width = 70
pole_gap = 150
pole_x = 320
top_pole_height = randint(100, 400)
pole_color = (255, 0, 0)
bird_x = 20
bird_y = 200
score = 0
clock = pygame.time.Clock()
while True:
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_y = bird_y - 3
    elif keys[pygame.K_DOWN]:
        bird_y = bird_y + 6
    display.blit(bg, (0, 0))
    display.blit(bird, (bird_x, bird_y))
    pole_x = pole_x - 2
    if pole_x <= -pole_width:
        pole_x = 320
        top_pole_height = randint(50, 400)
        score = score + 20
    pygame.draw.rect(display, pole_color, (pole_x, 0, pole_width, top_pole_height))
    pygame.draw.rect(display, pole_color, (pole_x, top_pole_height + pole_gap, pole_width, 568))

    # collision part
    if pole_x <= bird_x + 50 and bird_x <= pole_x + pole_width:
        if bird_y <= top_pole_height or bird_y >= top_pole_height + pole_gap:
            score = score - 1

    score_text = text.render(f'Score: {score}', True, (0, 0, 0))
    display.blit(score_text, (0, 0))
    pygame.display.update()
    clock.tick(60)