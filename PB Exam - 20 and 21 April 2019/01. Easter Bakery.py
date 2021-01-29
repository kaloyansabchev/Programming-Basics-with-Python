price_flour_kg = float(input())
flours_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
yeast = int(input())

price_sugar_kg = price_flour_kg - (price_flour_kg * 0.25)
price_eggs = price_flour_kg + (price_flour_kg * 0.10)
price_yeast = price_sugar_kg - (price_sugar_kg * 0.80)

sum_flour = price_flour_kg * flours_kg
sum_sugar = price_sugar_kg * sugar_kg
sum_eggs = price_eggs * eggs
sum_yeast = price_yeast * yeast

total = sum_yeast + sum_sugar + sum_flour + sum_eggs
print(f'{total:.2f}')