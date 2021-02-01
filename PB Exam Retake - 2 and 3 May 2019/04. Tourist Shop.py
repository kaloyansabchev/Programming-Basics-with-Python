budget = float(input())
product_name = input()
product_price = float(input())

money_left = budget
items = 0
total_products_price = 0

while money_left >= product_price:
    items += 1
    money_left -= product_price
    if items % 3 == 0:
        product_price = product_price - (product_price * 0.5)
    total_products_price += product_price
    product_name = input()
    if product_name == 'Stop' or product_name == '':
        print(f"You bought {items} products for {total_products_price:.2f} leva.")
        break
    product_price = float(input())

if product_name != 'Stop' or product_name == '':
    needed_money = product_price - money_left
    print("You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")
