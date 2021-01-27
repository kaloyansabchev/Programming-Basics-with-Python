fruit = input()
size = input()
quantity = int(input())

if fruit == "Watermelon":
    if size == "small":
        small_W_price = quantity * 2 * 56
        if small_W_price < 400:
            print(f'{small_W_price:.2f} lv.')
        elif 400 <= small_W_price <= 1000:
            final_price = small_W_price - small_W_price * 0.15
            print(f'{final_price:.2f} lv.')
        elif small_W_price > 1000:
            final_price = small_W_price - small_W_price * 0.5
            print(f'{final_price:.2f} lv.')
    elif size == "big":
        big_W_price = quantity * 5 * 28.7
        if big_W_price < 400:
            print(f'{big_W_price:.2f} lv.')
        elif 400 <= big_W_price <= 1000:
            final_price = big_W_price - big_W_price * 0.15
            print(f'{final_price:.2f} lv.')
        elif big_W_price > 1000:
            final_price = big_W_price - big_W_price * 0.5
            print(f'{final_price:.2f} lv.')
elif fruit == "Mango":
    if size == "small":
        small_W_price = quantity * 2 * 36.66
        if small_W_price < 400:
            print(f'{small_W_price:.2f} lv.')
        elif 400 <= small_W_price <= 1000:
            final_price = small_W_price - small_W_price * 0.15
            print(f'{final_price:.2f} lv.')
        elif small_W_price > 1000:
            final_price = small_W_price - small_W_price * 0.5
            print(f'{final_price:.2f} lv.')
    elif size == "big":
        big_W_price = quantity * 5 * 19.6
        if big_W_price < 400:
            print(f'{big_W_price:.2f} lv.')
        elif 400 <= big_W_price <= 1000:
            final_price = big_W_price - big_W_price * 0.15
            print(f'{final_price:.2f} lv.')
        elif big_W_price > 1000:
            final_price = big_W_price - big_W_price * 0.5
            print(f'{final_price:.2f} lv.')
elif fruit == "Pineapple":
    if size == "small":
        small_W_price = quantity * 2 * 42.10
        if small_W_price < 400:
            print(f'{small_W_price:.2f} lv.')
        elif 400 <= small_W_price <= 1000:
            final_price = small_W_price - small_W_price * 0.15
            print(f'{final_price:.2f} lv.')
        elif small_W_price > 1000:
            final_price = small_W_price - small_W_price * 0.5
            print(f'{final_price:.2f} lv.')
    elif size == "big":
        big_W_price = quantity * 5 * 24.80
        if big_W_price < 400:
            print(f'{big_W_price:.2f} lv.')
        elif 400 <= big_W_price <= 1000:
            final_price = big_W_price - big_W_price * 0.15
            print(f'{final_price:.2f} lv.')
        elif big_W_price > 1000:
            final_price = big_W_price - big_W_price * 0.5
            print(f'{final_price:.2f} lv.')
elif fruit == "Raspberry":
    if size == "small":
        small_W_price = quantity * 2 * 20
        if small_W_price < 400:
            print(f'{small_W_price:.2f} lv.')
        elif 400 <= small_W_price <= 1000:
            final_price = small_W_price - small_W_price * 0.15
            print(f'{final_price:.2f} lv.')
        elif small_W_price > 1000:
            final_price = small_W_price - small_W_price * 0.5
            print(f'{final_price:.2f} lv.')
    elif size == "big":
        big_W_price = quantity * 5 * 15.2
        if big_W_price < 400:
            print(f'{big_W_price:.2f} lv.')
        elif 400 <= big_W_price <= 1000:
            final_price = big_W_price - big_W_price * 0.15
            print(f'{final_price:.2f} lv.')
        elif big_W_price > 1000:
            final_price = big_W_price - big_W_price * 0.5
            print(f'{final_price:.2f} lv.')
