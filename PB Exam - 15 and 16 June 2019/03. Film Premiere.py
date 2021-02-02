film_name = input()
package = input()
quan_tickets = int(input())

prize = 0

if film_name == 'John Wick':
    if package == 'Drink':
        prize = 12
    elif package == 'Popcorn':
        prize = 15
    elif package == 'Menu':
        prize = 19
elif film_name == 'Star Wars':
    if package == 'Drink':
        prize = 18
    elif package == 'Popcorn':
        prize = 25
    elif package == 'Menu':
        prize = 30
elif film_name == 'Jumanji':
    if package == 'Drink':
        prize = 9
    elif package == 'Popcorn':
        prize = 11
    elif package == 'Menu':
        prize = 14

if film_name == 'Star Wars' and quan_tickets >= 4:
    prize = prize - (prize * 0.3)
if film_name == 'Jumanji' and quan_tickets == 2:
    prize = prize - (prize * 0.15)
total_prize = prize * quan_tickets
print(f"Your bill is {total_prize:.2f} leva.")