price_per_page = float(input())
price_per_cover = float(input())
pecen_discount = int(input())
desiner_salary = float(input())
percent_of_total_sum = int(input())

total_for_print = (price_per_page * 899) + (price_per_cover * 2)
total_after_discount = total_for_print - (total_for_print * pecen_discount / 100)
total_plus_desein = total_after_discount + desiner_salary
total_for_the_group = total_plus_desein - (total_plus_desein * percent_of_total_sum / 100)

print(f"Avtonom should pay {total_for_the_group:.2f} BGN.")