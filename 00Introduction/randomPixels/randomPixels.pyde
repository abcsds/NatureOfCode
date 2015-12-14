size(400,360)
loadPixels()
for x in range(width):
    for y in range(height):
        bright = random(255)
        pixels[x+y*width] = color(bright)
updatePixels()