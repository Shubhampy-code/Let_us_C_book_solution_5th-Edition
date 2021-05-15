"""Write a function that receives marks received by a student in 
3 subjects and returns the average and percentage of these marks.
Call this function from main( ) and print the results in main( )."""

def Percentage(math,physic,chemistry,max):
    average = ((math + physic + chemistry)/3)
    percentage = (((math + physic + chemistry)/max)*100)
    return average , percentage

    
     

Math = float(input("Enter the marks of mathes : "))
Phy = float(input("Enter the marks of physics : "))
Che = float(input("Enter the marks of chemistry : "))
max_marks = float(input("Enter the maximum total marks of 3 subject : "))
myAverage, My_per = Percentage(Math,Phy,Che,max_marks)
print("Average = " + str(myAverage))
print("Percentage = " + str(My_per)+ " %")
