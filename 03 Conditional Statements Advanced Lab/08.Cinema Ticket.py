day = input()

# ticket_prize_12 = day == 'Monday' or day == 'Tuesday' or day == 'Friday'
# ticket_prize_14 = day == 'Wednesday' or day == 'Thursday'
# ticket_prize_16 = day == 'Saturday' or day == 'Sunday'

if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    print(12)
elif day == 'Wednesday' or day == 'Thursday':
    print(14)
elif day == 'Saturday' or day == 'Sunday':
    print(16)
