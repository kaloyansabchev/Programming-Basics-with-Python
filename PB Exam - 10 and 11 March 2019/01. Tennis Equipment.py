import math
one_racket_price = float(input())
quan_racket = int(input())
quan_boots = int(input())

rackets_price = one_racket_price * quan_racket
boots_price = one_racket_price / 6
all_boots_price = boots_price * quan_boots
left_over_equp = (rackets_price + all_boots_price) * 0.2
total = rackets_price + all_boots_price + left_over_equp
jock_part = total / 8
sponsors_part = total - jock_part

print(f"Price to be paid by Djokovic {math.floor(jock_part)}")
print(f"Price to be paid by sponsors {math.ceil(sponsors_part)}")