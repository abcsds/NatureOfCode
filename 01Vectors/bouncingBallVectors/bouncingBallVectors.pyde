location = PVector(100, 100)
volocity = PVector(1.0, 3.3)

def setup():
    size(640,360)
    background(255)

def draw():
    global location, volocity
    background(255)

    location.add(volocity)

    if location.x > width or location.x < 0:
        volocity.x = volocity.x * -1
    if location.y > height or location.y < 0:
        volocity.y = volocity.y * -1

    stroke(0)
    fill(175)

    ellipse(location.x,location.y,16,16)