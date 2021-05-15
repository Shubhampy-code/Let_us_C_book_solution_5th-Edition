"""Find the absolute value of a number entered through the
keyboard. """
value=float(input("Enter the number:"))
if value>0:
    print("Absolute value is:" + str(value))

else:
    print("Absolute value is:" + str(value*(-1)))
    
