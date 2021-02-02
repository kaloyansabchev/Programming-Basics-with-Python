actor_name = input()
points_from_academy = float(input())
number_of_evaluators = int(input())

total_p = points_from_academy

for evaluator in range(0, number_of_evaluators):
    evaluator_name = input()
    point_from_a = float(input())
    counter = evaluator_name.count('')
    total_points_from_counter = ((counter - 1) * point_from_a) / 2
    total_p += total_points_from_counter
    if total_p > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_p:.1f}!")
        break
if total_p < 1250.5:
    points_needed = 1250.5 - total_p
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")