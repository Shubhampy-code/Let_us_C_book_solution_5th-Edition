"""Write a program to print the multiplication table of the
number entered by the user. The table should get displayed in
the following form.
 29 * 1 = 29
 29 * 2 = 58 """

number=int(input("Enter the number : "))
i=1
while i<=10:
    table=number*i
    print(str(number)+" * "+str(i)+" = "+str(table))
    i=i+1
 