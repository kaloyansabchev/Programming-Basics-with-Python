counter_days = int(input())
counter_bakers = int(input())
counter_cake = int(input())
counter_waffles = int(input())
counter_pancakes = int(input())

cake = counter_cake * 45
waffle = counter_waffles * 5.80
pancakes = counter_pancakes * 3.20

one_baker_per_day = cake + waffle + pancakes
all_bakers_per_day = one_baker_per_day * counter_bakers
sum_all_days = all_bakers_per_day * counter_days
expenses = sum_all_days / 8
profit = sum_all_days - expenses

print(profit)