"""Write a program to check whether a triangle is valid or not,
when the three angles of the triangle are entered through the
keyboard. A triangle is valid if the sum of all the three angles
is equal to 180 degrees. """
print("In triangle ABC")
ang_a=float(input("Enter the angle A:"))
ang_b=float(input("Enter the angle B:"))
ang_c=float(input("Enter the angle C:"))
if (ang_a + ang_b + ang_c == 180):
    print("Triangle is valid")
else:
    print("tringle is not valid")    