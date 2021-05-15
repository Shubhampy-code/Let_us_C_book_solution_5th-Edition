"""Given three points (x1, y1), (x2, y2) and (x3, y3), write a
program to check if all the three points fall on one straight line. """
x1,y1=input("Enter the vale of X1 and Y1:").split()
x2,y2=input("Enter the vale of X2 and Y2:").split()
x3,y3=input("Enter the vale of X3 and Y3:").split()
x1=float(x1)
y1=float(y1)
x2=float(x2)
y2=float(y2)
x3=float(x3)
y3=float(y3)
area=(1/2)*( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )

if area==0:
    print("All the three points fall on one straight line")

else :
    print(" No points fall on one straight line")    
    
