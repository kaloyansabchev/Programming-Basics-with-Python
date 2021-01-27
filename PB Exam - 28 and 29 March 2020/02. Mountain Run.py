import math
record = float(input())
distance = float(input())
time_in_seconds = float(input())

total_to_climb_in_seconds = distance * time_in_seconds
add_time = math.floor(distance / 50) * 30
total_time_in_sec = total_to_climb_in_seconds + add_time
time_diff = total_time_in_sec - record

if total_time_in_sec < record:
    print(f'Yes! The new record is {total_time_in_sec} seconds.')

else:
    print(f'"No! He was {time_diff} seconds slower.')