# The Simulton is derived from both Hunter and Mobile_Simulton
# It is "Special" because it frequently changes colours
# AND is repelled by any Mobile_Simultons
# Meaning it will change its direction to actually run from any Prey
# It is derived from Hunter because it needs to find all nearby Mobile_Simultons
# And is derived from Mobile Simulton because it moves and constantly updates

from hunter import Hunter
from mobilesimulton import Mobile_Simulton
from math import pi, atan2
from random import random, choice


class Special(Hunter, Mobile_Simulton):
    range = 50
    radius = 10
    
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, Special.radius*2, Special.radius*2, random()*pi*2, 20)
    
    def update(self, model):
        def seek(xy):
            return self.distance(xy) <= Special.range
        go_away = model.find(seek)
        if len(go_away)!=0:
            closest = min([self.distance(mark.get_location()) for mark in go_away])
            for mark in go_away:
                if closest == self.distance(mark.get_location()):
                    lock = mark
            trail = atan2(self._y-lock._y, self._x-lock._x)
            self.set_angle(trail)
        self.move()

    def display(self,canvas):
        canvas.create_oval(self._x-self._width/2,
                           self._y-self._height/2,
                           self._x+self._width/2,
                           self._y+self._height/2,
                           fill = choice(["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"]))