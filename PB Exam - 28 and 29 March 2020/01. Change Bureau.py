bitcoin_count = int(input())
cny_count = float(input())
commission = float(input())

bitcoin = 1168
cny = 0.15
dollar = 1.76
euro = 1.95

total_in_lv = (bitcoin * bitcoin_count + (cny * cny_count * dollar)) / euro
commission_value = total_in_lv * commission / 100
result = total_in_lv - commission_value
print(f'{result:.2f}')
