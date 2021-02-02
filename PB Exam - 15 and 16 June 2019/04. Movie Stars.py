budget = float(input())
name = input()

total_s_given = 0
money_left = budget
money_needed = 0
m = True

while name != 'ACTION':
    counter = name.count('')
    counter -= 1
    if counter <= 15:
        new_salary = float(input())
        if new_salary > money_left:
            money_needed = new_salary - money_left
            print(f"We need {money_needed:.2f} leva for our actors.")
            m = False
            break
        total_s_given += new_salary
        money_left -= new_salary
    else:
        new_salary = money_left * 0.2
        if new_salary > money_left:
            money_needed = new_salary - money_left
            print(f"We need {money_needed:.2f} leva for our actors.")
            m = False
            break
        total_s_given += new_salary
        money_left -= new_salary
    name = input()

if m:
    left_over = budget - total_s_given
    print(f"We are left with {left_over:.2f} leva.")