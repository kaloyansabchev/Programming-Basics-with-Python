days = int(input())
hours = int(input())

fee_per_day = 0
total = 0

for day in range(1, days+1):
    for hour in range(1, hours+1):
        if day % 2 == 0:
            if hour % 2 == 0:
                fee_per_day += 1
            else:
                fee_per_day += 2.5
        else:
            if hour % 2 == 0:
                fee_per_day += 1.25
            else:
                fee_per_day += 1
    total += fee_per_day
    print(f'Day: {day} - {fee_per_day:.2f} leva')
    fee_per_day = 0

print(f'Total: {total:.2f} leva')