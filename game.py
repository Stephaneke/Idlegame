import pygame
import random
pygame.init()


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (127, 0, 255)

# Define some variables
FPS = 60
running = True


# screen variables
screen_width = 500
screen_height = 600
screen_size = (screen_width, screen_height)
pygame.display.set_caption("Stephane Idle ")
screen = pygame.display.set_mode(screen_size)
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# game variables
score = 98

green_value = 1
red_value = 2
orange_value = 3
white_value = 4
purple_value = 5

draw_green = False
draw_red = False
draw_orange = False
draw_white = False
draw_purple = False

green_length = 0
red_length = 0
orange_length = 0
white_length = 0
purple_length = 0

green_speed = 5
red_speed = 4
orange_speed = 3
white_speed = 2
purple_speed = 1

# draw button functions
green_cost = 1
green_owned = False
green_manager_cost = 100
red_cost = 2
red_owned = False
red_manager_cost = 500
orange_cost = 3
orange_owned = False
orange_manager_cost = 1800
white_cost = 4
white_owned = False
white_manager_cost = 4000
purple_cost = 5
purple_owned = False
purple_manager_cost = 10000




# game functions
def draw_task(color, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        length = 0
        draw = False
        score += value 
    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord -15, 200,30])
    pygame.draw.rect(screen, BLACK, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    value_text = font.render(str(round(value,2)), True, WHITE)
    screen.blit(value_text, (25, y_coord - 8))
    # draw the revenue per second
    revenue_per_second = round(value * speed / 200 * FPS, 2)
    revenue_text = font.render("€" + str(revenue_per_second) + " per sec", True, WHITE)
    screen.blit(revenue_text, (300, y_coord - 8))
    return task, length, draw

def draw_buttons(color, x_coord, cost, owned, manager_cost):
    color_button = pygame.draw.rect(screen, color, [x_coord, 340, 50, 30])
    color_cost = font.render(str(round(cost, 2)), True, BLACK)
    screen.blit(color_cost, (x_coord + 6, 350))
    if not owned:
        manager_button = pygame.draw.rect(screen, color, [x_coord, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost, 2)), True, BLACK)
        screen.blit(manager_text, (x_coord + 2, 410))
    else:
        manager_button = pygame.draw.rect(screen, BLACK, [x_coord, 405, 50, 30])
    return color_button, manager_button

# Game loop

while running:
    screen.fill(BLACK)
    timer.tick(FPS)
    if green_owned and not draw_green:
        draw_green = True
    if red_owned and not draw_red:
        draw_red = True
    if orange_owned and not draw_orange:
        draw_orange = True
    if white_owned and not draw_white:
        draw_white = True
    if purple_owned and not draw_purple:
        draw_purple = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Game logic
        if event.type == pygame.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_green = True
            if task2.collidepoint(event.pos):
                draw_red = True
            if task3.collidepoint(event.pos):
                draw_orange = True
            if task4.collidepoint(event.pos):
                draw_white = True
            if task5.collidepoint(event.pos):
                draw_purple = True

            if green_manager_button.collidepoint(event.pos):
                if score >= green_manager_cost and not green_owned:
                    score -= green_manager_cost
                    green_owned = True
            if red_manager_button.collidepoint(event.pos):
                if score >= red_manager_cost and not red_owned:
                    score -= red_manager_cost
                    red_owned = True
            if orange_manager_button.collidepoint(event.pos):
                if score >= orange_manager_cost and not orange_owned:
                    score -= orange_manager_cost
                    orange_owned = True
            if white_manager_button.collidepoint(event.pos):
                if score >= white_manager_cost and not white_owned:
                    score -= white_manager_cost
                    white_owned = True
            if purple_manager_button.collidepoint(event.pos):
                if score >= purple_manager_cost and not purple_owned:
                    score -= purple_manager_cost
                    purple_owned = True

            if green_button.collidepoint(event.pos) and score >= green_cost:
                score -= green_cost
                green_value = round(green_value + .15, 2)
                green_cost = round(green_cost * 1.1, 2)
            if red_button.collidepoint(event.pos) and score >= red_cost:
                score -= red_cost
                red_value = round(red_value + .3, 2)
                red_cost = round(red_cost * 1.08, 2)
            if orange_button.collidepoint(event.pos) and score >= orange_cost:
                score -= orange_cost
                orange_value = round(orange_value + .45, 2)
                orange_cost = round(orange_cost *1.06, 2)
            if white_button.collidepoint(event.pos) and score >= white_cost:
                score -= white_cost
                white_value = round(white_value + .6, 2)
                white_cost = round(white_cost *1.04, 2)
            if purple_button.collidepoint(event.pos) and score >= purple_cost:
                score -= purple_cost
                purple_value = round(purple_value + .75, 2)
                purple_cost = round(purple_cost *1.02, 2)    

    # --- Drawing code
    task1, green_length, draw_green = draw_task(GREEN, 50, green_value, draw_green, green_length, green_speed)
    task2, red_length, draw_red = draw_task(RED, 110, red_value, draw_red, red_length, red_speed)
    task3, orange_length, draw_orange = draw_task(ORANGE, 170, orange_value, draw_orange, orange_length, orange_speed)
    task4, white_length, draw_white = draw_task(WHITE, 230, white_value, draw_white, white_length, white_speed)
    task5, purple_length, draw_purple = draw_task(PURPLE, 290,  purple_value,  draw_purple, purple_length, purple_speed)

    green_button, green_manager_button = draw_buttons(GREEN, 10, green_cost, green_owned, green_manager_cost)
    red_button, red_manager_button = draw_buttons(RED, 70, red_cost, red_owned, red_manager_cost)
    orange_button, orange_manager_button = draw_buttons(ORANGE, 130, orange_cost, orange_owned, orange_manager_cost)
    white_button, white_manager_button = draw_buttons(WHITE, 190, white_cost, white_owned, white_manager_cost)
    purple_button, purple_manager_button = draw_buttons(PURPLE, 250, purple_cost, purple_owned, purple_manager_cost)

    display_score = font.render("Money: €" + str(round(score, 2)), True, WHITE, BLACK)
    screen.blit(display_score, (10, 5))
    buy_more = font.render("Buy more:", True, WHITE, BLACK)
    screen.blit(buy_more, (10, 315))
    buy_manager = font.render("Buy managers:", True, WHITE, BLACK)
    screen.blit(buy_manager, (10, 380))
    # --- Update screen


    pygame.display.flip()

pygame.quit()