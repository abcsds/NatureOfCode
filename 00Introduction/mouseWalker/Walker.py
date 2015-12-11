class Walker():
    """Screen Walker"""
    def __init__(self):
        self.x = float(width/2)
        self.y = float(height/2)
    def display(self):
        stroke(0)
        point(self.x, self.y)
    def step(self):
        r = random(1)
        if r < 0.5:
            self.x += (mouseX-self.x)/(width)
            self.y += (mouseY-self.y)/(height)
        elif r < 0.625:
            self.x += 1
        elif r < 0.75:
            self.x -= 1
        elif r < 0.875:
            self.y += 1
        else:
            self.y -= 1
