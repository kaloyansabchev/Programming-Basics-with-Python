chicken_q = int(input())
fish_q = int(input())
vegan_q = int(input())

chicken_price = chicken_q * 10.35
fish_price = fish_q * 12.40
vegan_price = vegan_q * 8.15
food_price = chicken_price + fish_price + vegan_price
desert = food_price * 0.2
total_price = food_price + desert + 2.5
print(f'Total: {total_price:.2f}')