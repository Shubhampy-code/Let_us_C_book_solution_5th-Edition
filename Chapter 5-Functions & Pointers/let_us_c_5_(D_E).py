"""A positive integer is entered through the keyboard.
 Write a function to obtain the prime factors of this number.
For example, prime factors of 24 are 2, 2, 2 and 3, whereas prime factors of 35 are 5 and 7."""
def PrmFactor(num):
    #num = int(input("Enter the number : "))
    i = num
    j=2
    if num <2 :
        print (num)

    while i>1:
        if i%j==0 :
            i = i/j 
            print(j,end=" ")
        else:
            j=j+1

number=int(input("Enter your number for find out prime factor : "))
myprmfactor = PrmFactor( number )






       
    
