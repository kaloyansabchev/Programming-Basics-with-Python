start_quantity = int(input())
command = input()
eggs = int(input())

eggs_left = start_quantity
eggs_sold = 0
sold_out = True

while True:
    if command == "Buy":
        eggs_left -= eggs
        eggs_sold += eggs
    elif command == "Fill":
        eggs_left += eggs
    if eggs_left < 0:
        eggs_left += eggs
        print(f"Not enough eggs in store!")
        print(f"You can buy only {eggs_left}.")
        sold_out = False
        break
    command = input()
    if command == "Close":
        break
    eggs = int(input())
if sold_out:
    print(f"Store is closed!")
    print(f"{eggs_sold} eggs sold.")
