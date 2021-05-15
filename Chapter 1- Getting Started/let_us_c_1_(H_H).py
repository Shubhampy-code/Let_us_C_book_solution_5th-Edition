"""If a five-digit number is input through the keyboard, write a
program to reverse the number. """

number=int(input("Enter the five digit number:"))

new_number=0
while (number>0):
    new_number = str(new_number) + str(number%10)
    number=int(number/10)
new_number=int(new_number)    
print(new_number)
