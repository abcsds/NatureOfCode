import Walker

def setup():
    size(640, 360)
    background(255)
    global w
    w = Walker.Walker()


def draw():
    global w
    w.step()
    w.display()