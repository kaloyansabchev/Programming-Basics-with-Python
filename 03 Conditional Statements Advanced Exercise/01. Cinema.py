type = input()
rows = int(input())
colums = int(input())

income = 0
capacity = rows * colums

if type == 'Premiere':
    income = capacity * 12.00
elif type == 'Normal':
    income = capacity * 7.50
elif type == 'Discount':
    income = capacity * 5.00

print(f'{income:.2f} leva')