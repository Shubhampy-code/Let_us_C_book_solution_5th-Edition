"""A library charges a fine for every book returned late. For first
5 days the fine is 50 paise, for 6-10 days fine is one rupee and
above 10 days fine is 5 rupees. If you return the book after 30
days your membership will be cancelled. Write a program to
accept the number of days the member is late to return the
book and display the fine or the appropriate message. """
late= int(input("How many days late for returning the book : "))

if late <= 5:
    print("fine is 50 paise")

elif (late > 5) and (late <= 10):
    print(" fine is 1 rupee")

elif late > 10 and late <= 30:
    print("fine is 5 rupee")
elif late > 30 :
    print ("your mambership is cancelled")
