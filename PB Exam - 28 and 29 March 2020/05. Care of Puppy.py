total_food = int(input())
food_per_day = input()

food_eaten = 0
total_food_in_gr = total_food * 1000

while food_per_day != "Adopted":
    food_eaten += int(food_per_day)
    food_per_day = input()

if total_food_in_gr >= food_eaten:
    letf_over_food = total_food_in_gr - food_eaten
    print(f"Food is enough! Leftovers: {letf_over_food} grams.")
elif total_food_in_gr < food_eaten:
    food_need_more = food_eaten - total_food_in_gr
    print(f"Food is not enough. You need {food_need_more} grams more.")

