"""Write a function which receives a float and an int from main( ), 
finds the product of these two and returns the product which is printed through main( )."""

def Product(FirstNumber,SecNumber):
    product = FirstNumber  * SecNumber
    return product

firstNum,secNum = input("Enter the first and second number : ").split()
firstNum = float(firstNum)
secNum = float(secNum)
multiply = Product(firstNum,secNum)
print("Product of first and second number : "+ str(multiply))