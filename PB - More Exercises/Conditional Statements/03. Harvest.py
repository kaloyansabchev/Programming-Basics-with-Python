# От лозе с площ X квадратни метри се заделя 40% от реколтата за производство на вино. От 1 кв.м лозе се изкарват Y килограма грозде.
# За 1 литър вино са нужни 2,5 кг. грозде. Желаното количество вино за продан е Z литра.
# Напишете програма, която пресмята колко вино може да се произведе и дали това количество е достатъчно. Ако е достатъчно,
# остатъкът се разделя по равно между работниците на лозето.

import math
x = int(input())
y = float(input())
z = int(input())
workers = int(input())

total_grape = x * y
wine = (total_grape * 0.4) / 2.5
if wine >= z:
    wine_left = wine - z
    wine_left = abs(wine_left)
    wine_per_person = wine_left / workers
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(wine_left)} liters left -> {math.ceil(wine_per_person)} liters per person.")
else:
    wine_needed = z - wine
    print(f"It will be a tough winter! More {math.floor(wine_needed)} liters wine needed.")