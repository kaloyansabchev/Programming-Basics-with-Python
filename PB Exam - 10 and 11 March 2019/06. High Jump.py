hight_needed = int(input())
jump_hight = int(input())
starting_hight = hight_needed - 30
jumps = 0
not_successful_jump = 0

while not hight_needed <= jump_hight:
    if jump_hight >= starting_hight:
        jumps += 1
        starting_hight += 5
    else:
        not_successful_jump += 1
        jumps += 1
    if not_successful_jump == 3:
        print(f"Tihomir failed at {starting_hight - 5}cm after {jumps + 1} jumps.")
        break
    jump_hight = int(input())
if not_successful_jump == 3:
    pass
else:
    print(f"Tihomir succeeded, he jumped over {starting_hight}cm after {jumps + 1} jumps.")