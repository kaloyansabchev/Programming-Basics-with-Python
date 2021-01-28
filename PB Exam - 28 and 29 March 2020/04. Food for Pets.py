days = int(input())
food_total = int(input())

total_dog = 0
total_cat = 0
bonus_food = 0

for day in range(1, days+1):
    dog_eaten = int(input())
    cat_eaten = int(input())
    total_dog += dog_eaten
    total_cat += cat_eaten
    if day % 3 == 0:
        total = dog_eaten + cat_eaten
        bonus = total * 0.1
        bonus_food += bonus

percent_eaten = 100 * (total_cat + total_dog) / food_total
percent_dog = 100 * total_dog / (total_cat + total_dog)
percent_cat = 100 - percent_dog

print(f"Total eaten biscuits: {round(bonus_food)}gr.")
print(f"{percent_eaten:.2f}% of the food has been eaten.")
print(f"{percent_dog:.2f}% eaten from the dog.")
print(f"{percent_cat:.2f}% eaten from the cat.")