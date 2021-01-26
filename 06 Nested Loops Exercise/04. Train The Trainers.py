people = int(input())
total_pres = 0
total_grades = 0

name = input()
while name != 'Finish':
    total_sum = 0
    for i in range(1, people +1):
        grade = float(input())
        total_sum += grade
    print(f'{name} - {total_sum / people:.2f}.')
    total_pres += 1
    total_grades += total_sum
    name = input()

print(f"Student's final assessment is {total_grades / (total_pres * people):.2f}.")