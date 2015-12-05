x, y = 100, 100
xspeed, yspeed = 1.0, 3.3

def setup():
    size(640,360)
    background(255)

def draw():
    global x, y, xspeed, yspeed 
    background(255)

    x = x + xspeed
    y = y + yspeed

    if x > width or x < 0:
        xspeed = xspeed * -1
    if y > height or y < 0:
        yspeed = yspeed * -1

    stroke(0)
    fill(175)

    ellipse(x,y,16,16)