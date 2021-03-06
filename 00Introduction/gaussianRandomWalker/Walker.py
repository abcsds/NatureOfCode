class Walker():
    """Screen Walker"""
    def __init__(self):
        self.x = width/2
        self.y = height/2
    def display(self):
        stroke(0)
        point(self.x, self.y)
    def step(self):
        sd = 3
        mean = 10
        stepSize = randomGaussian() * sd + mean
        stepx = random(-stepSize, stepSize)
        stepy = random(-stepSize, stepSize)
        self.x += stepx
        self.y += stepy
