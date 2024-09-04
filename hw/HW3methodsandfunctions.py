class House:
    def __init__(self, size, color='white'):
        self.size = size
        self.color = color
        
    def build_expansion(self, addition):
        self.size += addition
home = House(2000)