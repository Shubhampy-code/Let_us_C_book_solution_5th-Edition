"""If a five-digit number is input through the keyboard, write a
program to print a new number by adding one to each of its
digits. For example if the number that is input is 12391 then
the output should be displayed as 23402. """

number=int(input("Enter the five digit number:"))

new_number=0
while (number>0):
    digit = number%10
    new_digit = digit +1
    if(new_digit == 10):
        new_digit = 0
        
    new_number = str(new_digit) + str(new_number)
    number=int(number/10)
    

#new_number=int(new_number)   
#new_number=int(new_number/10 )
print(int(int(new_number)/10))
