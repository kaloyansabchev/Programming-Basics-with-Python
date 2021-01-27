pens_quantity = int(input())
markers_quantity = int(input())
water_quantity = float(input())
discount = int(input())

pens = 5.80
markers = 7.20
water = 1.20

pens_price = pens_quantity * pens
markers_price = markers_quantity * markers
water_price = water_quantity * water
total_price = pens_price + markers_price + water_price
discount_price = total_price * discount / 100
result = total_price - discount_price
print(f'{result:.3f}')