"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = 0.1
    else:
        bonus = 0.15
    print(bonus)

for i in range(0,101,10):
    print(i)
for i in range(1,21,-1):
    print(i)

DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1
total_price = 0
item_num = int(input("Number of items:"))
while item_num < 0:
    print('Invalid')
    item_num = int(input("Number of items:"))
for i in range(item_num):
    item_price = float(input("Price of item:$"))
    total_price += item_price
if total_price > DISCOUNT_THRESHOLD:
    total_price *= DISCOUNT_RATE
print(f"Total price for {item_num} is ${total_price:.2f}")


