import math
width = float(input())
lenght = float(input())
high = float(input())
astronaught_h = float(input())

rocket_s = width * lenght * high
room_s = (astronaught_h + 0.4) * 2 * 2
persons = rocket_s / room_s
persons = math.floor(persons)

if persons <= 2:
    print(f"The spacecraft is too small.")
elif 3 <= persons <= 10:
    print(f"The spacecraft holds {persons} astronauts.")
elif persons > 10:
    print(f"The spacecraft is too big.")