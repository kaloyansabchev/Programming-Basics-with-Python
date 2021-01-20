product = input()
day = input()
quantity = float(input())

if day == "Saturday" or day == "Sunday":
    if product == 'banana':
        banana_cost = 2.70 * quantity
        print(f'{banana_cost:.2f}')
    elif product == 'apple':
        apple_cost = 1.25 * quantity
        print(f'{apple_cost:.2f}')
    elif product == 'orange':
        orange_cost = 0.90 * quantity
        print(f'{orange_cost:.2f}')
    elif product == 'grapefruit':
        grapefruit_cost = 1.60 * quantity
        print(f'{grapefruit_cost:.2f}')
    elif product == 'kiwi':
        kiwi_cost = 3.00 * quantity
        print(f'{kiwi_cost:.2f}')
    elif product == 'pineapple':
        pineapple_cost = 5.60 * quantity
        print(f'{pineapple_cost:.2f}')
    elif product == 'grapes':
        grapes_cost = 4.20 * quantity
        print(f'{grapes_cost:.2f}')
    else:
        print('error')

elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thruesday" or day == "Friday":
    if product == 'banana':
        banana_cost = 2.50 * quantity
        print(f'{banana_cost:.2f}')
    elif product == 'apple':
        apple_cost = 1.20 * quantity
        print(f'{apple_cost:.2f}')
    elif product == 'orange':
        orange_cost = 0.85 * quantity
        print(f'{orange_cost:.2f}')
    elif product == 'grapefruit':
        grapefruit_cost = 1.45 * quantity
        print(f'{grapefruit_cost:.2f}')
    elif product == 'kiwi':
        kiwi_cost = 2.70 * quantity
        print(f'{kiwi_cost:.2f}')
    elif product == 'pineapple':
        pineapple_cost = 5.50 * quantity
        print(f'{pineapple_cost:.2f}')
    elif product == 'grapes':
        grapes_cost = 3.85 * quantity
        print(f'{grapes_cost:.2f}')
    else:
        print('error')

else:
    print("error")