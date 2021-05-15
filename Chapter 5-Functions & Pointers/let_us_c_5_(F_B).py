"""Write a function that receives 5 integers and returns the sum,
 average and standard deviation of these numbers.
  Call this function from main( ) and print the results in main( )."""


def StdDevi(First,Second,Third,Fourth,Fifth):
    sum = First+Second+Third+Fourth+Fifth
    average = (sum/5)
    First = pow((Fifth-average),2)
    Second = pow((Second-average),2)
    Third = pow((Third-average),2)
    Fourth = pow((Fourth - average),2)
    Fifth = pow((Fifth - average),2)
    Sum =  First+Second+Third+Fourth+Fifth
    N_1 = ((1/4) * Sum)
    stdDeviation = pow((N_1),(1/2))
    return sum , average , stdDeviation


first = int(input("Enter the first integer : "))
second = int(input("Enter the second integer : "))
third = int(input("Enter the third integer : "))
fourth = int(input("Enter the fourth integer : "))
fifth = int(input("Enter the fifth  integer : ")) 
My_sum, My_avg, My_StdD = StdDevi(first,second,third,fourth,fifth)
print("Sum = " + str(My_sum))
print("Average = " + str(My_avg))
print("Standard Deviation = " + str(My_StdD))
