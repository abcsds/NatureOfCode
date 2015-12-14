
def setup():
    global t
    size(400,360)
    noiseDetail(1,1)
    t = 0

def draw():
    global t
    noiseDetail(int(map(mouseX,0,width,0,10)),map(mouseY,0,height,0.01,2.00))
    loadPixels()
    xoff = 0.0
    for x in range(width):
        yoff = 0.0
        for y in range(height):
            r = map(noise(xoff,yoff,t),0.0,1.0,0,255)
            g = map(noise(xoff+5000,yoff+5000,t),0.0,1.0,0,255)
            b = map(noise(xoff+10000,yoff+10000,t),0.0,1.0,0,255)
            pixels[x+y*width] = color(r,g,b)
            yoff += 0.01
        xoff += 0.01
    updatePixels()
    t += 0.1