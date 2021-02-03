p_name = input()
multiplier = input()
int_points = int(input())

points_left = 301
points = 0
successful_shots = 0
not_successful_shots = 0

while multiplier != 'Retire':
    if multiplier == 'Single':
        points += int_points
    elif multiplier == 'Double':
        points += (int_points * 2)
    elif multiplier == 'Triple':
        points += (int_points * 3)
    points_left -= points
    if points_left < 0:
        points_left += points
        not_successful_shots += 1
    else:
        successful_shots += 1
    points = 0
    if points_left == 0:
        break
    multiplier = input()
    if multiplier == 'Retire':
        break
    int_points = int(input())
if multiplier == 'Retire' or int_points == 'Retire':
    print(f"{p_name} retired after {not_successful_shots} unsuccessful shots.")
else:
    print(f"{p_name} won the leg with {successful_shots} shots.")
