class Walker():
    """Screen Walker"""
    def __init__(self):
        self.position = pVector(float(width/2),float(height/2))
    def display(self):
        stroke(0)
        point(self.x, self.y)
    def step(self):
        r = random(1)
        if r < 0.5:
            self.position.x += (mouseX-self.position.x)/(width)
            self.position.y += (mouseY-self.position.y)/(height)
        elif r < 0.625:
            self.position.x += 1
        elif r < 0.75:
            self.position.x -= 1
        elif r < 0.875:
            self.position.y += 1
        else:
            self.position.y -= 1
