price_over_20 = float(input())
kg_luggage = float(input())
days = int(input())
quantity_luggage = int(input())

price_per_l = 0

if kg_luggage < 10:
    price_per_l = price_over_20 * 0.2
elif 10 <= kg_luggage <= 20:
    price_per_l = price_over_20 / 2
elif kg_luggage > 20:
    price_per_l = price_over_20

if days > 30:
    price_per_l *= 1.1
elif 7 <= days <= 30:
    price_per_l *= 1.15
elif days < 7:
    price_per_l *= 1.4

total_sum = price_per_l * quantity_luggage
print(f"The total price of bags is: {total_sum:.2f} lv. ")