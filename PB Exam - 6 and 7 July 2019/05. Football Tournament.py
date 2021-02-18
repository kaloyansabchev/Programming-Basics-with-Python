name = input()
games = int(input())

points = 0
wins = 0
draws = 0
losts = 0

if games > 0:
    for game in range(0, games):
        result = input()
        if result == "W":
            points += 3
            wins += 1
        elif result == "D":
            points += 1
            draws += 1
        elif result == "L":
            losts += 1
    win_rate = (wins / games) * 100
    print(f"{name} has won {points} points during this season.")
    print(f"Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losts}")
    print(f"Win rate: {win_rate:.2f}%")
else:
    print(f"{name} hasn't played any games during this season.")
