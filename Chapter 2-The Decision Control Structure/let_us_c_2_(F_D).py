""" A certain grade of steel is graded according to the following
conditions:
(i) Hardness must be greater than 50
(ii) Carbon content must be less than 0.7
(iii) Tensile strength must be greater than 5600
The grades are as follows:
Grade is 10 if all three conditions are met
Grade is 9 if conditions (i) and (ii) are met
Grade is 8 if conditions (ii) and (iii) are met
Grade is 7 if conditions (i) and (iii) are met
Grade is 6 if only one condition is met
Grade is 5 if none of the conditions are met
Write a program, which will require the user to give values of
hardness, carbon content and tensile strength of the steel
under consideration and output the grade of the steel"""
hardness = float(input("Enter the hardness of steel : "))
car_cont = float(input("Enter the carbon content of steel : "))
ten_str = float(input("Enter the tensile strength of steel : "))

hardness = (hardness >50 )
car_cont = (car_cont < 0.7)
ten_str = (ten_str > 5600)

if hardness and car_cont and ten_str:
    print("Grade of steel : 10 ") 

elif  hardness and car_cont :
    print("Grade of steel : 9")

elif car_cont and ten_str:
    print("Grade of steel : 8")

elif hardness and ten_str:
    print("Grade of steel : 7")

elif hardness or car_cont or ten_str:
    print("Grade of steel : 6")
else:
    print("Grade of steel : 5")    




