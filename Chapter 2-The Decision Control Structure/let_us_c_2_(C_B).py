"""Any integer is input through the keyboard. Write a program to
find out whether it is an odd number or even number. """

number=int(input("Enter the number:"))
Number=number%2
if (Number == 0):
    print("Entered number is even")
else:
    print("Entered number is odd")    