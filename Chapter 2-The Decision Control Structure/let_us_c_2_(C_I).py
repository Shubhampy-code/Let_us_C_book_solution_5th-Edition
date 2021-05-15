"""Given the length and breadth of a rectangle, write a program to
find whether the area of the rectangle is greater than its
perimeter. For example, the area of the rectangle with length = 5
and breadth = 4 is greater than its perimeter. """
length=float(input("Enter the lenght of rectangle:"))
breadth=float(input("Enter the breadth of rectangle:"))
area= length*breadth
perimeter=2*(length+breadth)

if area>perimeter:
    print("Area of rectangle is greter then its perimeter")

else:
    print("perimeter of rectangle is greater then its area ")    