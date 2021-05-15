"""If a four-digit number is input through the keyboard, write a
program to obtain the sum of the first and last digit of this
number."""
number=int(input("Enter the four digit number:"))
num1=number%10

num2=int(number/10)

num3=int(num2/100)

sum1_4=(num1+num3)
print("sum of the first and last digit of this number:" + str(sum1_4))