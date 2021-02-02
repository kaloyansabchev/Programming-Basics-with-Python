capacity = int(input())
people_in = input()

space_left = capacity
ticket_pay = 0
total_pay = 0
while people_in != 'Movie time!':
    people = int(people_in)
    space_left -= people
    if space_left < 0:
        print(f'The cinema is full.')
        break
    if people % 3 == 0:
        ticket_pay = people * 5 - 5
        total_pay += ticket_pay
    else:
        ticket_pay = people * 5
        total_pay += ticket_pay
    people_in = input()
if people_in == 'Movie time!':
    print(f"There are {space_left} seats left in the cinema.")
print(f"Cinema income - {total_pay} lv.")