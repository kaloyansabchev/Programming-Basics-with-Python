month = input()
hours = int(input())
people_in_group = int(input())
time_of_the_day = input()

per_hour = 0

if month == "march" or month == "april" or month == "may":
    if time_of_the_day == "day":
        per_hour = 10.50
    elif time_of_the_day == "night":
        per_hour = 8.40
elif month == "june" or month == 'july' or month == "august":
    if time_of_the_day == "day":
        per_hour = 12.60
    elif time_of_the_day == "night":
        per_hour = 10.20

if people_in_group >= 4:
    per_hour *= 0.9
if hours >= 5:
    per_hour *= 0.5

price_per_person = per_hour
total_price = (price_per_person * people_in_group) * hours

print(f"Price per person for one hour: {price_per_person:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")