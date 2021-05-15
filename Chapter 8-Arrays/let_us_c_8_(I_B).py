"""If an array arr contains n elements,
 then write a program to check if arr[0] = arr[n-1], arr[1] = arr[n-2] and so on"""

from array import*
my_arrey = array('i',[0,1,7,3,4,5,6,7,8,0])
i=0
j=len(my_arrey)
while i<(len(my_arrey)/2):
    if my_arrey[i] == my_arrey[j-1]:
        print((str(my_arrey[i]))+ " , " +str(my_arrey[j-1])+" Element is same")
    else:
        print((str(my_arrey[i]))+ " , " +str(my_arrey[j-1])+" Element is not same")
    i=i+1
    j=j-1 