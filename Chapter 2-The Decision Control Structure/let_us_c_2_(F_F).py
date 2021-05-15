"""If the three sides of a triangle are entered through the
keyboard, write a program to check whether the triangle is
valid or not. The triangle is valid if the sum of two sides is
greater than the largest of the three sides. """
side1 = float(input("Enter the first side of tringle : "))
side2 = float(input("Enter the second side of tringle : "))
side3 = float(input("Enter the third side of tringle : "))
"""
if (side1 > side2) and (side1 > side3):
    if  (side2 + side3 > side1):
       print("Tringle is valid")
    else:
        print("Tringle is not valid")

elif (side2 > side1) and (side2 > side3) :
    if (side1 + side3 > side2):
        print("Tringle is valid")
    else :
        print("Tringle is not vaild") 
elif (side3> side1) and (side3> side2):
    if (side1 + side2 > side3):
        print("Tringle is valid")
    else:
        print("Tringle is not valid")
elif (side1 == side2 == side3):
    print("Tringle is  valid")
"""

"""
if (side1+side2>side3) and (side2+side3>side1) and (side3+side1>side2):
    print("Tringle is valid")

else:
    print("tringle is not valid")
"""

if (side1 >= side2) and (side1 >= side3):
    MaxSide = side1
    SumOfOherTwo  = side2 + side3
elif (side2 >= side1) and (side2 >= side3):
    MaxSide = side2
    SumOfOherTwo  = side1 + side3
elif (side3 >= side1) and (side3 >= side2):
    MaxSide = side3
    SumOfOherTwo  = side1 + side3

if(MaxSide < SumOfOherTwo):
    print("Tringle is valid")
else:
    print("tringle is not valid")