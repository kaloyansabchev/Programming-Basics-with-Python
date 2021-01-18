#     7. * Пазар за плодове
# Мария решава да мине на диета и отива до  близкия пазар, за да купи ягоди, банани, портокали и малини. Да се напише програма,
# която пресмята колко пари са  ѝ необходими за да плати сметката, като знаете, че:
#     • цената на  малините е на половина по-ниска от тази на ягодите;
#     • цената на портокалите е с 40% по-ниска от цената на малините;
#     • цената на бананите е с 80% по-ниска от цената на малините.
# Вход
# От конзолата се четат 5 реда:
#     1. Цена на ягодите в лева – реално число;
#     2. Количество на бананите в килограми – реално число;
#     3. Количество на портокалите в килограми – реално число;
#     4. Количество на малините в килограми – реално число;
#     5. Количество на ягодите в килограми – реално число.

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