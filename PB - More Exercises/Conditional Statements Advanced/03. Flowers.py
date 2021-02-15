q_chrysanthemums = int(input())
q_roses = int(input())
q_tulips = int(input())
season = input()
holiday = input()

chrysanthemums_price = 0
roses_price = 0
tulips_price = 0
if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.1
    tulips_price = 2.5
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.5
    tulips_price = 4.15

total_price = chrysanthemums_price * q_chrysanthemums + roses_price * q_roses + tulips_price * q_tulips
total_flowers = q_tulips + q_roses + q_chrysanthemums

if holiday == "Y":
    total_price *= 1.15
if q_tulips > 7 and season == "Spring":
    total_price *= 0.95
if q_roses >= 10 and season == "Winter":
    total_price *= 0.9
if total_flowers > 20:
    total_price *= 0.8

total_price += 2 #за направата на букета, аранжирането е 2лв
print(f"{total_price:.2f}")