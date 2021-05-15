"""If cost price and selling price of an item is input through the
keyboard, write a program to determine whether the seller has
made profit or incurred loss. Also determine how much profit
he made or loss he incurred."""

cost_price = float(input("Enter the cost price of an item:"))
Sell_price = float(input("Enter the selling price of an item:"))

prof_loss = float(Sell_price-cost_price)

if prof_loss > 0 : 
    print("Saller make profit")
    print("Profit Earn:" + str(prof_loss))

else:
    print("Saller is in loss")    
    print("Loss:" + str(prof_loss))