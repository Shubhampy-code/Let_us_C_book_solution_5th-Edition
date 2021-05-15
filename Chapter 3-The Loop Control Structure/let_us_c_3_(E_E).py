"""According to a study, the approximate level of intelligence of
a person can be calculated using the following formula:
i = 2 + ( y + 0.5 x ) 

Write a program, which will produce a table of values of i, y
and x, where y varies from 1 to 6, and, for each value of y, x
varies from 5.5 to 12.5 in steps of 0.5 """

i=float(0)
y=int(1)


while y<=6:
    x=float(5.5)
    while x <= 12.5:
        i = 2 + ( y + 0.5 * x ) 
        print ( "i "+" = "+str(i)+ " for " + "y = "+str(y) + ", x = " + str(x) )
        x=x+0.5
    y=y+1