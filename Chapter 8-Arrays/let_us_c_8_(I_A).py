"""Write a program to copy the contents of one array into another in the reverse order."""

from array import*
my_array = array('i',[1,44,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99,90])
my_new_array=[None]*len(my_array)
i=0
j=len(my_array)
while j>0:
    my_new_array[i] = my_array[j-1]
    j=j-1
    i=i+1
print(my_new_array)

    