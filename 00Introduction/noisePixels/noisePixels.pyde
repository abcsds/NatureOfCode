size(400,360)
loadPixels()
for x in range(width):
    for y in range(height):
        bright = map(noise(x,y),0.0,1.0,0,255)
        pixels[x+y*width] = color(bright)
updatePixels()