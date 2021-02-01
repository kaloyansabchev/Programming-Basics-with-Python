budget = float(input())
petrol_l_needed = float(input())
day = input()

petrol_price = petrol_l_needed * 2.1
total_needed = petrol_price + 100
discount_price = 0

if day == 'Sunday':
    discount_price = total_needed - (total_needed * 0.2)
elif day == "Saturday":
    discount_price = total_needed - (total_needed * 0.1)

money_left = budget - discount_price

if budget >= discount_price:
    print(f"Safari time! Money left: {abs(money_left):.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {abs(money_left):.2f} lv.")