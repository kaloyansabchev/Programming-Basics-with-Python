strawberry_price = float(input())
quan_banana = float(input())
quan_orange = float(input())
quan_raspberry = float(input())
quan_strawberry = float(input())

raspberry_price = strawberry_price / 2
oranges_price = raspberry_price - (raspberry_price * 0.4)
bananas_price = raspberry_price - (raspberry_price * 0.8)
total_raspberry = quan_raspberry * raspberry_price
total_oranges = quan_orange * oranges_price
total_bananas = quan_banana * bananas_price
total_strawberry = quan_strawberry * strawberry_price
total_price = total_raspberry + total_oranges + total_bananas + total_strawberry
print(total_price)