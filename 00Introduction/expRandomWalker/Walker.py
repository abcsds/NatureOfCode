class Walker():
    """Screen Walker"""
    def __init__(self):
        self.x = width/2
        self.y = height/2
    def display(self):
        stroke(0)
        point(self.x, self.y)
    def step(self):
        stepSize = self.montecarlo(20)
        stepx = random(-stepSize, stepSize)
        stepy = random(-stepSize, stepSize)
        self.x += stepx
        self.y += stepy
    def montecarlo(self, multiplier):
        while True:
            r1 = random(1)
            probability = exp(-r1) # Modified probability
            r2 = random(1)
            if r2 < probability:
                return r1 * multiplier
