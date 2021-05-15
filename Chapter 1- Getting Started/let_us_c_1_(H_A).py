Ramesh_basic_salary=input("Enter the Ramesh’s basic salary: ")
rameshsalary=float(Ramesh_basic_salary)
dearness_allowance=rameshsalary*(40/100)
house_rent_allowance=rameshsalary*(20/100)
gross_salary=rameshsalary + dearness_allowance + house_rent_allowance 
print("Gross Salary:"+ str(gross_salary))


"""Ramesh’s basic salary is input through the keyboard. His
dearness allowance is 40% of basic salary, and house rent
allowance is 20% of basic salary. Write a program to calculate
his gross salary"""