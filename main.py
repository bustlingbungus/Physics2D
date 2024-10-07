import pygame, sys
from Classes import Vector2, Ball, GRAVITY_STRENGTH, BALL_COLOR, BALL_RADIUS, gravity, BACKGROUND_COLOR, BRUSH_SIZE

pygame.init()

left_mouseDown = False
right_mouseDown = False

WIDTH, HEIGHT = 540, 540
FONT = pygame.font.SysFont("Satoshi-Variable.ttf", int(WIDTH/20))
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()


def update_objects(objects):
    for ball in objects:
        ball.update(objects)
        pygame.draw.circle(WINDOW, "blue", (ball.pos.x, ball.pos.y), ball.radius, 1)
        
        
def get_input(event):
    global left_mouseDown, right_mouseDown, gravity
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            left_mouseDown = True
        elif mouse_buttons[2]:
            right_mouseDown = True
    elif event.type  == pygame.MOUSEBUTTONUP:
        mouse_buttons = pygame.mouse.get_pressed()
        if not mouse_buttons[0]:
            left_mouseDown = False
        # i am not sure why this is not working
        elif not mouse_buttons[2]:
            right_mouseDown = False
    
    
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
        gravity = Vector2(0, -GRAVITY_STRENGTH)
    elif keys_pressed[pygame.K_DOWN]:
        gravity = Vector2(0, GRAVITY_STRENGTH)
    elif keys_pressed[pygame.K_LEFT]:
        gravity = Vector2(-GRAVITY_STRENGTH, 0)
    elif keys_pressed[pygame.K_RIGHT]:
        gravity = Vector2(GRAVITY_STRENGTH, 0)
    elif keys_pressed[pygame.K_RETURN]:
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