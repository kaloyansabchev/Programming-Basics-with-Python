num = float(input())
edinica = input()
new_edinica = input()

if edinica == 'mm':
    if new_edinica == 'cm':
        result = num / 10
        print(f'{result:.3f}')
    elif new_edinica == 'm':
        result = num / 1000
        print(f'{result:.3f}')
elif edinica == 'cm':
    if new_edinica == 'mm':
        result = num * 10
        print(f'{result:.3f}')
    elif new_edinica == 'm':
        result = num / 100
        print(f'{result:.3f}')
elif edinica == "m":
    if new_edinica == "mm":
        result = num * 1000
        print(f'{result:.3f}')
    elif new_edinica == 'cm':
        result = num * 100
        print(f'{result:.3f}')