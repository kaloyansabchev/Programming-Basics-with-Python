locations = int(input())

for location in range(0, locations):
    average_expected = float(input())
    days = int(input())
    total_extracted = 0
    for day in range(0, days):
        extracted_gold = float(input())
        total_extracted += extracted_gold
    average_extracted = total_extracted / days
    needed = average_expected - average_extracted
    if average_extracted >= average_expected:
        print(f"Good job! Average gold per day: {average_extracted:.2f}.")
    else:
        print(f"You need {needed:.2f} gold.")