length = int(input())
width = int(input())
hight = int(input())
percent_o_volume = float(input())

total_volume = length * width * hight
total_volume_liters = total_volume * 0.001
percent = percent_o_volume * 0.01
total_volume_free = total_volume_liters * (1 - percent)
print(total_volume_free)