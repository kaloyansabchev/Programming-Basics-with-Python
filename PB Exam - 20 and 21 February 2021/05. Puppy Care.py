food_kg = int(input())

total_food_gr = food_kg * 1000
eated = 0

while True:
    food_eaten_gr = input()
    if food_eaten_gr == "Adopted":
        break
    food_eaten_gr = int(food_eaten_gr)
    eated += food_eaten_gr

food_needed = eated - total_food_gr
if eated > total_food_gr:
    print(f"Food is not enough. You need {abs(food_needed)} grams more.")
else:
    print(f"Food is enough! Leftovers: {abs(food_needed)} grams.")