income = int(input())

money_in = 0

while True:
    drink_name = input()
    if drink_name == "Party!":
        needed_money = income - money_in
        print(f"We need {needed_money:.2f} leva more.")
        break
    quantity_drinks = int(input())
    price = len(drink_name) * quantity_drinks
    if price % 2 != 0:
        price *= 0.75
    money_in += price
    if money_in >= income:
        print(f"Target acquired.")
        break
print(f"Club income - {money_in:.2f} leva.")