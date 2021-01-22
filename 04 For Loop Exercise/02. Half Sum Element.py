import sys
n = int(input())
max_num = -sys.maxsize
total_sum = 0
for i in range (n):
    number = int(input())
    if number > max_num:
        max_num = number
    total_sum += number

other_sum = total_sum - max_num
if other_sum == max_num:
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print('No')
    print((f'Diff = {abs(max_num - other_sum)}'))