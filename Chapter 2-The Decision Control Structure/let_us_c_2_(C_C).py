"""Any year is input through the keyboard. Write a program to
determine whether the year is a leap year or not.
(Hint: Use the % (modulus) operator)"""

year = int(input("Enter the year:"))
"""fir_cond = year%4 
sec_cond = year%100
third_cond = year%400"""

if (year%4==0) :
    if year%100!=0:
        print(" Entred Year is leep year")
    else:
        if (year%400 ==0):
            print("Entred year is leep year")
        else:
            print("Enterd year is not leep year")    

else:
    print("Entred Year is not leep year")