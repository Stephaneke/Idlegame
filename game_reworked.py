import pygame
import random

pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PURPLE = (127, 0, 255)

# Define constants
FPS = 60

# Screen settings
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 500
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# Task Class
class Task:
    def __init__(self, color, y_coord, value, speed):
        self.color = color
        self.y_coord = y_coord
        self.value = value
        self.speed = speed
        self.length = 0
        self.draw = False

    def update(self):
        if self.draw and self.length < 200:
            self.length += self.speed
        elif self.length >= 200:
            self.length = 0
            self.draw = False
            return self.value
        return 0

    def render(self, screen, font):
        pygame.draw.circle(screen, self.color, (30, self.y_coord), 20, 5)
        pygame.draw.rect(screen, self.color, [70, self.y_coord - 15, 200, 30])
        pygame.draw.rect(screen, BLACK, [75, self.y_coord - 10, 190, 20])
        pygame.draw.rect(screen, self.color, [70, self.y_coord - 15, self.length, 30])

        value_text = font.render(str(round(self.value, 2)), True, WHITE)
        screen.blit(value_text, (25, self.y_coord - 8))

        # Draw revenue per second
        revenue_per_second = round(self.value * self.speed / 200 * FPS, 2)
        revenue_text = font.render("€" + str(revenue_per_second) + " per sec", True, WHITE)
        screen.blit(revenue_text, (300, self.y_coord - 8))

    def check_collision(self, pos):
        # Check if the click is inside the circle
        circle_center = (30, self.y_coord)
        circle_radius = 20
        dx, dy = pos[0] - circle_center[0], pos[1] - circle_center[1]
        return dx*dx + dy*dy <= circle_radius*circle_radius

# Button Class
class Button:
    def __init__(self, color, x_coord, cost, manager_cost):
        self.color = color
        self.x_coord = x_coord
        self.cost = cost
        self.manager_cost = manager_cost
        self.owned = False

    def render(self, screen, font):
        button = pygame.draw.rect(screen, self.color, [self.x_coord, 340, 50, 30])
        cost_text = font.render(str(round(self.cost, 2)), True, BLACK)
        screen.blit(cost_text, (self.x_coord + 6, 350))

        if not self.owned:
            manager_button = pygame.draw.rect(screen, self.color, [self.x_coord, 405, 50, 30])
            manager_text = font.render(str(round(self.manager_cost, 2)), True, BLACK)
            screen.blit(manager_text, (self.x_coord + 2, 410))
        else:
            manager_button = pygame.draw.rect(screen, BLACK, [self.x_coord, 405, 50, 30])

        return button, manager_button

# Game Class
class IdleGame:
    def __init__(self):
        pygame.display.set_caption("Stephane Idle")
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.clock = pygame.time.Clock()
        self.running = True
        self.score = 0

        # Create tasks and buttons
        self.tasks = [
            Task(GREEN, 50, 1, 5),
            Task(RED, 110, 2, 4),
            Task(ORANGE, 170, 3, 3),
            Task(WHITE, 230, 4, 2),
            Task(PURPLE, 290, 5, 1)
        ]

        self.buttons = [
            Button(GREEN, 10, 1, 100),
            Button(RED, 70, 2, 500),
            Button(ORANGE, 130, 3, 1800),
            Button(WHITE, 190, 4, 4000),
            Button(PURPLE, 250, 5, 10000)
        ]

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for task in self.tasks:
                    if task.check_collision(event.pos):
                        task.draw = True
                for i, button in enumerate(self.buttons):
                    task_button, manager_button = button.render(self.screen, self.font)
                    if task_button.collidepoint(event.pos) and self.score >= button.cost:
                        self.score -= button.cost
                        self.tasks[i].value = round(self.tasks[i].value + 0.15 * (i+1), 2)
                        button.cost = round(button.cost * 1.1, 2)
                    if manager_button.collidepoint(event.pos) and self.score >= button.manager_cost and not button.owned:
                        self.score -= button.manager_cost
                        button.owned = True
                        self.tasks[i].draw = True

    def update(self):
        for i, task in enumerate(self.tasks):
            button = self.buttons[i]
            if button.owned:
                task.draw = True
            self.score += task.update()


    def draw(self):
        self.screen.fill(BLACK)
        for task in self.tasks:
            task.render(self.screen, self.font)
        for button in self.buttons:
            button.render(self.screen, self.font)
        score_text = self.font.render("Money: €" + str(round(self.score, 2)), True, WHITE, BLACK)
        self.screen.blit(score_text, (10, 5))
        pygame.display.flip()

# Create game instance and run
game = IdleGame()
game.run()

pygame.quit()
