import  math
days = int(input())
all_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

dog_needed = days * dog_food_per_day
cat_needed = days * cat_food_per_day
turtle_needed = days * turtle_food_per_day * 0.001

total_needed = dog_needed + cat_needed + turtle_needed
diff = total_needed - all_food
diff = abs(diff)
if total_needed <= all_food:
    print(f"{math.floor(diff)} kilos of food left.")
else:
    print(f"{math.ceil(diff)} more kilos of food are needed.")