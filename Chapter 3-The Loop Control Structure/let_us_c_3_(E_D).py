""" Write a program to generate all combinations of 1, 2 and 3
using for loop.
 """

i = 1
while(i<=3):
    j=1
    while(j<=3):
        k=1
        while(k<=3):
            if(i!=j and j!=k and k!=i):
                print(i,j,k)

            
            k=k+1
        j=j+1    
    i=i+1        
