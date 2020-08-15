# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    radius = 10
    
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        self.counter = 30
         
    def update(self, model):
        self.counter -= 1
        if self.counter == 0:
            self.change_dimension(-1, -1)
            self.counter = 30
        ate = model.find(self.contains)
        for food in ate:
            self.change_dimension(1, 1)
        if self.get_dimension() == (0,0):
            ate.add(self)
        return ate
            
        
             
        
