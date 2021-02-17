kozinaci = int(input())

winner_points = 0
winner_name = ""
for k in range(0, kozinaci):
    name = input()
    grade = input()
    total_points = 0
    while grade != "Stop":
        grade = int(grade)
        total_points += grade
        grade = input()

    print(f"{name} has {total_points} points.")
    if total_points > winner_points:
        winner_points = total_points
        winner_name = name
        print(f"{name} is the new number 1!")

print(f"{winner_name} won competition with {winner_points} points!")