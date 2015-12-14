def setup():
    size(400,300)
    global noiseScale
    noiseScale = 0.02

def draw():
    global noiseScale
    background(0)
    for x in range(width):
        noiseVal = noise((mouseX+x)*noiseScale, mouseY*noiseScale)
        stroke(noiseVal*255)
        line(x, mouseY+noiseVal*80, x, height)
