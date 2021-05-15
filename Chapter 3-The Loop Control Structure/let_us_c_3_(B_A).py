"""Write a program to calculate overtime pay of 10 employees.
Overtime is paid at the rate of Rs. 12.00 per hour for every
hour worked above 40 hours. Assume that employees do not
work for fractional part of an hour."""
employe = 1
while employe <=10 :
    
    time = int(input("working hours by employe : "))
    overtime = time - 40
    if overtime > 0: 
        pay = overtime *12
        print("overtime pay  " +  str(pay))
    else:
        print("overtime pay is zero because you are not working greater then 40 hours")    
    employe = employe + 1






