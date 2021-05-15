"""A cashier has currency notes of denominations 10, 50 and
100. If the amount to be withdrawn is input through the
keyboard in hundreds, find the total number of currency notes
of each denomination the cashier will have to give to the
withdrawer"""


amount=int(input("Please enter your amount: "))

if (amount%100 == 0) and (amount>=100) :
    hundred = (amount-100)
    hund_note = int(hundred/100)
    print("100 : "+ str(hund_note) + " Notes")
    print("50 : 1 Note")
    print("10 : 5 Notes")
   
else:
    print("Enter your amount in hundreds and more then and equal to 200")
