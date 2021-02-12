fuel_type = input()
quantity = float(input())
card = input()

diesel = 2.33
gasoline = 2.22
gas = 0.93
price = 0

if card == "Yes":
    diesel -= 0.18
    gasoline -= 0.12
    gas -= 0.08

if fuel_type == "Diesel":
    price = diesel * quantity
elif fuel_type == "Gasoline":
    price = gasoline * quantity
elif fuel_type == "Gas":
    price = gas * quantity

if 20 <= quantity <= 25:
    price *= 0.92
elif quantity > 25:
    price *= 0.9

print(f"{price:.2f} lv.")
