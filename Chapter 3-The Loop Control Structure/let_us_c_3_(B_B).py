"""
 Write a program to find the factorial value of any number
entered through the keyboard. """

value=int(input("Enter the value : "))
factorialValue = 1
i=1
while (i <= value) :
    factorialValue = factorialValue * i
    i=i+1
print(factorialValue)



"""
number = int(input("Enter the number: "))
factorial_number = 1

while  number > 0:
    factorial_number = factorial_number * number
    number = number-1
print(factorial_number)
"""