import pygame, sys
# Import the classes we've made 
from Classes import Vector2, Ball

pygame.init() # turn on pygame

# Variables to track mouse buttons
left_mouseDown = False
right_mouseDown = False


# CONSTANT SIMULATION VARIABLES

# Gravity direction and magnitude
GRAVITY_STRENGTH = 0.1
gravity = Vector2(0, GRAVITY_STRENGTH)

# Colour variables 
BALL_COLOR = "blue"
BACKGROUND_COLOR = "white"

# The radius of each ball and the brush to remove them
BALL_RADIUS = 20
BRUSH_SIZE = 20

# Window dimensions. Set up the window, a font, and a clock
WIDTH, HEIGHT = 720, 720
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
FONT = pygame.font.SysFont("Satoshi-Variable.ttf", int(WIDTH/20))
CLOCK = pygame.time.Clock()

# update all physics objects
def update_objects(objects):
    # for each ball in the array, update the object, the render it ot the screen
    for ball in objects:
        ball.update(objects, gravity)
        # render the ball by drawing a circle, with reference to the ball's variables
        pygame.draw.circle(WINDOW, ball.color, (ball.pos.x, ball.pos.y), ball.radius, 1)
        

# change global variables according to user input
def get_input(event):
    # declare external variables
    global left_mouseDown, right_mouseDown, gravity
    
    # update mouse variables when the mouse is pressed or released
    if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
        # get an array of all the mouse buttons
        mouse_buttons = pygame.mouse.get_pressed()
        # update variables 
        left_mouseDown = mouse_buttons[0]
        right_mouseDown = mouse_buttons[2]
    
    # alter gravity when a key is pressed 
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            gravity = Vector2(0, -GRAVITY_STRENGTH)
        elif event.key == pygame.K_DOWN:
            gravity = Vector2(0, GRAVITY_STRENGTH)
        elif event.key == pygame.K_LEFT:
            gravity = Vector2(-GRAVITY_STRENGTH, 0)
        elif event.key == pygame.K_RIGHT:
            gravity = Vector2(GRAVITY_STRENGTH, 0)
        elif event.key == pygame.K_RETURN:
            gravity = Vector2(0, 0)



quit_app = False
# This array will contain all balls in the simulation
objects = []

# Main simulation loop
while (not quit_app):
    
    # Handle input
    for event in pygame.event.get():
        # Exit when you press the X
        if event.type == pygame.QUIT:
            quit_app = True
        else:
            # Call the get input function for other inputs
            get_input(event)
    
    # Fill the window with a solid colour
    WINDOW.fill(BACKGROUND_COLOR)
    
    # When pressing left mouse, spawn a ball on the mouse
    if left_mouseDown:
        # Find the mouse's position
        mousex, mousey = pygame.mouse.get_pos()
        # Spawn in a new ball at (mousex, mousey)
        ball = Ball(mousex, mousey, BALL_RADIUS, WIDTH, HEIGHT, BALL_COLOR)
        # Add the ball to the array
        objects.append(ball)
    
    # When pressing right mouse, remove balls nearby the cursor
    if right_mouseDown:
        # Find the mouse's positoin
        mousex, mousey = pygame.mouse.get_pos()
        # Check every ball in the array 
        for ball in objects:
            # Convert the mouse position to a Vector2, and find the displacement from the current ball
            disp = ball.pos - Vector2(mousex, mousey)
            # If the cursor is close enough to the ball, remove it from the array
            if disp.length() < ball.radius+BRUSH_SIZE:
                objects.remove(ball)
    
    # Update all the objects
    update_objects(objects)
    
    # Display object count
    object_count_text = FONT.render(f"{len(objects)} objects", True, "black")
    WINDOW.blit(object_count_text, (5, 5))

    # Update the window
    pygame.display.update()
    CLOCK.tick(300)
    
# Close the application when the main loop exits
pygame.quit()
sys.exit()