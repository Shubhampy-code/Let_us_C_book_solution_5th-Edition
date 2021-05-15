"""If the ages of Ram, Shyam and Ajay are input through the
keyboard, write a program to determine the youngest of the
three. """
ram_age= int (input("Enter the age of Ram:"))
shyam_age = int(input("Enter the age of Shyam:"))
ajay_age=int(input("Enter the age of Ajay:"))
if (ram_age) < (shyam_age) and (ram_age)< (ajay_age):
    print("Ram is youngest")
elif (shyam_age) < (ram_age) and (shyam_age)< (ajay_age):
    print("Shyam is youngest")
else :
    print("Ajay is youngest")    