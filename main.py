import pygame, sys
from Classes import Vector2, Ball, GRAVITY_STRENGTH, BALL_COLOR, BALL_RADIUS, BACKGROUND_COLOR, BRUSH_SIZE

pygame.init()

left_mouseDown = False
right_mouseDown = False

gravity = Vector2(0, GRAVITY_STRENGTH)

WIDTH, HEIGHT = 720, 720
FONT = pygame.font.SysFont("Satoshi-Variable.ttf", int(WIDTH/20))
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

# update all physics objects
def update_objects(objects):
    # for each ball in the array, update the object, the render it ot the screen
    for ball in objects:
        ball.update(objects, gravity)
        # render the ball by drawing a circle, with reference to the ball's variables
        pygame.draw.circle(WINDOW, BALL_COLOR, (ball.pos.x, ball.pos.y), ball.radius, 1)
        

# change globar variables according to user input
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


quit = False
objects = []

while (not quit):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            get_input(event)
            
    WINDOW.fill(BACKGROUND_COLOR)
    
    if left_mouseDown:
        mousex, mousey = pygame.mouse.get_pos()
        ball = Ball(mousex, mousey, BALL_RADIUS, WIDTH, HEIGHT, BALL_COLOR)
        objects.append(ball)
        
    if right_mouseDown:
        mousex, mousey = pygame.mouse.get_pos()
        for ball in objects:
            dx, dy = ball.pos.x - mousex, ball.pos.y - mousey
            disp = Vector2(dx, dy)
            if disp.length() < ball.radius+BRUSH_SIZE:
                objects.remove(ball)
                
    update_objects(objects)
    
    object_count_text = FONT.render(f"{len(objects)} objects", True, "black")
    WINDOW.blit(object_count_text, (5, 5))

    pygame.display.update()
    CLOCK.tick(300)