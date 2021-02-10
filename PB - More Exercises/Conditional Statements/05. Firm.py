import math

hours_needed = int(input())
days = int(input())
workers_overtime = int(input())

working_days = days * 0.9
working_hours = working_days * 8
overtime = workers_overtime * (2 * days)
total_hours = working_hours + overtime
total_hours = math.floor(total_hours)
diff = total_hours - hours_needed
if total_hours >= hours_needed:
    print(f"Yes!{abs(diff)} hours left.")
else:
    print(f"Not enough time!{abs(diff)} hours needed.")