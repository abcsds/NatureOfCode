def setup():
    global randomCounts
    size(640,240)
    randomCounts = [0 for i in range(20)]

def draw():
    background(255)

    index = int(random(len(randomCounts)))
    randomCounts[index] += 1

    stroke(0)
    fill(175)
    w = width/len(randomCounts)
    for x in range(len(randomCounts)):
        rect(x*w, height-randomCounts[x], w-1, randomCounts[x])
