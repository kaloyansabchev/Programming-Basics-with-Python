import math
q_magnolias = int(input())
q_hyacinths = int(input())
q_roses = int(input())
q_cactus = int(input())
gift = float(input())

magnolias = 3.25
hyacinths = 4
roses = 3.5
cactus = 8

magnolias_price = magnolias * q_magnolias
hyacinths_price = hyacinths * q_hyacinths
roses_price = roses * q_roses
cactus_price = cactus * q_cactus
total_price = magnolias_price + hyacinths_price + roses_price + cactus_price
taxes = total_price * 0.05
income = total_price - taxes
diff = abs(income - gift)
if income >= gift:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")