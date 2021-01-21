budget = int(input())
season = input()
number_of_people = int(input())

boat_price = 0
discount_price = 0

if season == 'Spring':
    boat_price = 3000
    if number_of_people <= 6:
        discount_price = boat_price - (boat_price * 0.1)
    elif 7 <= number_of_people <= 11:
        discount_price = boat_price - (boat_price * 0.15)
    elif number_of_people >= 12:
        discount_price = boat_price - (boat_price * 0.25)
    if number_of_people % 2 == 0:
        discount_price = discount_price - (discount_price * 0.05)
elif season == 'Summer':
    boat_price = 4200
    if number_of_people <= 6:
        discount_price = boat_price - (boat_price * 0.1)
    elif 7 <= number_of_people <= 11:
        discount_price = boat_price - (boat_price * 0.15)
    elif number_of_people >= 12:
        discount_price = boat_price - (boat_price * 0.25)
    if number_of_people % 2 == 0:
        discount_price = discount_price - (discount_price * 0.05)
elif season == 'Autumn':
    boat_price = 4200
    if number_of_people <= 6:
        discount_price = boat_price - (boat_price * 0.1)
    elif 7 <= number_of_people <= 11:
        discount_price = boat_price - (boat_price * 0.15)
    elif number_of_people >= 12:
        discount_price = boat_price - (boat_price * 0.25)
elif season == 'Winter':
    boat_price = 2600
    if number_of_people <= 6:
        discount_price = boat_price - (boat_price * 0.1)
    elif 7 <= number_of_people <= 11:
        discount_price = boat_price - (boat_price * 0.15)
    elif number_of_people >= 12:
        discount_price = boat_price - (boat_price * 0.25)
    if number_of_people % 2 == 0:
        discount_price = discount_price - (discount_price * 0.05)
money_left = budget - discount_price
if budget >= discount_price:
    print(f'Yes! You have {abs(money_left):.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(money_left):.2f} leva.')