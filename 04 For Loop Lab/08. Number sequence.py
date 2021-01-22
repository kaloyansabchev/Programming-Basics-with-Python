import sys
numbers = int(input())

bigger_n = -sys.maxsize
smaller_n = sys.maxsize

for n in range(1, numbers+1):
    number = int(input())
    if number < smaller_n:
        smaller_n = number
    if number > bigger_n:
        bigger_n = number

print(f'Max number: {bigger_n}')
print(f'Min number: {smaller_n}')