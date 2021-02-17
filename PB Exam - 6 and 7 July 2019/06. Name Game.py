name = input()

check_name = name
winner_points = 0
winner_name = ""

for num in range(1, len(name)):
    total_points = 0
    for letter in name:
        number = int(input())
        number_symbol = chr(number)
        if letter == number_symbol:
            total_points += 10
        else:
            total_points += 2
    if total_points >= winner_points:
        winner_points = total_points
        winner_name = name
    name = input()
    if name == "Stop":
        break
print(f"The winner is {winner_name} with {winner_points} points!")

