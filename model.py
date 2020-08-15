import controller, sys
import model   # We need a reference to this module to pass it to update methods

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import Special
import random

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=

running = False
cycle_count = 0
balls=set()
remember = None

#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running,cycle_count,balls
    running = False
    cycle_count = 0
    balls = set()


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global running,cycle_count
    if running:
        update_all()
        running = False
    cycle_count += 1
    removal = [b.update(model) for b in balls]
    for stomach in removal:
        if stomach != None:
            for food in stomach:
                remove(food)
        
    


#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(kind):
    global remember
    remember = kind


#add the kind of remembered object to the simulation (or remove all objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    global balls, remember
    if remember == None: pass
    elif remember == 'Remove':
        rem = None
        for b in balls:
            if b._x-5<=x<=b._x+5 and b._y-5<=y<=b._y+5:
                rem = b
                break
        if rem != None: remove(rem)
    else: add(eval(remember+'('+str(x)+','+str(y)+')'))


#add simulton s to the simulation
def add(s):
    global balls, remember
    balls.add(s)


    

# remove simulton s from the simulation    
def remove(s):
    global balls, remember
    balls.discard(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    r = set()
    for b in balls:
        if p(b.get_location()) and not isinstance(b, Black_Hole): r.add(b)
    return r
            


#call update for every simulton in the simulation (pass each model)
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def update_all():
    global cycle_count, balls
    if running:
        cycle_count += 1
        removal = [b.update(model) for b in balls]
        for stomach in removal:
            if stomach != None:
                for food in stomach:
                    remove(food)
    

#delete every simulton being simulated from the canvas; next call display on every
#  simulton being simulated to add it back to the canvas, possibly in a new location, to
#  animate it; also, update the progress label defined in the controller
#this function should loop over one set containing all the simultons
#  and should not call type or isinstance: let each simulton do the
#  right thing for itself, without this function knowing what kinds of
#  simultons are in the simulation
def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for b in balls:
        b.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(len(balls))+" balls/"+str(cycle_count)+" cycles")
