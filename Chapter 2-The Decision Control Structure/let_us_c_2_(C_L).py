"""Given a point (x, y), write a program to find out if it lies on the
x-axis, y-axis or at the origin, viz. (0, 0). """
x,y = input("Enter the point : ").split()
x = float(x)
y = float(y)
if ( x == 0) and (y == 0):
    print("point lies on origin")      
elif x == 0:
    print("Point lies on y-axis")
elif y == 0:
    print("point lies on x-axis")
else:
    print("Given point is not lies on origin and x,y axis")  