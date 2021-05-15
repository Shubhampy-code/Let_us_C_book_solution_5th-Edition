"""Write a general-purpose function to convert any given year into its roman equivalent.
 The following table shows the roman equivalents of decimal numbers:
 Decimal   Roman
 1         i
100        c
5          v
500        d
10         x
1000       m
50         l
 """
def RomYearEqu(year):
#year = int(input("Enter the year : "))
    currentYear = year
    
    while currentYear >=1000:
        currentYear = currentYear-1000
        print ("m",end="")
    while currentYear >= 500:
        currentYear = currentYear-500
        print("d",end="")
    while currentYear>=100:
        currentYear = currentYear-100
        print("c",end="")
    while currentYear>=50:
        currentYear = currentYear-50
        print("l",end="")
    while currentYear>=10:
        currentYear = currentYear-10
        print("x",end="")
    while currentYear>=5:
        currentYear = currentYear-5
        print("v",end="")
    while currentYear >=1:
        currentYear = currentYear-1
        print("i",end="")


Year=int(input("Enter the year : "))
MyRomYear = RomYearEqu(Year)