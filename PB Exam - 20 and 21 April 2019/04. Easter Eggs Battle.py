import sys
p_one_eggs = int(input())
p_two_eggs = int(input())
winner = input()

p_one_eggs_left = p_one_eggs
p_two_eggs_left = p_two_eggs
while winner != 'End of battle':
    if winner == 'one':
        p_two_eggs_left -= 1
    elif winner == 'two':
        p_one_eggs_left -= 1
    if p_one_eggs_left == 0:
        print(f"Player one is out of eggs. Player two has {p_two_eggs_left} eggs left.")
        break
    elif p_two_eggs_left == 0:
        print(f"Player two is out of eggs. Player one has {p_one_eggs_left} eggs left.")
        break
    winner = input()
if p_one_eggs_left and p_two_eggs_left > 0:
    print(f"Player one has {p_one_eggs_left} eggs left.")
    print(f"Player two has {p_two_eggs_left} eggs left.")