mackerel_price = float(input())
caca_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = float(input())

bonito_price = mackerel_price * 1.6
horse_mackerel_price = caca_price * 1.8
sum_bonito = bonito_price * bonito_kg
sum_horse_mackerel = horse_mackerel_price * horse_mackerel_kg
sum_mussels = mussels_kg * 7.5
total = sum_mussels + sum_bonito + sum_horse_mackerel
print(f'{total:.2f}')