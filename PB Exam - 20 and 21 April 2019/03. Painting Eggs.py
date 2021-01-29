egg_size = input()
egg_color = input()
eggs_quantity = int(input())

prize = 0
if egg_size == "Large":
    if egg_color == "Red":
        prize = 16
    elif egg_color == "Green":
        prize = 12
    elif egg_color == "Yellow":
        prize = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        prize = 13
    elif egg_color == "Green":
        prize = 9
    elif egg_color == "Yellow":
        prize = 7
elif egg_size == "Small":
    if egg_color == "Red":
        prize = 9
    elif egg_color == "Green":
        prize = 8
    elif egg_color == "Yellow":
        prize = 5

total_prize = prize * eggs_quantity
end_prize = total_prize * 0.65
print(f"{end_prize:.2f} leva.")