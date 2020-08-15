# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


# from PIL.ImageTk import PhotoImage
from prey import Prey
import random
import math


class Floater(Prey):
    radius = 5
     
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Floater.radius*2, Floater.radius*2, random.random()*math.pi*2, 5)

    def update(self, model):
        prob = random.random()
        if prob <= 0.30:
            supido = self.get_speed()
            anguru = self.get_angle()
            change = random.uniform(-0.5, 0.5)
            if 3 <= supido+change <= 7:
                self.set_velocity(supido+change, anguru+random.uniform(-0.5, 0.5))
            self.move()
        else:
            self.move()
        
    
    def display(self,canvas):
        canvas.create_oval(self._x-self._width/2,
                           self._y-self._height/2,
                           self._x+self._width/2,
                           self._y+self._height/2,
                           fill = 'red')

