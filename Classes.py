import math

class Vector2:
    x = 0
    y = 0
    
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def length(self):
        return math.sqrt((self.x*self.x) + (self.y*self.y))
    
    def normalize(self):
        len = self.length()
        self.x /= len
        self.y /= len
        
    def __sub__(self, other : "Vector2"):
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __iadd__(self, other : "Vector2"):
        self.x += other.x
        self.y += other.y
        return self
        
    def __isub__(self, other : "Vector2"):
        self.x -= other.x
        self.y -= other.y
        return self
        
    def __mul__(self, k):
        return Vector2(self.x * k, self.y * k)
    
BOUNCE_COEFF = 0.9
GRAVITY_STRENGTH = 0.2
BALL_RADIUS = 20
BRUSH_SIZE = 20

BALL_COLOR = "blue"
BACKGROUND_COLOR = "white"

gravity = Vector2(0, GRAVITY_STRENGTH)

class Ball:
    def __init__(self, x, y, radius, wndWidth, wndHeight, color):
        self.pos = Vector2(x, y)
        self.acceleration = gravity
        self.wndWidth, self.wndHeight = wndWidth, wndHeight
        self.color = color
        self.radius = radius
        
    pos = Vector2(0, 0) 
    velocity = Vector2(0, 0)
    acceleration = Vector2(0, 0)
    radius = 0
    wndWidth, wndHeight = 0, 0
    color = "blue"


    def update(self, objects):
        for ball in objects:
            self.collide_with_ball(ball)
        self.collide_with_borders()
        
        self.acceleration = gravity
        self.velocity += self.acceleration
        self.pos += self.velocity
        
    
    def collide_with_borders(self):
        r = self.radius
        if (self.pos.x < r):
            self.pos.x = r
            self.velocity.x *= -BOUNCE_COEFF
        elif (self.pos.x > self.wndWidth-r):
            self.pos.x = self.wndWidth-r
            self.velocity.x *= -BOUNCE_COEFF
        if (self.pos.y < r):
            self.pos.y = r
            self.velocity.y *= -BOUNCE_COEFF
        elif (self.pos.y > self.wndHeight-r):
            self.pos.y = self.wndHeight-r
            self.velocity.y *= -BOUNCE_COEFF
            
    def collide_with_ball(self, other : "Ball"):
        disp = other.pos - self.pos
        
        r = self.radius + other.radius
        len = disp.length()
        
        if (len < r and len != 0):
            disp.normalize()
            move = (r - len)/2
            self.pos -= disp * move
            other.pos += disp * move
            
            temp = self.velocity
            self.velocity = other.velocity * BOUNCE_COEFF
            other.velocity = temp * BOUNCE_COEFF
            