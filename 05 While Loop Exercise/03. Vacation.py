budget = float(input())
start_money = float(input())

spend_days = 0
total_money = start_money
days_count = 0
enough = True

while total_money < budget:
    action = input()
    add_remove_sum = float(input())
    days_count += 1
    if action == 'spend':
        total_money -= add_remove_sum
        if total_money < 0:
            total_money = 0
        spend_days += 1
    elif action == 'save':
        total_money += add_remove_sum
        spend_days = 0

    if spend_days == 5:
        print(f"You can't save the money.")
        print(f"{days_count}")
        break
    if total_money >= budget:
        print(f"You saved the money for {days_count} days.")
        enough = False
    if not enough:
        break
