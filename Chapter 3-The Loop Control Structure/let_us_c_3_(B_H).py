"""Write a program to find the octal equivalent of the entered
number"""
#reminder = 1
number = int(input("Enter the numbre : "))
num = number
count = 0
octal = 0
while num > 0:
    reminder = num%8
    num = int(num/8)
    octal = reminder * pow(10,count) + octal
    count = count + 1

print(octal)
