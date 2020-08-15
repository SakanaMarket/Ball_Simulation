# Hunter is derived from the Mobile_Simulton/Pulsator classes: i.e., it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import pi, atan2
from random import random


class Hunter(Pulsator, Mobile_Simulton):
    range = 200
    
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, x*2, y*2, random()*pi*2, 5)
        Pulsator.__init__(self, x, y)
    
    def update(self, model):
        def seek(xy):
            return self.distance(xy) <= Hunter.range
        
        target = model.find(seek)
        if len(target)!=0:
            closest = min([self.distance(mark.get_location()) for mark in target])
            for mark in target:
                if closest == self.distance(mark.get_location()):
                    lock = mark
            trail = atan2(lock._y-self._y, lock._x-self._x)
            self.set_angle(trail)
        self.move()
        Pulsator.update(self, model)
        ate = model.find(self.contains)
        if self.get_dimension() == (0,0):
            ate.add(self)
        return ate
        
