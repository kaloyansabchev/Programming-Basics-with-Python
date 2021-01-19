# 4. Конвертор за мерни единици
# Да се напише програма, която преобразува разстояние между следните 3 мерни единици: mm, cm, m.
# Използвайте съответствията от таблицата по-долу:
# входна единица
# изходна единица
# 1 meter (m) = 1000 millimeters (mm)
# 1 meter (m) = 100 centimeters (cm)
# Входните данни се състоят от три реда, въведени от потребителя:
#     • Първи ред: число за преобразуване - реално число;
#     • Втори ред: входна мерна единица – текст;
#     • Трети ред: изходна мерна единица (за резултата) – текст.
# На конзолата да се отпечата резултатът от преобразуването на мерните единици, форматиран до третия знак след десетичната запетая.

num = float(input())
unit = input()
new_unit = input()

if unit == 'mm':
    if new_unit == 'cm':
        result = num / 10
        print(f'{result:.3f}')
    elif new_unit == 'm':
        result = num / 1000
        print(f'{result:.3f}')
elif unit == 'cm':
    if new_unit == 'mm':
        result = num * 10
        print(f'{result:.3f}')
    elif new_unit == 'm':
        result = num / 100
        print(f'{result:.3f}')
elif unit == "m":
    if new_unit == "mm":
        result = num * 1000
        print(f'{result:.3f}')
    elif new_unit == 'cm':
        result = num * 100
        print(f'{result:.3f}')