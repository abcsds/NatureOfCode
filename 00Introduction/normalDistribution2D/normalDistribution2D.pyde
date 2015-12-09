def setup():
    size(640, 360)
    background(0)

def draw():
    numx  = float(randomGaussian())
    numy  = float(randomGaussian())
    numr = int(randomGaussian())
    numg = int(randomGaussian())
    numb = int(randomGaussian())

    x = width/5 * numx + width/2
    y = height/5 * numy + height/2
    r = 255/5 * numr + 255/2
    g = 255/5 * numg + 255/2
    b = 255/5 * numb + 255/2

    noStroke()
    fill(r, g, b, 10)
    ellipse(x, y, 16, 16)
