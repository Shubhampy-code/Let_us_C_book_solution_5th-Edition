"""Write a program to add first seven terms of the following
series using a for loop:
1+ 2 + 3+  …….
1! 2! 3!  
"""

number = 1
series = 0
while number<=7:
    factorialValue = 1
    i=1
    while (i<= number):
        factorialValue = factorialValue * i
        i=i+1
    series = series+(number/ factorialValue)
    number=number+1
print(series)   





