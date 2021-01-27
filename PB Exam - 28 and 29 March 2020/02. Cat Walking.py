minutes = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

burn_calories_per_day = (minutes * walks_per_day) * 5
half_calories = calories_per_day * 0.5
if burn_calories_per_day >= half_calories:
    print(f'Yes, the walk for your cat is enough. Burned calories per day: {burn_calories_per_day}.')
else:
    print(f'No, the walk for your cat is not enough. Burned calories per day: {burn_calories_per_day}.')