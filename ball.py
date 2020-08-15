# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).

from prey import Prey
import random, math

def random_angle():
    # between 0 and 2pi
    return random.random()*math.pi*2

class Ball(Prey): 
    radius = 5
     
    def __init__(self, x, y):
        Prey.__init__(self, x, y, Ball.radius*2, Ball.radius*2, random.random()*math.pi*2, 5)

    def update(self, model):
        self.move()
        
    
    def display(self,canvas):
        canvas.create_oval(self._x-self._width/2,
                           self._y-self._height/2,
                           self._x+self._width/2,
                           self._y+self._height/2,
                           fill = 'blue')
 

