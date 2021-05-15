"""Twenty-five numbers are entered from the keyboard into an array. 
Write a program to find out how many of them are positive, 
how many are negative, how many are even and how many odd."""

from array import*
my_array = array('i',[1,2,3,4,50,6,7,8,9,6,8,-9,4,-3,11,-2,5,-8,9,6,-1,4,6,2,9])
i=0
odd=0
even=0
positive=0
negative=0
lenth = len(my_array)
while i<len(my_array):
    if my_array[i]>0:
        positive=positive+1
    elif my_array[i]< 0 :
        negative=negative+1

    if ((my_array[i])%2 == 0):
        even=even+1
    elif((my_array[i])%2 != 0):
        odd = odd+1

    i=i+1
print("Positive number is present in array : " +str(positive))
print("Negative number is present in array : " +str(negative))
print("Even number is present in array : " +str(even))
print("Odd number is present in array : " +str(odd))