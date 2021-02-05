import math
w = float(input())
h = float(input())

height = h * 100 - 100
h_desk = math.floor(height / 70)

wide = w * 100
w_desk = math.floor(wide / 120)

total_desks = h_desk * w_desk - 3
print(total_desks)