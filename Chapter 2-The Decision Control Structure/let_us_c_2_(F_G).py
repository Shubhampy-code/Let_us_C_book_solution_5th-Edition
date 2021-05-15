"""If the three sides of a triangle are entered through the
keyboard, write a program to check whether the triangle is
isosceles, equilateral, scalene or right angled triangle. """
side1 = float(input("length of 1st side of tringle : "))
side2 = float(input("length of 2nd side of tringle : "))
side3 = float(input("length of 3rd side of tringle : "))

if (side1+side2>side3) and (side2+side3>side1) and (side3+side1>side2):
    if (side1 == side2) or (side2 == side3) or (side3==side1):

        if (side1 == side2== side3):
            print("Tringle is equilateral")
        else:
            print("Tringle is isosceles") 

    elif (side1!=side2) and (side2 !=side3) and (side3 != side1):

        if  pow(side1,2)==pow(side2,2)+pow(side3,2) or pow(side2,2)==pow(side1,2)+pow(side3,2) or pow(side3,2)==pow(side2,2)+pow(side1,2) :
            print("Tringle is right angle and scalene")

        else:
            print("tringle is scalen")
else:
    print("Tringle is not valid")


