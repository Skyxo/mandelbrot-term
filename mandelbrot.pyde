from random import *
from cmath import *

width, height = 800, 800
precision = 250
nbr = 2000

zoom = 0

f = 100
x, y = 0, 0
zoomspeed = 3

def new_lst():
    global nbr
    return [complex(-uniform((x+float(width/2))/float(f), (x+float(-width/2))/float(f)), -uniform((y+float(height/2))/float(f), (y+float(-height/2))/float(f))) for i in range(nbr)]

def calcul(list_):
    finallist_ = []
    
    for i in range(len(list_)):
        z = list_[i]
        
        o = 0
        while z.real**2+z.imag**2 <= 5 and o < precision:
            z = z**2 + list_[i]
            o+=1
        
        if o >= 3:
            finallist_.append((list_[i], o))

    return finallist_

#mandelbrot_ = calcul([complex(uniform(-2, 0.5), uniform(-1.15, 1.15)) for i in range(nbr)])
mandelbrot_ = calcul(new_lst())

def setup():
    size(width, height)
    textSize(23)
    smooth()
    rectMode(CENTER)

def draw():
    global mandelbrot_, f, x, y

    background(0)
    
    translate(x, y)
    translate(width/2, height/2)
    
    """
    line(-1000, 0, 1000, 0)
    line(0, -1000, 0, 1000)
    
    for i in range(-10, 10):
        circle(i*f, 0, 5)
        circle(0, i*f, 5)
        text(i, i*f, -10)
        text(i, 10, i*f)
    """

    for i in range(len(mandelbrot_)):
        stroke(mandelbrot_[i][1]*255/precision)
        point(mandelbrot_[i][0].real*float(f), mandelbrot_[i][0].imag*float(f))
        
    translate(-x, -y)
    translate(-width/2, -height/2)
    
    text("x : {}, y : {}".format(-(x+float(width/2-mouseX))/float(f), (y+float(height/2-mouseY))/float(f)), 30, 30)
    text("zoom : {}".format(zoom), 30, 55)
              
def mousePressed():
    global f, x, y, zoomspeed, zoom, mandelbrot_, nbr
    
    button = mouseButton
    
    if button == LEFT:
        x += width/2-mouseX
        y += height/2-mouseY
        x *= zoomspeed
        y *= zoomspeed
        f *= zoomspeed
        zoom += 1
        
    if button == RIGHT:
        x -= width/2-mouseX
        y -= height/2-mouseY
        x /= zoomspeed
        y /= zoomspeed
        f /= zoomspeed
        zoom -= 1
        
    mandelbrot_ = calcul(new_lst())
        
def keyPressed():
    global mandelbrot_, nbr, precision
    
    if key == " ":
        mandelbrot_ = calcul()
        print("Recalcul effectué")
        
    if key == "r":
        nbr+=100
        mandelbrot_ = calcul(new_lst())
        print("Nombre :",nbr)
        
    if key == "f":
        nbr-=100
        mandelbrot_ = calcul(new_lst())
        print("Nombre :",nbr)
        
    if key == "p":
        precision+=10
        mandelbrot_ = calcul(new_lst())
        print("precision :",precision)
        
    if key == "m":
        precision-=10
        mandelbrot_ = calcul(new_lst())
        print("precision :",precision)
