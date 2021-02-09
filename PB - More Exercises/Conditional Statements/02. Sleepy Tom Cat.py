# Котката Том обича по цял ден да спи, за негово съжаление стопанинът му си играе с него винаги когато  има свободно време. За да се наспи добре,
# нормата за игра на Том е 30 000  минути в година. Времето за игра на Том зависи от почивните дни на стопанина му:
#     • Когато е на работа, стопанинът му си играе с него по 63 минути на ден.
#     • Когато почива, стопанинът му си играе с него  по 127 минути на ден.
# Напишете програма, която въвежда броя почивни дни и отпечатва дали Том може да се наспи добре и колко е разликата от нормата за текущата година,
# като приемем че годината има 365 дни.

import math
holidays = int(input())

work_days = 365 - holidays
total_minutes = (work_days * 63) + (holidays * 127)
diff = 30000 - total_minutes
total_h = abs(diff) / 60
total_h = math.floor(total_h)
total_m = abs(diff) % 60
if total_minutes < 30000:
    print(f'Tom sleeps well')
    print(f'{total_h:.0f} hours and {total_m:.0f} minutes less for play')
else:
    print(f"Tom will run away")
    print(f"{total_h:.0f} hours and {total_m:.0f} minutes more for play")