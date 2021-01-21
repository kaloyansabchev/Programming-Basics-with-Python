flowers = input()
quantity = int(input())
budget = int(input())

price = 0
discount = 0
if flowers == 'Roses':
    if quantity > 80:
        discount = quantity * 5 * 0.1
        price = quantity * 5 - discount
    else:
        price = quantity * 5
elif flowers == 'Dahlias':
    if quantity > 90:
        discount = quantity * 3.8 * 0.15
        price = quantity * 3.8 - discount
    else:
        price = quantity * 3.8
elif flowers == 'Tulips':
    if quantity > 80:
        discount = quantity * 2.8 * 0.15
        price = quantity * 2.8 - discount
    else:
        price = quantity * 2.8
elif flowers == 'Narcissus':
    if quantity < 120:
        discount = quantity * 3 * 0.15
        price = quantity * 3 + discount
    else:
        price = quantity * 3
elif flowers == 'Gladiolus':
    if quantity < 80:
        discount = quantity * 2.5 * 0.2
        price = quantity * 2.5 + discount
    else:
        price = quantity * 2.5

money_left = budget - price
if budget >= price:
    print(f"Hey, you have a great garden with {quantity} {flowers} and {abs(money_left):.2f} leva left.")
else:
    print(f"Not enough money, you need {abs(money_left):.2f} leva more.")