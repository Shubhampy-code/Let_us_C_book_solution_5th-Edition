"""Write a program to print all prime numbers from 1 to 300.
(Hint: Use nested loops, break and continue)"""

number = 2
while number<=500:
    prime = 1
    num = 2
    while num < number:
        if(number % num == 0): 
            prime = 0
            break
        num = num + 1
        
    if(prime == 1):
        print (str(number) + " is prime")

    number = number + 1
