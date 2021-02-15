junior = int(input())
senior = int(input())
race_type = input()

junior_price = 0
senior_price = 0

if race_type == "trail":
    junior_price = 5.5
    senior_price = 7
elif race_type == "cross-country":
    junior_price = 8
    senior_price = 9.5
elif race_type == "downhill":
    junior_price = 12.25
    senior_price = 13.75
elif race_type == "road":
    junior_price = 20
    senior_price = 21.50

total_sum = junior * junior_price + senior * senior_price

total_participants = junior + senior
if total_participants >= 50 and race_type == "cross-country":
    total_sum *= 0.75

fee = total_sum * 0.05
end_sum = total_sum - fee
print(f"{end_sum:.2f}")