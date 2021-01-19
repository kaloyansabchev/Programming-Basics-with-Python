# 6. Годзила срещу Конг
# Снимките за дългоочаквания филм "Годзила срещу Конг" започват. Сценаристът Адам Уингард ви моли да напишете
# програма, която да изчисли, дали предвидените средства са достатъчни за снимането на филма. За снимките  ще бъдат
# нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
#         ◦ Декорът за филма е на стойност 10% от бюджета.
#         ◦ При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
#     Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
#     Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
#     Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

budget = float(input())
statists = int(input())
costume = float(input())

decor = budget * 0.1
price_costume = statists * costume
discount = 0
if statists > 150:
    price_costume -= (price_costume * 0.1)

total_cost = decor + price_costume
money_left = budget - total_cost

if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(money_left):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")