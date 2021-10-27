# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
t = trtl.Turtle()

import random as rand

#-----game configuration----
t.shape("turtle")
t.shapesize(1.5)
t.fillcolor("pink")
t.pencolor("pink")

#-----initialize turtle-----


#-----game functions--------
def change_position():
	t.penup()
	new_xpos = rand.randint(-200,200)
	new_ypos = rand.randint(-200,200)
	t.goto(new_xpos,new_ypos)
	

def t_clicked(x,y):
	change_position()


t.onclick(t_clicked)
#-----events----------------

wn = trtl.Screen()
wn.mainloop()