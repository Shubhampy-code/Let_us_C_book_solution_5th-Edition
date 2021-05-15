"""Any character is entered through the keyboard, write a
program to determine whether the character entered is a
capital letter, a small case letter, a digit or a special symbol.
The following table shows the range of ASCII values for
various characters.
Characters ASCII Values
A – Z -- 65 – 90
a – z -- 97 – 122
0 – 9 -- 48 – 57
special symbols --   0 - 47, 58 - 64, 91 - 96, 123 - 127"""

asc=input("Give the Chracter ")
asc=(ord(asc))
if asc >= 65 and asc <= 90:
    print("Entred character is Capital latter.") 

elif asc >= 97 and asc <= 122:
    print("Entred character is small latter.")    

elif asc >= 48 and asc <= 57:
    print("Entred character is digit.")   

else:
    print("Entred character is special symbol.")    