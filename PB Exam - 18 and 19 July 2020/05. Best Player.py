name = input()
goals = int(input())

most_goals = 0
best_player = ""

while True:
    if goals > most_goals:
        most_goals = goals
        best_player = name
    name = input()
    if name == "END":
        break
    goals = int(input())
    if goals >= 10:
        most_goals = goals
        best_player = name
        break

print(f"{best_player} is the best player!")

if goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")