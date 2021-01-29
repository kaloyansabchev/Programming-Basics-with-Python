import math
guest = int(input())
price_kuvert = float(input())
budget = float(input())

kuvert_for_one = 0
cake = budget * 0.1
if guest < 10:
    kuvert_for_one += price_kuvert
elif 10 <= guest <= 15:
    kuvert_for_one += price_kuvert - (price_kuvert *0.15)
elif 15 < guest <= 20:
    kuvert_for_one = price_kuvert - (price_kuvert * 0.2)
elif guest > 20:
    kuvert_for_one = price_kuvert - (price_kuvert * 0.25)

total_sum = guest * kuvert_for_one + cake
money_left = total_sum - budget
money_need = total_sum - budget
if total_sum < budget:
    print(f"It is party time! {abs(money_left):.2f} leva left.")
else:
    print(f"No party! {abs(money_need):.2f} leva needed.")