budget = float(input())
serials = int(input())

serial_prize = 0
total_prize = 0

for serial in range(0, serials):
    name = input()
    prize = float(input())
    if name == 'Thrones':
         serial_prize = prize - (prize * 0.5)
         total_prize += serial_prize
    elif name == 'Lucifer':
        serial_prize = prize - (prize * 0.4)
        total_prize += serial_prize
    elif name == 'Protector':
        serial_prize = prize - (prize * 0.3)
        total_prize += serial_prize
    elif name == 'TotalDrama':
        serial_prize = prize - (prize * 0.2)
        total_prize += serial_prize
    elif name == 'Area':
        serial_prize = prize - (prize * 0.1)
        total_prize +=serial_prize
    else:
        serial_prize = prize
        total_prize += serial_prize

money_let = budget - total_prize
if budget >= total_prize:
    print(f"You bought all the series and left with {money_let:.2f} lv.")
else:
    print(f"You need {abs(money_let):.2f} lv. more to buy the series!")