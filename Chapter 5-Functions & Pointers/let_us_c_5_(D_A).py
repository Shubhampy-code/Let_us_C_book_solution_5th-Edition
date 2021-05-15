"""Write a function to calculate the factorial value of any integer entered through the keyboard."""

def GetFactorial(num):
    i=num
    factorialVal = 1
    while i >=1:
        factorialVal=factorialVal*i
        i -= 1 
    return factorialVal
    

myNum = int(input("Get Number : "))
myFactorialValue =  GetFactorial(myNum)
print("factorial value of any integer : " + str(myFactorialValue))