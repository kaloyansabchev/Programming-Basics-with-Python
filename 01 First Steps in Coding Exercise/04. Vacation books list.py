# 4. Задължителна литература
# За лятната ваканция в спикъка със задължителна литература на Жоро има определен брой книги, но Жоро предпочита
# да играе с приятели навън. Вашата задача е да помогнете на Жоро да изчисли колко часа на ден трябва да отделя,
# за да прочете необходимата литература, но и да прекарва максимално време навън.
# Вход
# От конзолата се четат 3 реда:
#     1. Брой страници в текущата книга – цяло число;
#     2. Страници, които може да прочита за 1 час – цяло число;
#     3. Броя на дните, за които трябва да прочете книгата – цяло число;

total_pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_time = total_pages / pages_per_hour
result = total_time / days
print(result)