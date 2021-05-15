"""Write a function power ( a, b ), to calculate the value of a raised to b."""

def Getpower(a, b):
    #num,power = input("enter the value of a and b : ").split()
    num = float(a)
    power = int(b)
    pow = 1 
    while power>=1:
        pow = pow*num
        power = power-1
    return pow

x,y = input("Enter the number and it's power : ").split()
mypow = Getpower(x, y)
print(" the value of a raised to b : " + str(mypow))
