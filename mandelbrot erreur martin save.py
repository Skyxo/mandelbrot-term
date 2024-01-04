from random import *

width, height = 800, 800

def setup():
    size(width, height)
    textSize(23)
    smooth()
    rectMode(CENTER)

mandelbrot_ = []
    
clist_ = []
for i in range(100000):
    clist_.append([uniform(-2, 1), uniform(-1.5, 1.5)])
    
for i in range(len(clist_)):
        z = clist_[i]
    
        for o in range(7):
            z[0] = z[0]**2 - z[1]**2 + clist_[i][0]
            z[1] = 2*z[0]*z[1] + clist_[i][1]
        
        if z[0]**2+z[1]**2 <= 10:
            mandelbrot_.append(clist_[i])

f = 100
x, y = 0, 0
zoomspeed = 1.5

def draw():
    global mandelbrot_, j, f, x, y
    
    background(0)
    
    translate(x, y)
    translate(width/2, height/2)
    
    stroke(255)
    for i in range(len(mandelbrot_)):
        point(mandelbrot_[i][0]*f, mandelbrot_[i][1]*f)
    
def mousePressed():
    global f, x, y, zoomspeed
    button = mouseButton
    
    if button == LEFT:
        x += width/2-mouseX
        y += height/2-mouseY
        x *= zoomspeed
        y *= zoomspeed
        f *= zoomspeed
    if button == RIGHT:
        x -= width/2-mouseX
        y -= height/2-mouseY
        x /= zoomspeed
        y /= zoomspeed
        f /= zoomspeed