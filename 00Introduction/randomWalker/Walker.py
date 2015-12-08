class Walker():
    """Screen Walker"""
    def __init__(self):
        self.x = width/2
        self.y = height/2
    def display(self):
        stroke(0)
        point(self.x, self.y)
    def step(self):
        stepx = random(-1, 1)
        stepy = random(-1, 1)
        self.x += stepx
        self.y += stepy
