# 7. Магазин за детски играчки
# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни. С парите, които ще спечели,
# иска да отиде на екскурзия. Да се напише програма, която пресмята печалбата от поръчката.
# Цени на играчките:
#     • Пъзел - 2.60 лв.
#     • Говореща кукла - 3 лв.
#     • Плюшено мече - 4.10 лв.
#     • Миньон - 8.20 лв.
#     • Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът, прави отстъпка 25% от общата цена. От спечелените пари Петя трябва да даде 10%
# за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.

puzzle = 2.60
talking_doll = 3
bear = 4.10
minion = 8.20
truck = 2

trip = float(input())
puzzle_numbers = int(input())
talking_doll_numbers = int(input())
bear_numbers = int(input())
minion_numbers = int(input())
truck_numbers = int(input())

total = puzzle * puzzle_numbers + talking_doll * talking_doll_numbers + bear * bear_numbers + minion * minion_numbers + truck * truck_numbers
total_toys = puzzle_numbers + talking_doll_numbers + bear_numbers + minion_numbers + truck_numbers


if total_toys >= 50:
    total = total - total * 0.25

total = total - total * 0.1
win = total - trip
if win < 0:
    win = win * -1


if win > trip:
    print(f'Yes! {win:.2f} lv left.')
else:
    print(f'Not enough money! {win:.2f} lv needed.')
