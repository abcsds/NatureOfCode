def setup():
    size(640, 360)
    background(0)

def draw():
    num  = float(randomGaussian())
    sd   = 60
    mean = 320

    x = sd * num + mean

    noStroke()
    fill(255, 10)
    ellipse(x, 180, 16, 16)