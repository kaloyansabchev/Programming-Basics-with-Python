bad_grades = int(input())
task_name = input()
task_grade = int(input())

total_grades = 0
num_task = 0
last_task = ''
bad_grade = 0
has_failed = False

while task_name != 'Enough':
    total_grades += task_grade
    num_task += 1
    last_task = task_name
    if task_grade <= 4:
        bad_grade += 1
    if bad_grade >= bad_grades:
        print(f'You need a break, {bad_grade} poor grades.')
        has_failed = True
        break
    task_name = input()
    if task_name == 'Enough':
        break
    task_grade = int(input())

everage = total_grades / num_task
if not has_failed:
    print(f'Average score: {everage:.2f}')
    print(f'Number of problems: {num_task}')
    print(f'Last problem: {last_task}')