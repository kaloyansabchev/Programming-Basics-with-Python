import math
tournaments = int(input())
start_points = int(input())


total_points = start_points
tournaments_points_only = 0
points = 0
average_points = 0
times_won = 0
for tournament in range(1, tournaments+1):
    etap = input()
    if etap == 'F':
        points += 1200
    elif etap == 'W':
        points += 2000
    elif etap == 'SF':
        points += 720
    if etap == 'W':
        times_won += 1
    tournaments_points_only += points
    total_points += points
    points = 0


average_points = tournaments_points_only / tournaments
print(f'Final points: {math.floor(total_points)}')
print(f'Average points: {math.floor(average_points)}')
print("{:.2%}".format(times_won / tournaments))
