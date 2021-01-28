money = float(input())
gender = input()
age = int(input())
sport = input()

cost = 0
discount_prize = 0

if sport == "Gym":
    if gender == "m":
        cost = 42
    elif gender == "f":
        cost = 35
elif sport ==  "Boxing":
    if gender == "m":
        cost = 41
    elif gender == "f":
        cost = 37
elif sport ==  "Yoga":
    if gender == "m":
        cost = 45
    elif gender == "f":
        cost = 42
elif sport ==  "Zumba":
    if gender == "m":
        cost = 34
    elif gender == "f":
        cost = 31
elif sport ==  "Dances":
    if gender == "m":
        cost = 41
    elif gender == "f":
        cost = 53
elif sport ==  "Pilates":
    if gender == "m":
        cost = 39
    elif gender == "f":
        cost = 37

if age <= 19:
    discount_prize = cost * 0.8
else:
    discount_prize = cost

needed = discount_prize - money
if discount_prize <= money:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${needed:.2f} more.")