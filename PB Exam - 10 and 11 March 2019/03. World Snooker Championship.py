stage = input()
ticket_type = input()
ticket_q = int(input())
picture = input()

ticket_prize = 0

if stage == 'Quarter final':
    if ticket_type == 'Standard':
        ticket_prize = 55.50
    elif ticket_type == 'Premium':
        ticket_prize = 105.2
    elif ticket_type == 'VIP':
        ticket_prize = 118.9
elif stage == 'Semi final':
    if ticket_type == 'Standard':
        ticket_prize = 75.88
    elif ticket_type == 'Premium':
        ticket_prize = 125.22
    elif ticket_type == 'VIP':
        ticket_prize = 300.4
elif stage == 'Final':
    if ticket_type == 'Standard':
        ticket_prize = 110.1
    elif ticket_type == 'Premium':
        ticket_prize = 160.66
    elif ticket_type == 'VIP':
        ticket_prize = 400

total_prize = ticket_prize * ticket_q
discount_prize = 0

if total_prize <= 2500:
    discount_prize = total_prize
elif 2500 < total_prize < 4000:
    discount_prize = total_prize - (total_prize * 0.1)
elif total_prize >= 4000:
    discount_prize = total_prize - (total_prize * 0.25)

end_sum = 0

if picture == 'Y':
    if total_prize > 4000:
        end_sum = discount_prize
    else:
        end_sum = discount_prize + ticket_q * 40
elif picture == 'N':
    end_sum = discount_prize


print(f'{end_sum:.2f}')