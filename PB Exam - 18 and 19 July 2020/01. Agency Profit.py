company = input()
tickets_adult = int(input())
tickets_kids = int(input())
ticket_price = float(input())
fee = float(input())

kid_t_price = ticket_price * 0.3
tickets_adult_total = ticket_price + fee
tickets_kids_total = kid_t_price + fee
total_t_price = tickets_adult_total * tickets_adult + tickets_kids_total * tickets_kids
profit = total_t_price * 0.2
print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")