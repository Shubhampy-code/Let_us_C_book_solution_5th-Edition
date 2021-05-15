"""If the total selling price of 15 items and the total profit earned
on them is input through the keyboard, write a program to
find the cost price of one item. """
Amo_15_items = float(input("Enter the total selling price of 15 items:"))
total_profit = float(input("Enter the total profit earn:"))
amo_1_item = (Amo_15_items/15)
profit_1 = (total_profit/15)
cost_price = (amo_1_item-profit_1)
print("Cost price of one item:" + str(cost_price))