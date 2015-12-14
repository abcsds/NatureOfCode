
def setup():
    global xoff
    xoff = float(0.0)

def draw():
    global xoff
    background(255)
    xoff += 0.01
    n = noise(xoff) * width
    line(n, 0, n, height)
