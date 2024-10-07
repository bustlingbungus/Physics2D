## ISSUES
### Framerate
In the C version, the program is set to run at a fixed framerate (120fps). I don't know how to do that in pygame,
so I just added 'CLOCK.tick(300)' at the end, which is just wasiting for 0.3s, not atually fixing the framerate.
This discrepancy leads to some very unnatural physics
### Input
Input is broken, you should be able to press arrow keys to change gravity, and return to disable it. I don't know 
why this doesn't work, the code for it is in 'get_input'

Right clicking allows you to delete entities. For some reason, right clicking once will put your mouse in "delete 
mode" forever, even when you release right click. I don't know why this is, the code for it is also in 'get_input'
### Lag
Lag: the C version can handle upwards of 500 entities before encountering serious lag. This version can only handle
around 140. Part of this is likely just Python being inherently slower, but it is also likely due to my own
inexperience with Python programming. If someone could figure out a way to optimise this code, that would be good

(I'm talking minor optimisations, no fixing the lag by optimising collision detection by dividing the area into 
chunks or anything like that, it would get too complicated for the workshop T-T)

## 2D Pyshics Workshop

This is a simple simulation of 2D physics for a system of elastic collision between spheres.
This is intended for use in a workshop, essentially an hour long presentation teaching new to intermediate programmers how to create something like this. 

Operates using the formula for elastic collisions: 
### m<sub>1</sub>v<sub>1i</sub> + m<sub>2</sub>v<sub>2i</sub> = m<sub>1</sub>v<sub>1f</sub> + m<sub>2</sub>v<sub>2f</sub>

For simplicity, this program assumes all objects have a mass of 1, meaning the elastic collision formula becomes
### v<sub>1i</sub> + v<sub>2i</sub> = v<sub>1f</sub> + v<sub>2f</sub>

What this essentially means is that when two objects collide in this simulation, they swap velocities.

## Build instructions
Being python this should be very simple
### Dependencies
- Python compiler
- pygame

With pygame and all the included installed, simply compile and run main.py