quantity_joinery = int(input())
joinery_type = input()
delivery = input()

one_joinery = 0
if quantity_joinery < 10:
    print("Invalid order")
else:
    if joinery_type == "90X130":
        one_joinery = 110
        if 30 < quantity_joinery <= 60:
            one_joinery *= 0.95
        elif quantity_joinery > 60:
            one_joinery *= 0.92
    elif joinery_type == "100X150":
        one_joinery = 140
        if 40 < quantity_joinery <= 80:
            one_joinery *= 0.94
        elif quantity_joinery > 80:
            one_joinery *= 0.90
    elif joinery_type == "130X180":
        one_joinery = 190
        if 20 < quantity_joinery <= 50:
            one_joinery *= 0.93
        elif quantity_joinery > 50:
            one_joinery *= 0.88
    elif joinery_type == "200X300":
        one_joinery = 250
        if 25 < quantity_joinery <= 50:
            one_joinery *= 0.91
        elif quantity_joinery > 50:
            one_joinery *= 0.86

    total_price = quantity_joinery * one_joinery
    if delivery == "With delivery":
        total_price += 60

    if quantity_joinery > 99:
        total_price *= 0.96

    print(f'{total_price:.2f} BGN')
