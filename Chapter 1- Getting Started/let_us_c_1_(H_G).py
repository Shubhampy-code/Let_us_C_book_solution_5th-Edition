""" If a five-digit number is input through the keyboard, write a
program to calculate the sum of its digits.
(Hint: Use the modulus operator ‘%’) """

number=input("Enter the five digits number:")
number=int(number)
sum = 0
while(number >0):
    sum = sum + number%10
    number =  int(number/10)

print(sum)