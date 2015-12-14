def setup():
    global t
    t = 0.0

def draw():
    global t
    n = noise(t)
    print n
    # t += 0.01
    t += 1