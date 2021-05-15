"""
Write a program which performs the following tasks:
− initialize an integer array of 10 elements in main( )
− pass the entire array to a function modify( )
− in modify( ) multiply each element of array by 3
− return the control to main( ) and print the new array elements in main( )
"""
def MultipuleArray(My_Array):
    i=0
    while i<len(My_Array):
        My_Array[i] =3 * My_Array[i]
        i=i+1
    return (My_Array)

from array import*
my_array = array('i',[4,2,5,1,6,9,8])
multiplyBy3 = MultipuleArray(my_array)
print(multiplyBy3)



