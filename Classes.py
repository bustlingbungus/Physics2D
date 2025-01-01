from math import sqrt

# PHYSICS CONSTANTS
BOUNCE_COEFF = 0.9

# Define a structure to represent 2D position, velocity, and acceleration
class Vector2:
    
    # Initialise x and y variables 
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
    
    # The magnitude of the vector is sqrt(x^2 + y^2)
    def length(self):
        return sqrt((self.x**2) + (self.y**2))
    
    # Make the vector's length 1 by dividing x and y by the length
    def normalize(self):
        leng = self.length()
        self.x /= leng
        self.y /= leng
        
    # Redefine basic operators to make vector arithmetic easier
    
    # Return this vector minus the other vector
    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)
    
    # Subtract the other vector's x and y components from this one
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    # Add the other vector's x and y components to this one
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self    
        
    # Return x and y multiplied by k
    def __mul__(self, k):
        return Vector2(self.x * k, self.y * k)
    

# A class for a collision object
class Ball:
    
    # Initialise position, velocity, and acceleration vectors
    # Initialise window dimensions
    # Initialise the ball's color and radius
    def __init__(self, x, y, radius, wndWidth, wndHeight, color):
        self.pos = Vector2(x, y)
        # Initialise position and velocity to 0
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2(0, 0)
        
        self.wndWidth, self.wndHeight = wndWidth, wndHeight
        self.color = color
        self.radius = radius

    # Check for collisions with other balls, and update position and velocity
    def update(self, objects, gravity):
        # Iterate through all other balls, and handle collisions
        for ball in objects:
            self.collide_with_ball(ball)
        # Collide with the window borders
        self.collide_with_borders()
        
        # For this example, acceleration will always just be gravity
        self.acceleration = gravity
        # Add accerleration to velocity, and add velocity to acceleration
        self.velocity += self.acceleration
        self.pos += self.velocity
        
    # Bounces the ball off the side of the window by setting its position back inside the window,
    # Then multiplying it's velocity by a negative number to travel in the opposite direction
    def collide_with_borders(self):
        # Out of bounds on the left side
        if (self.pos.x < self.radius):
            self.pos.x = self.radius
            self.velocity.x *= -BOUNCE_COEFF
        # Out of bound on the right side
        elif (self.pos.x > self.wndWidth-self.radius):
            self.pos.x = self.wndWidth-self.radius
            self.velocity.x *= -BOUNCE_COEFF
        # Out of bounds on the top
        if (self.pos.y < self.radius):
            self.pos.y = self.radius
            self.velocity.y *= -BOUNCE_COEFF
        # Out of bounds on the bottom
        elif (self.pos.y > self.wndHeight-self.radius):
            self.pos.y = self.wndHeight-self.radius
            self.velocity.y *= -BOUNCE_COEFF
    
    
    # Handles collision with another ball by pushing them aprt and swapping their velocities
    def collide_with_ball(self, other):
        # Find the displacement between the two balls
        disp = other.pos - self.pos
        
        # r (sum of the radii) is the smallest distance to not be a collision
        r = self.radius + other.radius
        # find the length of the displacement
        # If the length is zero, then "other" is the same ball as "self", so no collision should happen
        leng = disp.length()
        
        # If the displacement is less than the sum of radii, there is a collision
        if (leng < r and leng != 0):
            # Normalise the displacement to get a unit vector (the direction of the displacemnet)
            disp.normalize()
            # Each ball will move half the distance that they're overlapping by
            # Find this distance by subtracting leng from r, then dividing by 2
            # Add 1 to avoid repeat collisions on subsequent checks
            move = (r - leng)/2 + 1
            
            # Alter each ball's position by "move" units, along the direction of displacement by multiplying the 
            # unit vector by "move", then adding/subtracting it from position
            self.pos -= disp * move
            other.pos += disp * move
            
            # On collisions, swap the ball's velocities (since in this example they all have mass 1)
            temp = self.velocity
            self.velocity = other.velocity * BOUNCE_COEFF
            other.velocity = temp * BOUNCE_COEFF
            