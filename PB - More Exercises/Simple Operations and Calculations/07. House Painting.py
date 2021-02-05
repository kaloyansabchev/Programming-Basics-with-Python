house_h = float(input())
wide_side_wall = float(input())
triangle_h = float(input())

#стените
side_wall_area = house_h * wide_side_wall
windows_area = 1.5 * 1.5
both_side_walls = 2 * side_wall_area - 2 * windows_area
back_side_wall = house_h * house_h
entrance = 1.2 * 2
front_and_back_walls = back_side_wall * 2 - entrance
total_down_part = both_side_walls + front_and_back_walls
green_paint = total_down_part / 3.4
#покрив
both_rectangle_roof = 2 * (house_h * wide_side_wall)
both_triangle_roof = 2 * (house_h * triangle_h / 2)
total_upper_part = both_rectangle_roof + both_triangle_roof
red_paint = total_upper_part / 4.3
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')