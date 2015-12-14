class Walker():
    """Screen Walker"""
    def __init__(self):
        self.x = float(width/2)
        self.y = float(height/2)

        self.tx = 0
        self.ty = 10000

    def display(self):
        stroke(0)
        point(self.x, self.y)
    def step(self):
        self.x += map(noise(self.tx), 0 ,1 ,-2, 2)
        self.y += map(noise(self.ty), 0 ,1 ,-2, 2)
        self.tx += 0.01
        self.ty += 0.01
