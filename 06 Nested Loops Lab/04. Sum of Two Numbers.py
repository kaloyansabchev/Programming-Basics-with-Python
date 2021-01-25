start_num = int(input())
end_num = int(input())
magic_num = int(input())
count = 0

is_found = False

for first in range(start_num, end_num +1):
    for second in range(start_num, end_num +1):
        count += 1
        if first + second == magic_num:
            is_found = True
            print(f'Combination N:{count} ({first} + {second} = {magic_num})')
            break
    if is_found:
        break

if not is_found:
    print(f'{count} combinations - neither equals {magic_num}')
