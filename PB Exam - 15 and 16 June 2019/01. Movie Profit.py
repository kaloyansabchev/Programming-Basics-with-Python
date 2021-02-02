name = input()
days = int(input())
tickets = int(input())
prize = float(input())
percent_for_the_cinema = int(input())

tickets_prize = tickets * prize
total_income = tickets_prize * days
cinema_income = total_income * percent_for_the_cinema / 100
profit = total_income - cinema_income
print(f"The profit from the movie {name} is {profit:.2f} lv.")