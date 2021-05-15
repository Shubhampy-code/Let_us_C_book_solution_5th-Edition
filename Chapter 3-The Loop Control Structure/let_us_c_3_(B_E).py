"""
Write a program to print out all Armstrong numbers between
1 and 500. If sum of cubes of each digit of the number is
equal to the number itself, then the number is called an
Armstrong number. For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5
* 5 ) + ( 3 * 3 * 3 )  """
"""If a five-digit number is input through the keyboard, write a
program to calculate the sum of its digits.
(Hint: Use the modulus operator ‘%’)"""
  
#number = int(input("Enter the number : "))
number =1
while(number <= 1000):
    num = number
    n3 = 0
    while num > 0:

        n =  num%10
        n3 =n3+ n*n*n
        num = int(num/10)
    if number==n3:
        print( str(number) + " is Armstrong number")


    number = number + 1  
    

        