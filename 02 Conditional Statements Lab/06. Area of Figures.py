import math
figure = input()

if figure == "square":
    side = float(input())
    area = side * side
    print(f'{area:.3f}')
elif figure == "rectangle":
    side = float(input())
    second_side = float(input())
    area = side * second_side
    print(f'{area:.3f}')
elif figure == "circle":
    side = float(input())
    area = math.pi * side * side
    print(f'{area:.3f}')
elif figure == "triangle":
    side = float(input())
    second_side = float((input()))
    area = side * second_side / 2
    print(f'{area:.3f}')