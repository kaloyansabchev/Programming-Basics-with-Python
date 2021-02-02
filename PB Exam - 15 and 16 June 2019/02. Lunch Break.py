import math
name = input()
duration_epizod = int(input())
duration_break = int(input())

lunch_time = duration_break / 8
break_time = duration_break / 4
time_left = duration_break - lunch_time - break_time

free_time = time_left - duration_epizod
if time_left >= duration_epizod:
    print(f"You have enough time to watch {name} and left with {math.ceil(free_time):.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(abs(free_time)):.0f} more minutes.")