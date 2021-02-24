cats = int(input())

small = 0
middle = 0
big = 0
total_food = 0

for cat in range(0, cats):
    grams_food = float(input())
    if 100 <= grams_food < 200:
        small += 1
        total_food += grams_food
    elif 200 <= grams_food < 300:
        middle += 1
        total_food += grams_food
    elif 300 <= grams_food < 400:
        big += 1
        total_food += grams_food

total_cost = (total_food / 1000) * 12.45
print(f"Group 1: {small} cats.")
print(f"Group 2: {middle} cats.")
print(f"Group 3: {big} cats.")
print(f"Price for food per day: {total_cost:.2f} lv.")


