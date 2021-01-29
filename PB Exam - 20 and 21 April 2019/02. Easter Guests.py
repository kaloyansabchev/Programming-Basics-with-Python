import math
guest = int(input())
budget = int(input())

kozunak = guest / 3
egg = guest * 2
kozunak_price = math.ceil(kozunak) * 4
egg_price = math.ceil(egg) * 0.45
total_price = kozunak_price + egg_price
# money_left = budget - total_price
# money_need = total_price - budget
end_money = budget - total_price
if total_price <= budget:
    print(f"Lyubo bought {math.ceil(kozunak)} Easter bread and {math.ceil(egg)} eggs.")
    print(f"He has {abs(end_money):.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {abs(end_money):.2f} lv. more.")