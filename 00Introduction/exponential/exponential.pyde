def setup():
    size(800,600)
    background(255)
def draw():
    x = random(1)
    y = exp(-x)
    print x, y
    ellipse(width*x,height-height*y,2,2)