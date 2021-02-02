budget = float(input())
destination = input()
season = input()
days = int(input())

prize_per_day = 0

if destination == 'Dubai':
    if season == 'Winter':
        prize_per_day = 45000
    elif season == 'Summer':
        prize_per_day = 40000
elif destination == 'Sofia':
    if season == 'Winter':
        prize_per_day = 17000
    elif season == 'Summer':
        prize_per_day = 12500
elif destination == 'London':
    if season == 'Winter':
        prize_per_day = 24000
    elif season == 'Summer':
        prize_per_day = 20250

if destination == 'Dubai':
    prize_per_day = prize_per_day - (prize_per_day * 0.3)
if destination == 'Sofia':
    prize_per_day = prize_per_day + (prize_per_day * 0.25)

total = prize_per_day * days
money_left = total - budget

if budget >= total:
    print(f'The budget for the movie is enough! We have {abs(money_left):.2f} leva left!')
else:
    print(f'The director needs {abs(money_left):.2f} leva more!')