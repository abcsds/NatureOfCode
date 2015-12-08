class Walker():
    """Screen Walker"""
    def __init__(self):
        self.x = width/2
        self.y = height/2
    def display(self):
        stroke(0)
        point(self.x, self.y)
    def step(self):
        r = random(1)
        if r < 0.5:
            self.x += (mouseX-width/2)/(width)
            self.y += (mouseY-height/2)/(height)
        elif r < 0.625:
            self.x += 1
        elif r < 0.75:
            self.x -= 1
        elif r < 0.875:
            self.y += 1
        else:
            self.y -= 1
