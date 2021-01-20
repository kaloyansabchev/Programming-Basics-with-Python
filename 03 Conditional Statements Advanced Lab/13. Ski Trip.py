days = int(input())
type_of = input()
rating = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35
total_prize = 0
discount_prize = 0
total_with_rating = 0

if days < 10:
    if type_of == 'room for one person':
        total_prize = (days - 1) * room_for_one_person
        discount_prize = total_prize
    elif type_of == 'apartment':
        total_prize = (days - 1) * apartment
        discount_prize = total_prize - (total_prize * 0.3)
    elif type_of == 'president apartment':
        total_prize = (days - 1) * president_apartment
        discount_prize = total_prize - (total_prize * 0.1)
elif 10 <= days <= 15:
    if type_of == 'room for one person':
        total_prize = (days - 1) * room_for_one_person
        discount_prize = total_prize
    elif type_of == 'apartment':
        total_prize = (days - 1) * apartment
        discount_prize = total_prize - (total_prize * 0.35)
    elif type_of == 'president apartment':
        total_prize = (days - 1) * president_apartment
        discount_prize = total_prize - (total_prize * 0.15)
elif days > 15:
    if type_of == 'room for one person':
        total_prize = (days - 1) * room_for_one_person
        discount_prize = total_prize
    elif type_of == 'apartment':
        total_prize = (days - 1) * apartment
        discount_prize = total_prize - (total_prize * 0.5)
    elif type_of == 'president apartment':
        total_prize = (days - 1) * president_apartment
        discount_prize = total_prize - (total_prize * 0.2)

if rating == 'positive':
    total_with_rating = discount_prize + (discount_prize * 0.25)
else:
    total_with_rating = discount_prize - (discount_prize * 0.1)
print(f'{total_with_rating:.2f}')