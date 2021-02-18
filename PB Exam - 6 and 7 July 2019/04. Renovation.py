import math
wall_h = int(input())
wall_w = int(input())
percentage_wp = int(input()) # част която няма да се боядисва

total_area = wall_h * wall_w * 4
area_for_painting = total_area - (total_area * percentage_wp / 100)


while True:
    painted = input()
    if painted == "Tired!":
        print(f"{math.ceil(area_for_painting)} quadratic m left.")
        break
    painted = int(painted)
    area_for_painting -= painted
    if area_for_painting < 0:
        print(f"All walls are painted and you have {math.ceil(abs(area_for_painting))} l paint left!")
        break
    elif area_for_painting == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break
