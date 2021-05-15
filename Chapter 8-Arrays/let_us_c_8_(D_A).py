"""Twenty-five numbers are entered from the keyboard into an array.
The number to be searched is entered through the keyboard by the user.
Write a program to find if the number to be searched is present in the
array and if it is present, display the number of times it appears in the array."""
from array import*
my_array = array('i',[1,2,3,4,50,6,7,8,9,6,8,9,4,3,11,2,5,8,9,6,1,4,6,2,9])

Number = int(input("Enter the number : "))
count = 0
i=0
found = 0
while i < len(my_array):
    if Number==my_array[i] :
        count=count+1
        found=1
        
    i=i+1
if found ==1:
    print(str(Number)+" is present in array " +str(count)+" times.")
if found==0:
    print(str(Number)+" is not present in array ")
    