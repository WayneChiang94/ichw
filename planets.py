#!/usr/bin/env python
# coding: utf-8

# In[1]:


#用python的turtle库, 写一个程序 planets.py, 能仿真太阳系水金火木土地球6大行星围绕太阳的运行轨迹. 如下图所示:



#planets.py要符合基本的python 编程规范.

#提交:

#在自己的github的作业库ichw中建一个文件夹pyassign1,作业提交到这个文件夹中，本次作业的程序名为planets.py


# In[1]:


import turtle
window = turtle.Screen()

sol = turtle.Turtle()
sol.shape("circle")
sol.color("yellow")

mercury = turtle.Turtle()
mercury.shape("circle")
mercury.color("blue")
mercury.penup()
mercury.setpos(0,-58)
mercury.pendown()
mercury.speed(40)

venus = turtle.Turtle()
venus.shape("circle")
venus.color("orange")
venus.penup()
venus.setpos(87,0)
venus.pendown()
venus.left(90)
venus.speed(40)

for i in range(180):
    mercury.forward(2)
    mercury.left(2)
    venus.forward(1.5)
    venus.left(1)

turtle.done()
turtle.bye()


# In[2]:


import turtle
window = turtle.Screen()

sol = turtle.Turtle()
sol.shape("circle")
sol.color("yellow")

mercury = turtle.Turtle()
mercury.penup()
mercury.sety(-58)
mercury.pendown()
mercury.shape("circle")
mercury.color("blue")
mercury.circle(58)

venus = turtle.Turtle()
venus.shape("circle")
venus.color("orange")
venus.penup()
venus.setpos(87,0)
venus.pendown()
venus.left(90)
venus.circle(87,240)


turtle.done()
turtle.bye()


# In[ ]:





# In[ ]:




