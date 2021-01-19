# 8. *Стипендии
# Учениците могат да кандидатстват за социална стипендия или за стипендия за отличен успех. Изискване за социална
# стипендия - доход на член от семейството по-малък от минималната работна заплата и успех над 4.5. Размер на социалната
# стипендия - 35% от минималната работна заплата. Изискване за стипендия за отличен успех - успех над 5.5, включително.
# Размер на стипендията за отличен успех - успехът на ученика, умножен по коефициент 25.
# Напишете програма, която при въведени доход, успех и минимална работна заплата, дава информация дали ученик има право да
# получава стипендия, и стойността на стипендията, която е по-висока за него.
# Вход
# Потребителят въвежда 3 числа, по едно на ред:
#     1. Доход в лева - реално число;
#     2. Среден успех -  реално числсо;
#     3. Минимална работна заплата – реално число.

import  math
income = float(input())
grades = float(input())
salary = float(input())

excellent_scholarship = 0
social_scholarship = 0

if grades >= 5.50:
    excellent_scholarship += grades * 25

if income < salary and grades > 4.50:
    social_scholarship += salary * 0.35

if social_scholarship > excellent_scholarship:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
elif excellent_scholarship >= social_scholarship:
    if excellent_scholarship != 0:
        print(f'You get a scholarship for excellent results {math.floor(excellent_scholarship)} BGN')
    else:
        print(f'You cannot get a scholarship!')