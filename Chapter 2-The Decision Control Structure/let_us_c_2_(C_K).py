"""Given the coordinates (x, y) of a center of a circle and it’s radius,
write a program which will determine whether a point lies inside
the circle, on the circle or outside the circle.
(Hint: Use sqrt( ) and pow( ) functions) """
from math import sqrt
x,y = input("Enter the coordinates:").split()
x = float(x)
y = float(y)
radius = float(input("Enter yhe radius:"))
x1,y1 = input("give your point:").split()
x1 = float(x1)
y1 = float(y1)
dis_between_point = sqrt((x1-x)*(x1-x)+(y1-y)*(y1-y))
if dis_between_point < radius:
    print("Given point is lies inside circle")

else:
    print("Given point is lies outside the circle")    