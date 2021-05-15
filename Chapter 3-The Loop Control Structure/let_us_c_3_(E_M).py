""" The natural logarithm can be approximated by the following
series.
If x is input through the keyboard, write a program to
calculate the sum of first seven terms of this series. """

valueOfX = float(input("Enter the value of x : "))
pow_of_x = 2
series = 0
while pow_of_x <= 7:
    series = series + (1/2)*pow(((valueOfX-1)/valueOfX),pow_of_x)
    pow_of_x = (pow_of_x + 1)
series = series + ((valueOfX-1)/valueOfX)
print("The sum of first seven terms of this series is : " + str(series))


