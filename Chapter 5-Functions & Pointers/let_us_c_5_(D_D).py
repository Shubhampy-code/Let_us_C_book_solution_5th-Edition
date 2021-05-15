"""Any year is entered through the keyboard. Write a function to 
determine whether the year is a leap year or not."""
def leapyear(year):
    #year = int(input("Enter the year:"))
    if (year%4==0) :
        if year%100!=0:
            st = " Entred Year is leap year"
            return(st)
        else:
            if (year%400 ==0):
                st = "Entred year is leap year"
                return(st)
            else:
                st="Enterd year is not leap year"
                return(st)    

    else:
        st="Entred Year is not leap year"
        return(st)


Year = int(input("Enter the year : "))
myyear = leapyear(Year)
print(myyear)