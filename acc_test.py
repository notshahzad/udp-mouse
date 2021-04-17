import pygame
import random
pygame.init()
display_x = 1000
display_y = 500
white = (225, 225, 225)
circle_di = 20


def make_circle():
    circle_x = random.randint(circle_di, display_x-circle_di)
    circle_y = random.randint(circle_di, display_y-circle_di)
    return circle_x, circle_y


win = pygame.display.set_mode((display_x, display_y))
pygame.display.set_caption('accuracy')
circle_x, circle_y = make_circle()
game = True
retry = False
sc0re = 0
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print('mouse_pos :', mouse_x, mouse_y)
            if game == True:
                if mouse_x >= circle_x-circle_di and mouse_x <= circle_x + circle_di and mouse_y >= circle_y - circle_di and mouse_y <= circle_y+circle_di:
                    circle_x, circle_y = make_circle()
                    sc0re += 1
                else:
                    sc0re = 0
                    retry = True
                    game = False
            if retry == True:
                if mouse_x >= 444 and mouse_x <= 556 and mouse_y >= 260 and mouse_y <= 287:
                    game = True
                    retry = False
    pygame.time.delay(40)
    if retry == True:
        font = pygame.font.SysFont(None, 24)
        resume = font.render('retry', True, white)
        resume_text_pos = display_x//2-56
        win.blit(resume, (resume_text_pos, 260))
        pygame.display.update()
        win.fill(0)
    if game == True:
        font = pygame.font.SysFont(None, 24)
        score = 'score:'+str(sc0re)
        score_render = font.render(score, True, white)
        win.blit(score_render,(display_x-100, 30))
        pygame.draw.circle(win, white, (circle_x, circle_y), circle_di)
        pygame.display.update()
        win.fill(0)
