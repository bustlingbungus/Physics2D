# 2D Pyshics Workshop

This is a simple simulation of 2D physics for a system of elastic collision between circles.
This is intended for use in a workshop, essentially an hour long presentation teaching new to intermediate programmers how to create something like this. 

Operates using the formula for elastic collisions: 

### m<sub>1</sub>v<sub>1i</sub> + m<sub>2</sub>v<sub>2i</sub> = m<sub>1</sub>v<sub>1f</sub> + m<sub>2</sub>v<sub>2f</sub>

For simplicity, this program assumes all objects have a mass of 1, meaning the elastic collision formula becomes

### v<sub>1i</sub> + v<sub>2i</sub> = v<sub>1f</sub> + v<sub>2f</sub>

What this essentially means is that when two objects collide in this simulation, they swap velocities.

## Controls

Left clicking will create a new physics object centred at the mouse every frame left mouse is held. 
Right clicking will delete all physics objects within a certain radius of the mouse every frame right mouse is held.
The arrow keys can be used to change the direction of gravity. Press ```return``` to toggle gravity on/off.

## Build instructions

Being python this should be very simple

### Dependencies

- Python compiler
- pygame

With pygame and all the included files installed, simply compile and run main.py

If you do not have `pygame` (which cam be checked with `pip show pygame`), run this command:

``` bash
pip install pygame
```
