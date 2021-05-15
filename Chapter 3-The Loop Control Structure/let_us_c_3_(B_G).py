"""Write a program to enter the numbers till the user wants and
at the end it should display the count of positive, negative and
zeros entered."""
Positive = 0
negative = 0
zero = 0
play = "yes"
while play == "yes":
    number= float(input("Enter the number : "))
    if number > 0 :
        Positive = Positive + 1
        
    elif number < 0:
        negative = negative + 1
        
    else:
        zero = zero + 1
         

    play = input("Do you want to enter more : ")   

print("Count of Positive : "+str(Positive))
print("Count of Negative : "+str(negative))
print("Count of Zero : "+str(zero))
    