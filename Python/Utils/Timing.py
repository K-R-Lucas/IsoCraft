class Timer:
    def __init__(self, tickrate):
        self.tps = tickrate
        self.dt = 1.0/self.tps
        self.ft = 0
        self.t = 0

    def accumulate(self, frametime):
        self.ft = frametime
        self.t += frametime

    def tick(self):
        c = self.t >= self.ft

        if c:
            self.t -= self.dt
            return True
        
        return False


