size(400,360)
xoff = 0.0
loadPixels()
for x in range(width):
    yoff = 0.0
    for y in range(height):
        bright = map(noise(xoff,yoff),0.0,1.0,0,255)
        pixels[x+y*width] = color(bright)
        yoff += 0.01
    xoff += 0.01
updatePixels()