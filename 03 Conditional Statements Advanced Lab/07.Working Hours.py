# 7. Работно време
# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) - въведени от потребителя и
#     роверява дали офисът на фирма е отворен, като работното време на офисът е от 10-18 часа, от понеделник до събота включително.

hour = int(input())
day = input()

is_working_h = 10 <= hour <= 18
is_working_d = day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday'

if is_working_h and is_working_d:
    print('open')
else:
    print('closed')