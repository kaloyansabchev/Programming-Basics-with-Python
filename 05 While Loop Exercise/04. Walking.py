steps = input()

steps_needed = 10000
steps_done = 0
if_made_steps = False

while steps != 'Going home':
    steps = int(steps)
    steps_done += steps
    diff_steps = steps_done - steps_needed
    if steps_done >= steps_needed:
        print(f'Goal reached! Good job!')
        print(f'{diff_steps} steps over the goal!')
        if_made_steps = True
        break

    steps = input()

if not if_made_steps:
    steps = input()
    steps = int(steps)
    steps_done += steps
    diff_steps = steps_done - steps_needed
    if steps_done >= steps_needed:
        print(f'Goal reached! Good job!')
        print(f'{diff_steps} steps over the goal!')
    else:
        print(f'{abs(diff_steps)} more steps to reach goal.')