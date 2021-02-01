clients = int(input())
perches = ""

basket_q = 0
wreath_q = 0
chocolate_bunny_q = 0
perch_q = 0
end_sum = 0
total_sum = 0
for client in range(1, clients +1):
    perches = input()
    while perches != 'Finish':
        if perches == "basket":
            basket_q += 1
        elif perches == 'wreath':
            wreath_q += 1
        elif perches == 'chocolate bunny':
            chocolate_bunny_q += 1
        perches = input()
    perch_q = basket_q + wreath_q + chocolate_bunny_q
    if perch_q % 2 == 0:
        end_sum = basket_q * 1.5 + wreath_q * 3.8 + chocolate_bunny_q * 7
        end_sum = end_sum - end_sum * 0.2
        total_sum += end_sum
    else:
        end_sum = basket_q * 1.5 + wreath_q * 3.8 + chocolate_bunny_q * 7
        total_sum += end_sum
    print(f"You purchased {perch_q} items for {end_sum:.2f} leva.")
    basket_q = 0
    wreath_q = 0
    chocolate_bunny_q = 0
    perch_q = 0
    end_sum = 0

average_sum = total_sum / clients
print(f"Average bill per client is: {average_sum:.2f} leva.")