import turtle
import math
import time 
'''
x is your width
y is your height
z is your depth
'''
def rotate_x(point, angle):
   x,y,z = point
   y_new = y * math.cos(angle) - z * math.sin(angle)
   z_new = y * math.sin(angle) + z * math.cos(angle)
   return (x, y_new, z_new)
def rotate_y(point, angle):
   x, y, z = point
   x_new = x * math.cos(angle) - z * math.sin(angle)
   z_new = x * math.sin(angle) + z * math.cos(angle)
   return (x_new, y , z_new)
def rotate_z(point, angle):
   x,y,z = point
   x_new = x * math.cos(angle) - y * math.sin(angle)
   y_new = x * math.sin(angle) + y * math.cos(angle)
   return(x_new, y_new, z)
def project(point, scale=100, viewer_distance=3):
   x,y,z = point
   factor = scale / (z + viewer_distance)
   x_proj = x * factor
   y_proj = y * factor
   return (x_proj, y_proj)

original_points = [
   [-1,-1,-1], [1,-1,-1],
   [1,1,-1], [-1,1,-1],
   [-1,-1,1], [1,-1,1],
   [1,1,1], [-1,1,1]
]
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0), #back face
    (4, 5), (5, 6), (6, 7), (7, 4), #front Face
    (0, 4), (1, 5), (2, 6), (3, 7) # connections
]
points = original_points.copy()
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.color("black")
t.pensize(2)
t.speed(0)
t.hideturtle()
turtle.tracer(0,0)
frame = 0
max_frames = 500
while frame < max_frames:
   points = [rotate_y(p, 0.05) for p in points]
   frame += 1
   projected_points = [project(p) for p in points]
   t.clear()
   for edge in edges:
      p1 = projected_points[edge[0]]
      p2 = projected_points[edge[1]]
      t.penup()
      t.goto(p1[0], p1[1])
      t.pendown()
      t.goto(p2[0], p2[1])
   turtle.update()
turtle.done()
