price_per_kilogram_v = float(input())
price_per_kilogram_f = float(input())
kg_v = int(input())
kg_f = int(input())


v = price_per_kilogram_v * kg_v
f = price_per_kilogram_f * kg_f
total = v + f
total_in_eur = total / 1.94
print(f'{total_in_eur:.2f}')