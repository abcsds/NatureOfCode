def setup():
    size(600,360)
    global t
    t = 0.0

def draw():
    global t
    background(0)
    n = noise(t)
    x = map(n,0,1,0,width)
    ellipse(x,180,16,16)
    t += 0.01