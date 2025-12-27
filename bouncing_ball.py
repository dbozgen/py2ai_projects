import pygame
import sys
import random  

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

#Colors
WHITE = (255, 255, 255)
ball_color = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 5
ball_speed_y = 3

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # speed control 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_speed_y *= 1.5
                ball_speed_x *= 1.5
            if event.key == pygame.K_DOWN:
                ball_speed_y *= 0.5
                ball_speed_x *= 0.5

    # Fill screen 
    screen.fill(WHITE)
    
    # ball movement
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    #bounce off walls
    if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
        ball_speed_x = -ball_speed_x
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  
    if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
        ball_speed_y = -ball_speed_y
        ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  

    # Draw ball 
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)
    
    # Update display
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
sys.exit()