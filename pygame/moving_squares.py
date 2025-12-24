# import the pygame library
import pygame

# initiate the pygame modules
pygame.init()

# set up the dimensions of the window
screen = pygame.display.set_mode((800, 600))
#add a caption to the window
pygame.display.set_caption("Moving Squares")

# Square properties
# starting position on horizontal axis
square_x = 100
# starting position on vertical axis
square_y = 250
# size of the square
square_size = 100
# movement speed of the square
speed = 1   

# main game state loop
running = True

#game loop: while running is True, track events and update, if the event type is quit, set running to False and exit the loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check which keys are pressed
    keys = pygame.key.get_pressed()
    # if left arrow key is pressed, move square left and follow the same logic for right, up, and down arrow keys
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed
    # Keep the square within the window bounds
    #if square_x is less than 0, set it to 0
    if square_x < 0:
        square_x = 0
    #if square_x is greater than window width minus square size, set it to that value
    if square_x > 800 - square_size:
        square_x = 800 - square_size
    if square_y < 0:
        square_y = 0
    if square_y > 600 - square_size:
        square_y = 600 - square_size

    # fill the screen with black color and draw the square at its new position
    screen.fill((0, 0, 0))
    #draw a green square at the updated position 
    pygame.draw.rect(screen, (0, 255, 0), (square_x, square_y, square_size, square_size))
    pygame.display.flip()

pygame.quit()